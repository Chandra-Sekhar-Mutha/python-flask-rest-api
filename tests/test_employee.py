import time
from http import HTTPStatus
from unittest.mock import patch, Mock
from flask import json
from flask_testing import TestCase

class TestEmployee(TestCase):
    @patch("requests.get")
    def test_api_get_employees_db(self, mock_get_representative):
        mock_get_response = Mock()
        mock_get_response.json.return_value = self.expected_representative
        mock_get_response.status_code = HTTPStatus.OK

        mock_get_representative.return_value = mock_get_response
        mock_get_representative.raise_for_status = json.dumps(HTTPStatus.OK)

        response = self.client.get(
            f"/db",
            headers={"Authorization": AUTH_COOKIE["Authorization"].value},
            follow_redirects=True,
            content_type="application/json",
        )
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)
        self.assertEqual(2, len(response.json.employees))