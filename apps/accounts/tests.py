from api.tests import APITestCase
from apps.accounts.factories import UserFactory
from apps.accounts.models import User


class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data = {
            'email': 'test@test.test',
            'phone': '+7 933 000 00 00',
            'first_name': 'first',
            'last_name': 'last',
            'age': 25,
            'password': '123'
        }

        resp = self.client.post('/accounts/register/', data, format='json')

        user = User.objects.get(pk=resp.data['pk'])
        self.assertEqual(user.first_name, 'first')
        self.assertEqual(user.last_name, 'last')
        self.assertEqual(user.age, 25)
        self.assertTrue(user.check_password('123'))
        self.assertEqual(user.email, 'test@test.test')
        self.assertEqual(user.username, 'test@test.test')
        # TODO check is active!!!

    def test_registration_params_set(self):
        data = {
            'email': 'test@test.test',
            'password': '123',
        }

        resp = self.client.post('/accounts/register/', data, format='json')
        self.assertBadRequest(resp)

        data['phone'] = '+7 933 000 00 00'
        resp = self.client.post('/accounts/register/', data, format='json')
        self.assertBadRequest(resp)

        data['first_name'] = 'first name'
        resp = self.client.post('/accounts/register/', data, format='json')
        self.assertBadRequest(resp)

        data['last_name'] = 'last name'
        resp = self.client.post('/accounts/register/', data, format='json')
        self.assertEqual(resp.status_code, 201)

    def test_registration_existing_email(self):
        user = UserFactory.create()
        data = {
            'email': user.email,
            'phone': '+7 933 000 00 00',
            'first_name': 'first',
            'last_name': 'last',
            'age': 25,
            'password': '123'
        }

        resp = self.client.post('/accounts/register/', data, format='json')
        self.assertBadRequest(resp)
