"""Small, dependency-free educational security auditor.

Checks an explicitly defined configuration schema and simple credential assignments.
Not a substitute for a production secrets scanner or security assessment.
"""

from dataclasses import dataclass
import re
from typing import Any


@dataclass(frozen=True)
class Finding:
    category: str
    severity: str
    location: str
    message: str


# Only boolean values are valid for these example configuration settings.
CONFIG_RULES = {
    "debug": (False, "HIGH", "Debug mode should be disabled"),
    "https_only": (True, "HIGH", "HTTPS enforcement should be enabled"),
    "session_cookie_secure": (
        True, "MEDIUM", "Session cookies should use the Secure flag"
    ),
}

# Intentionally narrow: assignments to clearly credential-related identifiers.
# Values are never included in findings.
CREDENTIAL_ASSIGNMENT = re.compile(
    r"(?i)\b(?P<name>api_key|secret_key|password|access_token)\b"
    r"\s*=\s*(?P<quote>['\"])(?P<value>[^'\"\r\n]+)(?P=quote)"
)
PLACEHOLDERS = {"", "example", "placeholder", "changeme", "your_key_here"}


def check_configuration(config: dict[str, Any]) -> list[Finding]:
    """Flag insecure or missing settings in the supported configuration schema."""
    if not isinstance(config, dict):
        raise TypeError("config must be a dictionary")

    findings = []
    for key, (secure_value, severity, explanation) in CONFIG_RULES.items():
        if key not in config:
            findings.append(Finding("configuration", "MEDIUM", key,
                                    "Required security setting is missing"))
        elif type(config[key]) is not bool:
            findings.append(Finding("configuration", "MEDIUM", key,
                                    "Security setting must be a boolean"))
        elif config[key] != secure_value:
            findings.append(Finding("configuration", severity, key, explanation))
    return findings


def scan_source(source: str, filename: str = "source") -> list[Finding]:
    """Flag simple credential assignments without exposing their values."""
    if not isinstance(source, str):
        raise TypeError("source must be a string")
    if not isinstance(filename, str) or not filename:
        raise ValueError("filename must be a nonempty string")

    findings = []
    for line_number, line in enumerate(source.splitlines(), start=1):
        # Ignore simple full-line comments; inline comments are not parsed.
        if line.lstrip().startswith(("#", "//")):
            continue
        for match in CREDENTIAL_ASSIGNMENT.finditer(line):
            if match.group("value").strip().lower() in PLACEHOLDERS:
                continue
            findings.append(Finding(
                "hardcoded-secret", "HIGH", f"{filename}:{line_number}",
                f"Possible hardcoded credential assigned to {match.group('name')}"
            ))
    return findings


def audit(config: dict[str, Any], source: str,
          filename: str = "source") -> list[Finding]:
    """Run both independent checks and return structured findings."""
    return check_configuration(config) + scan_source(source, filename)


def format_findings(findings: list[Finding]) -> str:
    """Render safe, readable summaries without secret values."""
    if not findings:
        return "No findings from the supported checks."
    return "\n".join(
        f"[{finding.severity}] {finding.location}: {finding.message}"
        for finding in findings
    )


if __name__ == "__main__":
    sample_config = {
        "debug": True,
        "https_only": False,
        "session_cookie_secure": True,
    }
    sample_source = 'api_key = "demo-not-a-real-key"\n'
    print(format_findings(audit(sample_config, sample_source, "example.py")))
