# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_save_location_vendor import RequestSaveLocationVendor  # noqa: E501
from swagger_server.models.response_save_location_vendor import ResponseSaveLocationVendor  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGuardarLocalizacionDeUnVendedorController(BaseTestCase):
    """GuardarLocalizacionDeUnVendedorController integration test stubs"""

    def test_save_location_vendor(self):
        """Test case for save_location_vendor

        Guardar localizacion de un vendedor
        """
        body = RequestSaveLocationVendor()
        response = self.client.open(
            '/saveLocationVendor',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
