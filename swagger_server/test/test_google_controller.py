# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.get_lat_lon import GetLatLon  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGoogleController(BaseTestCase):
    """GoogleController integration test stubs"""

    def test_get_latlon_get(self):
        """Test case for get_latlon_get

        obtener tiempo estimado
        """
        body = GetLatLon()
        response = self.client.open(
            '/v2/get_latlon',
            method='GET',
            data=json.dumps(body),
            content_type='text/plain; charset=utf-8 , text/plain; charset=utf-8')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
