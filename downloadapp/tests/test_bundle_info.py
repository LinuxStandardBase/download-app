import unittest
from downloadapp import bundle_info

class TestBundleInfo(unittest.TestCase):

    def test_get_released_bundle_dir(self):
        dirs = ["something-6.0.0", "released-5.0.0", "released-2.3.0",
                "somethingelse"]
        self.assertEqual(bundle_info._get_released_bundle_dir(dirs),
                         "released-5.0.0")
