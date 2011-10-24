import unittest

class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from application import main
        app = main()
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_it(self):
        res = self.testapp.get('/', status=200)
        self.failUnless('Home' in res.body)
