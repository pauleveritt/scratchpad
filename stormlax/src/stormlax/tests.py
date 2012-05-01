import unittest

from pyramid.testing import DummyRequest
from pyramid.testing import setUp
from pyramid.testing import tearDown

class StormlaxViewsUnitTests(unittest.TestCase):
    def setUp(self):
        request = DummyRequest()
        self.config = setUp(request=request)

    def tearDown(self):
        tearDown()

    def _makeOne(self, request):
        from views import StormlaxViews

        inst = StormlaxViews(request)
        return inst

    def test_index_view(self):
        request = DummyRequest()
        inst = self._makeOne(request)
        result = inst.siteindex_view()
        self.assertEqual(result['page_title'], 'Home')

class StormlaxFunctionalTests(unittest.TestCase):
    def setUp(self):
        from stormlax import main
        d = '/Users/paul/projects/scratchpad/stormlax/var/import'
        config = {}
        settings = dict(import_dir=d)
        app = main(config, import_dir=d)
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_it(self):
        res = self.testapp.get('/', status=200)
        self.failUnless('Home' in str(res.body))