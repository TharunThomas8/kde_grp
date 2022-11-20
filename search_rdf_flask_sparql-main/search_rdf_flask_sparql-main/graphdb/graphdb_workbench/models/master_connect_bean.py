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


class MasterConnectBean(object):
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
        'bidirectional': 'bool',
        'master_location': 'str',
        'master_node_id': 'str',
        'peer_location': 'str',
        'peer_node_id': 'str',
        'peer_repository_id': 'str'
    }

    attribute_map = {
        'bidirectional': 'bidirectional',
        'master_location': 'masterLocation',
        'master_node_id': 'masterNodeID',
        'peer_location': 'peerLocation',
        'peer_node_id': 'peerNodeID',
        'peer_repository_id': 'peerRepositoryID'
    }

    def __init__(self, bidirectional=None, master_location=None, master_node_id=None, peer_location=None, peer_node_id=None, peer_repository_id=None, _configuration=None):  # noqa: E501
        """MasterConnectBean - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bidirectional = None
        self._master_location = None
        self._master_node_id = None
        self._peer_location = None
        self._peer_node_id = None
        self._peer_repository_id = None
        self.discriminator = None

        if bidirectional is not None:
            self.bidirectional = bidirectional
        if master_location is not None:
            self.master_location = master_location
        if master_node_id is not None:
            self.master_node_id = master_node_id
        if peer_location is not None:
            self.peer_location = peer_location
        if peer_node_id is not None:
            self.peer_node_id = peer_node_id
        if peer_repository_id is not None:
            self.peer_repository_id = peer_repository_id

    @property
    def bidirectional(self):
        """Gets the bidirectional of this MasterConnectBean.  # noqa: E501


        :return: The bidirectional of this MasterConnectBean.  # noqa: E501
        :rtype: bool
        """
        return self._bidirectional

    @bidirectional.setter
    def bidirectional(self, bidirectional):
        """Sets the bidirectional of this MasterConnectBean.


        :param bidirectional: The bidirectional of this MasterConnectBean.  # noqa: E501
        :type: bool
        """

        self._bidirectional = bidirectional

    @property
    def master_location(self):
        """Gets the master_location of this MasterConnectBean.  # noqa: E501


        :return: The master_location of this MasterConnectBean.  # noqa: E501
        :rtype: str
        """
        return self._master_location

    @master_location.setter
    def master_location(self, master_location):
        """Sets the master_location of this MasterConnectBean.


        :param master_location: The master_location of this MasterConnectBean.  # noqa: E501
        :type: str
        """

        self._master_location = master_location

    @property
    def master_node_id(self):
        """Gets the master_node_id of this MasterConnectBean.  # noqa: E501


        :return: The master_node_id of this MasterConnectBean.  # noqa: E501
        :rtype: str
        """
        return self._master_node_id

    @master_node_id.setter
    def master_node_id(self, master_node_id):
        """Sets the master_node_id of this MasterConnectBean.


        :param master_node_id: The master_node_id of this MasterConnectBean.  # noqa: E501
        :type: str
        """

        self._master_node_id = master_node_id

    @property
    def peer_location(self):
        """Gets the peer_location of this MasterConnectBean.  # noqa: E501


        :return: The peer_location of this MasterConnectBean.  # noqa: E501
        :rtype: str
        """
        return self._peer_location

    @peer_location.setter
    def peer_location(self, peer_location):
        """Sets the peer_location of this MasterConnectBean.


        :param peer_location: The peer_location of this MasterConnectBean.  # noqa: E501
        :type: str
        """

        self._peer_location = peer_location

    @property
    def peer_node_id(self):
        """Gets the peer_node_id of this MasterConnectBean.  # noqa: E501


        :return: The peer_node_id of this MasterConnectBean.  # noqa: E501
        :rtype: str
        """
        return self._peer_node_id

    @peer_node_id.setter
    def peer_node_id(self, peer_node_id):
        """Sets the peer_node_id of this MasterConnectBean.


        :param peer_node_id: The peer_node_id of this MasterConnectBean.  # noqa: E501
        :type: str
        """

        self._peer_node_id = peer_node_id

    @property
    def peer_repository_id(self):
        """Gets the peer_repository_id of this MasterConnectBean.  # noqa: E501


        :return: The peer_repository_id of this MasterConnectBean.  # noqa: E501
        :rtype: str
        """
        return self._peer_repository_id

    @peer_repository_id.setter
    def peer_repository_id(self, peer_repository_id):
        """Sets the peer_repository_id of this MasterConnectBean.


        :param peer_repository_id: The peer_repository_id of this MasterConnectBean.  # noqa: E501
        :type: str
        """

        self._peer_repository_id = peer_repository_id

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
        if issubclass(MasterConnectBean, dict):
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
        if not isinstance(other, MasterConnectBean):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MasterConnectBean):
            return True

        return self.to_dict() != other.to_dict()
