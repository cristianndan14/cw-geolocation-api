import connexion
import six

from swagger_server.models.request_rev_geo_code import RequestRevGeoCode  # noqa: E501
from swagger_server.models.response_rev_geo_code import ResponseRevGeoCode  # noqa: E501
from swagger_server import util


def rev_geocode(body=None):  # noqa: E501
    """Obtiene la ubicación inversa

    Obtiene la ubicación inversa (reverse geocoding) basada en las coordenadas proporcionadas. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ResponseRevGeoCode
    """
    if connexion.request.is_json:
        body = RequestRevGeoCode.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
