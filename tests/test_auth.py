import unittest
from flask_testing import TestCase
from app import app, db


class AuthTestCase(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        return app

    def setUp(self):
        db.create_all()
        self.client = app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_login(self):
        response = self.client.post('/login',
                                    data={'username': 'admin', 'password': 'admin'},
                                    follow_redirects=True)
        self.assert200(response)
        self.assertIn(b'You have successfully logged in', response.data)

    def test_logout(self):
        self.client.post('/login', data={'username': 'admin', 'password': 'admin'})
        response = self.client.get('/logout', follow_redirects=True)
        self.assert200(response)
        self.assertIn(b'You have successfully logged out', response.data)

    def test_login_invalid(self):
        self.client.get('/logout', follow_redirects=True)
        response = self.client.post('/login',
                                    data={'username': 'admin', 'password': 'wrong_password'},
                                    follow_redirects=True)
        self.assert200(response)
        self.assertIn(b'Invalid username or password. Please try again.', response.data)


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTest(loader.loadTestsFromTestCase(AuthTestCase))

    runner = unittest.TextTestRunner()
    runner.run(suite)
