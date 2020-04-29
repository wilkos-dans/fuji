# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from fuji_server.models.base_model_ import Model
from fuji_server import util


class UniquenessOutput(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, guid: str=None, guid_scheme: str=None):  # noqa: E501
        """UniquenessOutput - a model defined in Swagger

        :param guid: The guid of this UniquenessOutput.  # noqa: E501
        :type guid: str
        :param guid_scheme: The guid_scheme of this UniquenessOutput.  # noqa: E501
        :type guid_scheme: str
        """
        self.swagger_types = {
            'guid': str,
            'guid_scheme': str
        }

        self.attribute_map = {
            'guid': 'guid',
            'guid_scheme': 'guid_scheme'
        }
        self._guid = guid
        self._guid_scheme = guid_scheme

    @classmethod
    def from_dict(cls, dikt) -> 'UniquenessOutput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Uniqueness_output of this UniquenessOutput.  # noqa: E501
        :rtype: UniquenessOutput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def guid(self) -> str:
        """Gets the guid of this UniquenessOutput.


        :return: The guid of this UniquenessOutput.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid: str):
        """Sets the guid of this UniquenessOutput.


        :param guid: The guid of this UniquenessOutput.
        :type guid: str
        """

        self._guid = guid

    @property
    def guid_scheme(self) -> str:
        """Gets the guid_scheme of this UniquenessOutput.


        :return: The guid_scheme of this UniquenessOutput.
        :rtype: str
        """
        return self._guid_scheme

    @guid_scheme.setter
    def guid_scheme(self, guid_scheme: str):
        """Sets the guid_scheme of this UniquenessOutput.


        :param guid_scheme: The guid_scheme of this UniquenessOutput.
        :type guid_scheme: str
        """

        self._guid_scheme = guid_scheme