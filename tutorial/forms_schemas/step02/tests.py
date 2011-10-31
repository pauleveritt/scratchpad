import unittest

from pyramid.testing import DummyRequest

class ProjectorViewsUnitTests(unittest.TestCase):

    def _makeOne(self, request):
        from views import ProjectorViews
        inst = ProjectorViews(request)
        return inst

    def test_site_view(self):
        request = DummyRequest()
        inst = self._makeOne(request)
        result = inst.site_view()
        self.assertTrue('form' in result.keys())

class ProjectorFunctionalTests(unittest.TestCase):
    def setUp(self):
        from application import main
        app = main()
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_GET(self):
        # Get the form
        res = self.testapp.get('/', status=200)
        self.failUnless('Hello Form' in res.body)

    def test_valid_POST(self):
        # Get the form
        res = self.testapp.get('/', status=200)
        self.failUnless('Hello Form' in res.body)
        form = res.form
        form['name'] = 'bobo'
        form['shoe_size'] = 22
        complete = form.submit()
        # XXX
        #self.failUnless('Valid form values' in complete.body)

    def test_invalid_POST(self):
        # Get the form
        res = self.testapp.get('/', status=200)
        form = res.form
        # XXX Copy from above, but fixed
        self.failUnless('Hello Form' in res.body)
