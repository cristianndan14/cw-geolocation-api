# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DataGetLocation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, ip: str=None, latitude: float=None, longitude: float=None):  # noqa: E501
        """DataGetLocation - a model defined in Swagger

        :param ip: The ip of this DataGetLocation.  # noqa: E501
        :type ip: str
        :param latitude: The latitude of this DataGetLocation.  # noqa: E501
        :type latitude: float
        :param longitude: The longitude of this DataGetLocation.  # noqa: E501
        :type longitude: float
        """
        self.swagger_types = {
            'ip': str,
            'latitude': float,
            'longitude': float
        }

        self.attribute_map = {
            'ip': 'ip',
            'latitude': 'latitude',
            'longitude': 'longitude'
        }
        self._ip = ip
        self._latitude = latitude
        self._longitude = longitude

    @classmethod
    def from_dict(cls, dikt) -> 'DataGetLocation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DataGetLocation of this DataGetLocation.  # noqa: E501
        :rtype: DataGetLocation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ip(self) -> str:
        """Gets the ip of this DataGetLocation.


        :return: The ip of this DataGetLocation.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip: str):
        """Sets the ip of this DataGetLocation.


        :param ip: The ip of this DataGetLocation.
        :type ip: str
        """

        self._ip = ip

    @property
    def latitude(self) -> float:
        """Gets the latitude of this DataGetLocation.


        :return: The latitude of this DataGetLocation.
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: float):
        """Sets the latitude of this DataGetLocation.


        :param latitude: The latitude of this DataGetLocation.
        :type latitude: float
        """

        self._latitude = latitude

    @property
    def longitude(self) -> float:
        """Gets the longitude of this DataGetLocation.


        :return: The longitude of this DataGetLocation.
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: float):
        """Sets the longitude of this DataGetLocation.


        :param longitude: The longitude of this DataGetLocation.
        :type longitude: float
        """

        self._longitude = longitude
