# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.base_request import BaseRequest  # noqa: E501
from swagger_server.models.response_get_location import ResponseGetLocation  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGetLocationController(BaseTestCase):
    """GetLocationController integration test stubs"""

    def test_get_geolocation(self):
        """Test case for get_geolocation

        Obtener localizacion
        """
        body = BaseRequest()
        response = self.client.open(
            '/getLocation',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
