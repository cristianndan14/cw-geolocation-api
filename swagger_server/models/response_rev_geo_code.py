# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.base_response import BaseResponse  # noqa: F401,E501
from swagger_server import util


class ResponseRevGeoCode(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, channel: str=None, external_transaction_id: str=None, internal_transaction_id: str=None, code: str=None, message: str=None, data: object=None):  # noqa: E501
        """ResponseRevGeoCode - a model defined in Swagger

        :param channel: The channel of this ResponseRevGeoCode.  # noqa: E501
        :type channel: str
        :param external_transaction_id: The external_transaction_id of this ResponseRevGeoCode.  # noqa: E501
        :type external_transaction_id: str
        :param internal_transaction_id: The internal_transaction_id of this ResponseRevGeoCode.  # noqa: E501
        :type internal_transaction_id: str
        :param code: The code of this ResponseRevGeoCode.  # noqa: E501
        :type code: str
        :param message: The message of this ResponseRevGeoCode.  # noqa: E501
        :type message: str
        :param data: The data of this ResponseRevGeoCode.  # noqa: E501
        :type data: object
        """
        self.swagger_types = {
            'channel': str,
            'external_transaction_id': str,
            'internal_transaction_id': str,
            'code': str,
            'message': str,
            'data': object
        }

        self.attribute_map = {
            'channel': 'channel',
            'external_transaction_id': 'externalTransactionId',
            'internal_transaction_id': 'internalTransactionId',
            'code': 'code',
            'message': 'message',
            'data': 'data'
        }
        self._channel = channel
        self._external_transaction_id = external_transaction_id
        self._internal_transaction_id = internal_transaction_id
        self._code = code
        self._message = message
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseRevGeoCode':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseRevGeoCode of this ResponseRevGeoCode.  # noqa: E501
        :rtype: ResponseRevGeoCode
        """
        return util.deserialize_model(dikt, cls)

    @property
    def channel(self) -> str:
        """Gets the channel of this ResponseRevGeoCode.


        :return: The channel of this ResponseRevGeoCode.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel: str):
        """Sets the channel of this ResponseRevGeoCode.


        :param channel: The channel of this ResponseRevGeoCode.
        :type channel: str
        """

        self._channel = channel

    @property
    def external_transaction_id(self) -> str:
        """Gets the external_transaction_id of this ResponseRevGeoCode.


        :return: The external_transaction_id of this ResponseRevGeoCode.
        :rtype: str
        """
        return self._external_transaction_id

    @external_transaction_id.setter
    def external_transaction_id(self, external_transaction_id: str):
        """Sets the external_transaction_id of this ResponseRevGeoCode.


        :param external_transaction_id: The external_transaction_id of this ResponseRevGeoCode.
        :type external_transaction_id: str
        """

        self._external_transaction_id = external_transaction_id

    @property
    def internal_transaction_id(self) -> str:
        """Gets the internal_transaction_id of this ResponseRevGeoCode.


        :return: The internal_transaction_id of this ResponseRevGeoCode.
        :rtype: str
        """
        return self._internal_transaction_id

    @internal_transaction_id.setter
    def internal_transaction_id(self, internal_transaction_id: str):
        """Sets the internal_transaction_id of this ResponseRevGeoCode.


        :param internal_transaction_id: The internal_transaction_id of this ResponseRevGeoCode.
        :type internal_transaction_id: str
        """

        self._internal_transaction_id = internal_transaction_id

    @property
    def code(self) -> str:
        """Gets the code of this ResponseRevGeoCode.


        :return: The code of this ResponseRevGeoCode.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this ResponseRevGeoCode.


        :param code: The code of this ResponseRevGeoCode.
        :type code: str
        """

        self._code = code

    @property
    def message(self) -> str:
        """Gets the message of this ResponseRevGeoCode.


        :return: The message of this ResponseRevGeoCode.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this ResponseRevGeoCode.


        :param message: The message of this ResponseRevGeoCode.
        :type message: str
        """

        self._message = message

    @property
    def data(self) -> object:
        """Gets the data of this ResponseRevGeoCode.


        :return: The data of this ResponseRevGeoCode.
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data: object):
        """Sets the data of this ResponseRevGeoCode.


        :param data: The data of this ResponseRevGeoCode.
        :type data: object
        """

        self._data = data
