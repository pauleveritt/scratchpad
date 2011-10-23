import unittest

class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from application import main
        app = main()
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.failUnless('Home' in res.body)

    def test_it(self):
        res = self.testapp.get('/', status=200)
        self.failUnless('Home' in res.body)
        res = self.testapp.get('/about.html', status=200)
        self.failUnless('autonomous' in res.body)
        res = self.testapp.get('/people', status=200)
        self.failUnless('Susan' in res.body)
        res = self.testapp.get('/somecompany', status=200)
        self.failUnless('Silly Slogans' in res.body)
