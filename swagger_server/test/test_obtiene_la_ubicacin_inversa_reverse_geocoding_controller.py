# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_rev_geo_code import RequestRevGeoCode  # noqa: E501
from swagger_server.models.response_rev_geo_code import ResponseRevGeoCode  # noqa: E501
from swagger_server.test import BaseTestCase


class TestObtieneLaUbicacinInversaReverseGeocodingController(BaseTestCase):
    """ObtieneLaUbicacinInversaReverseGeocodingController integration test stubs"""

    def test_rev_geocode(self):
        """Test case for rev_geocode

        Obtiene la ubicación inversa
        """
        body = RequestRevGeoCode()
        response = self.client.open(
            '/revGeoCode',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
