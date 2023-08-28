import connexion
import six

from swagger_server.models.request_save_location_vendor import RequestSaveLocationVendor  # noqa: E501
from swagger_server.models.response_save_location_vendor import ResponseSaveLocationVendor  # noqa: E501
from swagger_server import util


def save_location_vendor(body=None):  # noqa: E501
    """Guardar localizacion de un vendedor

    Guardar localizacion de un vendedor # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ResponseSaveLocationVendor
    """
    if connexion.request.is_json:
        body = RequestSaveLocationVendor.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
