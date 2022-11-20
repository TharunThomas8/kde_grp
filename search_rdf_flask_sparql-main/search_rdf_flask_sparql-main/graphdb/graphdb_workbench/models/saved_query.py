# coding: utf-8

"""
    GraphDB Workbench API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from graphdb.graphdb_workbench.configuration import Configuration


class SavedQuery(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'body': 'str',
        'name': 'str',
        'shared': 'bool'
    }

    attribute_map = {
        'body': 'body',
        'name': 'name',
        'shared': 'shared'
    }

    def __init__(self, body=None, name=None, shared=None, _configuration=None):  # noqa: E501
        """SavedQuery - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._body = None
        self._name = None
        self._shared = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if name is not None:
            self.name = name
        if shared is not None:
            self.shared = shared

    @property
    def body(self):
        """Gets the body of this SavedQuery.  # noqa: E501


        :return: The body of this SavedQuery.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this SavedQuery.


        :param body: The body of this SavedQuery.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def name(self):
        """Gets the name of this SavedQuery.  # noqa: E501


        :return: The name of this SavedQuery.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SavedQuery.


        :param name: The name of this SavedQuery.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def shared(self):
        """Gets the shared of this SavedQuery.  # noqa: E501


        :return: The shared of this SavedQuery.  # noqa: E501
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this SavedQuery.


        :param shared: The shared of this SavedQuery.  # noqa: E501
        :type: bool
        """

        self._shared = shared

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SavedQuery, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SavedQuery):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SavedQuery):
            return True

        return self.to_dict() != other.to_dict()
