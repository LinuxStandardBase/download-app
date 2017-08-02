import unittest
from downloadapp import bundle_info

class TestBundleInfo(unittest.TestCase):

    def test_get_released_bundle_dir(self):
        dirs = ["something-6.0.0", "released-5.0.0", "released-2.3.0",
                "somethingelse"]
        self.assertEqual(bundle_info._get_released_bundle_dir(dirs),
                         "released-5.0.0")

    def test_arch_name_from_filename(self):
        tests = [("lsb-app-checker-5.0.0-3.s390x.tar.gz", "s390x"),
                 ("lsb-dist-testkit-manager-5.0.0-2.ppc32.tar.gz", "ppc32"),
                 ("lsb-sdk-5.0.0-3.x86_64.tar.gz", "x86_64")]
        for (fn, result) in tests:
            self.assertEqual(bundle_info._arch_name_from_filename(fn),
                             result)

    def test_get_grouped_paths(self):
        paths = ['released-5.0.0/app-testkit/lsb-app-checker-5.0.0-3.ia32.tar.gz',
                 'released-5.0.0/app-testkit/lsb-app-checker-5.0.0-3.ia64.tar.gz',
                 'released-5.0.0/app-testkit/lsb-app-checker-5.0.0-3.ppc32.tar.gz',
                 'released-5.0.0/app-testkit/lsb-app-checker-5.0.0-3.ppc64.tar.gz',
                 'released-5.0.0/app-testkit/lsb-app-checker-5.0.0-3.s390.tar.gz',
                 'released-5.0.0/app-testkit/lsb-app-checker-5.0.0-3.s390x.tar.gz',
                 'released-5.0.0/app-testkit/lsb-app-checker-5.0.0-3.x86_64.tar.gz',
                 'released-5.0.0/app-testkit/lsb-app-checker-local-5.0.0-3.ia32.tar.gz',
                 'released-5.0.0/app-testkit/lsb-app-checker-local-5.0.0-3.ia64.tar.gz',
                 'released-5.0.0/app-testkit/lsb-app-checker-local-5.0.0-3.ppc32.tar.gz',
                 'released-5.0.0/app-testkit/lsb-app-checker-local-5.0.0-3.ppc64.tar.gz',
                 'released-5.0.0/app-testkit/lsb-app-checker-local-5.0.0-3.s390.tar.gz',
                 'released-5.0.0/app-testkit/lsb-app-checker-local-5.0.0-3.s390x.tar.gz',
                 'released-5.0.0/app-testkit/lsb-app-checker-local-5.0.0-3.x86_64.tar.gz']
        identifiers = [('-local', "local"), ('', "pkg")]
        results = bundle_info._get_grouped_paths(paths, identifiers)
        self.assertEqual(results["ia64"]["pkg"],
                         'released-5.0.0/app-testkit/lsb-app-checker-5.0.0-3.ia64.tar.gz')
        self.assertEqual(results["ppc32"]["local"],
                         'released-5.0.0/app-testkit/lsb-app-checker-local-5.0.0-3.ppc32.tar.gz')
