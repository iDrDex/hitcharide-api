import shutil
import tempfile
import errno

from django.test.utils import override_settings
from rest_framework.test import APITestCase as BaseAPITestCase
from rest_framework import status

from apps.accounts.factories import UserFactory


class APITestCase(BaseAPITestCase):
    def setUp(self):
        super(APITestCase, self).setUp()
        self.username = 'user@test.test'
        self.password = 'password'
        self.user = UserFactory.create(
            email=self.username,
            password=self.password)

    def authenticate_as(self, username, password):
        self.client.login(username=username, password=password)

    def authenticate(self):
        self.authenticate_as(self.username, self.password)

    def assertSuccessResponse(self, resp):
        if resp.status_code not in range(200, 300):
            raise self.failureException(
                'Response status is not success. '
                'Response data is:\n{0}'.format(resp.data))

    def assertNotAllowed(self, resp):
        self.assertEqual(resp.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def assertBadRequest(self, resp):
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def assertUnauthorized(self, resp):
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def assertForbidden(self, resp):
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

    def assertNotFound(self, resp):
        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)

    def fake_media(self):
        tmp_dir = tempfile.mkdtemp()

        try:
            return override_settings(MEDIA_ROOT=tmp_dir)
        finally:
            try:
                shutil.rmtree(tmp_dir)
            except OSError as e:
                # Reraise unless ENOENT: No such file or directory
                # (ok if directory has already been deleted)
                if e.errno != errno.ENOENT:
                    raise