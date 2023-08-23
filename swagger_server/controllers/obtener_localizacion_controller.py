import connexion
import six

from swagger_server.models.base_request import BaseRequest  # noqa: E501
from swagger_server.models.response_get_location import ResponseGetLocation  # noqa: E501
from swagger_server import util


def get_geolocation(body=None):  # noqa: E501
    """Obtener localizacion

    Obtener localizacion # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ResponseGetLocation
    """
    if connexion.request.is_json:
        body = BaseRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
