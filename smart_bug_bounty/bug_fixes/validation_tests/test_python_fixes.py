import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "bug_fixes"))
import unittest
from bug1_fixed import build_database, find_role
from bug4_fixed import register_user, verify_password

class FixTests(unittest.TestCase):
    def test_known_alex(self):
        db=build_database(); self.assertEqual(find_role(db,"alex"),"viewer"); db.close()
    def test_known_sam(self):
        db=build_database(); self.assertEqual(find_role(db,"sam"),"admin"); db.close()
    def test_unknown(self):
        db=build_database(); self.assertIsNone(find_role(db,"unknown")); db.close()
    def test_injection_literal(self):
        db=build_database(); self.assertIsNone(find_role(db,"' OR 1=1 --")); db.close()
    def test_correct_password(self):
        a={}; register_user(a,"alex","secret"); self.assertTrue(verify_password(a,"alex","secret"))
    def test_wrong_password(self):
        a={}; register_user(a,"alex","secret"); self.assertFalse(verify_password(a,"alex","wrong"))
    def test_unknown_account(self):
        self.assertFalse(verify_password({},"alex","secret"))
    def test_no_plaintext(self):
        a={}; register_user(a,"alex","secret"); self.assertNotIn("password",a["alex"])
    def test_duplicate(self):
        a={}; register_user(a,"alex","secret")
        with self.assertRaises(ValueError): register_user(a,"alex","other")
    def test_missing(self):
        with self.assertRaises(ValueError): register_user({},"","secret")
    def test_distinct_salts(self):
        a={}; register_user(a,"alex","same"); register_user(a,"sam","same")
        self.assertNotEqual(a["alex"]["salt"],a["sam"]["salt"])
if __name__=="__main__": unittest.main()
