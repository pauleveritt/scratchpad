import unittest

class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from application import main
        app = main()
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_it(self):
        res = self.testapp.get('/', status=200)
        self.failUnless('SiteFolder' in res.body)
        res = self.testapp.get('/folder1', status=200)
        self.failUnless('Folder' in res.body)
        res = self.testapp.get('/doc1', status=200)
        self.failUnless('Document' in res.body)
        res = self.testapp.get('/doc2', status=200)
        self.failUnless('Document' in res.body)
        res = self.testapp.get('/folder1/doc1', status=200)
        self.failUnless('Document' in res.body)
