import unittest

import unittest
from pyramid import testing

class ProjectorUnitTests(unittest.TestCase):
    def setUp(self):
        request = testing.DummyRequest()
        self.config = testing.setUp(request=request)

    def tearDown(self):
        testing.tearDown()

    def test_index_view(self):
        from views import Views
        self.assertEqual(1, 1)

        
class ProjectorFunctionalTests(unittest.TestCase):
    def setUp(self):
        from application import main
        app = main()
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_it(self):
        res = self.testapp.get('/', status=200)
        self.failUnless('Home' in res.body)
        res = self.testapp.get('/about.html', status=200)
        self.failUnless('autonomous' in res.body)
        res = self.testapp.get('/people', status=200)
        self.failUnless('Susan' in res.body)
        res = self.testapp.get('/acme', status=200)
        self.failUnless('Silly Slogans' in res.body)
        res = self.testapp.get('/updates.json', status=200)
        self.failUnless('888' in res.body)
