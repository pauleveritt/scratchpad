import unittest

from pyramid.testing import DummyRequest
from pyramid.testing import setUp
from pyramid.testing import tearDown

class ProjectorViewsUnitTests(unittest.TestCase):
    def setUp(self):
        request = DummyRequest()
        self.config = setUp(request=request)

    def tearDown(self):
        tearDown()

    def _makeOne(self, request):
        from .views import ProjectorViews

        inst = ProjectorViews(request)
        return inst

    def test_index_view(self):
        request = DummyRequest()
        inst = self._makeOne(request)
        result = inst.index_view()
        self.assertEqual(result['page_title'], 'Home')


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
