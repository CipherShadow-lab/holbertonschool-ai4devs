"""Tests for the intentionally limited Mini DevSecOps Security Auditor."""

import unittest
from security_auditor import audit, check_configuration, scan_source, format_findings


SECURE = {"debug": False, "https_only": True, "session_cookie_secure": True}


class ConfigurationTests(unittest.TestCase):
    def test_secure_configuration(self):
        self.assertEqual(check_configuration(SECURE), [])

    def test_insecure_configuration(self):
        config = {"debug": True, "https_only": False,
                  "session_cookie_secure": False}
        findings = check_configuration(config)
        self.assertEqual(len(findings), 3)
        self.assertEqual([f.severity for f in findings],
                         ["HIGH", "HIGH", "MEDIUM"])

    def test_missing_settings(self):
        self.assertEqual(len(check_configuration({})), 3)

    def test_invalid_boolean(self):
        config = {**SECURE, "debug": "false"}
        self.assertIn("boolean", check_configuration(config)[0].message)

    def test_invalid_config_type(self):
        with self.assertRaises(TypeError):
            check_configuration(None)


class SecretTests(unittest.TestCase):
    def test_detects_assignment_and_line(self):
        findings = scan_source('x = 1\npassword = "actual-demo-value"', "app.py")
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].location, "app.py:2")

    def test_does_not_expose_value(self):
        secret = "do-not-display-this-value"
        findings = scan_source(f'api_key = "{secret}"')
        self.assertEqual(len(findings), 1)
        self.assertNotIn(secret, format_findings(findings))
        self.assertNotIn(secret, repr(findings))

    def test_ignores_placeholders_and_comments(self):
        source = '# password = "real-looking"\napi_key = "placeholder"\n'
        self.assertEqual(scan_source(source), [])

    def test_no_findings(self):
        self.assertEqual(scan_source('count = 3'), [])
        self.assertIn("No findings", format_findings([]))

    def test_multiple_findings(self):
        source = 'password = "one"\naccess_token = "two"'
        self.assertEqual(len(scan_source(source)), 2)

    def test_invalid_source(self):
        with self.assertRaises(TypeError):
            scan_source(None)

    def test_invalid_filename(self):
        with self.assertRaises(ValueError):
            scan_source('password = "abc"', "")

    def test_combined_audit(self):
        config = {**SECURE, "debug": True}
        findings = audit(config, 'secret_key = "example-secret"')
        self.assertEqual(len(findings), 2)


if __name__ == "__main__":
    unittest.main()
