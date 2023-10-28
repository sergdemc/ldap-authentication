import unittest
import subprocess
from flask_testing import TestCase
from app import app, db


class UserAddTestCase(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        return app

    def setUp(self):
        db.create_all()
        self.client = app.test_client()

    def tearDown(self):
        try:
            ldapdelete_command = [
                'ldapdelete', '-x', '-D', 'cn=admin,dc=example,dc=org', '-w', 'admin', 'cn=Test_User,dc=example,dc=org'
            ]
            subprocess.check_call(ldapdelete_command)
        except subprocess.CalledProcessError:
            self.fail('Error executing ldapdelete command')

        db.session.remove()
        db.drop_all()

    def test_add_user_and_login(self):
        # Выполните команду ldapadd для добавления нового пользователя в LDAP
        try:
            ldapadd_command = [
                'ldapadd', '-x', '-D', 'cn=admin,dc=example,dc=org', '-w', 'admin', '-f', 'new_user.ldif'
            ]
            subprocess.check_call(ldapadd_command)

            # После успешного добавления пользователя в LDAP, проверьте его аутентификацию через /login
            response = self.client.post('/login', data={'username': 'Test_User', 'password': 'test_password'},
                                        follow_redirects=True)
            self.assert200(response)
            self.assertIn(b'You have successfully logged in', response.data)

        except subprocess.CalledProcessError:
            # Если команда ldapadd завершилась с ошибкой, вы можете обработать ошибку или вывести сообщение
            self.fail('Error executing ldapadd command')


if __name__ == '__main__':
    unittest.main()
