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
        res = self.testapp.get('/departments.html', status=200)
        self.failUnless('Departments' in res.body)
        res = self.testapp.get('/people.html', status=200)
        self.failUnless('People' in res.body)
        res = self.testapp.get('/projects.html', status=200)
        self.failUnless('Projects' in res.body)
