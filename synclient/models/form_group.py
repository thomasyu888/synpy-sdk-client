# coding: utf-8

"""
    Platform Repository Service

    Platform Repository Service - Sage Bionetworks Platform   # noqa: E501

    The version of the OpenAPI document: develop-SNAPSHOT
    Contact: thomas.yu@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from synclient.configuration import Configuration


class FormGroup(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'created_by': 'str',
        'created_on': 'str',
        'group_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'group_id': 'groupId',
        'name': 'name'
    }

    def __init__(self, created_by=None, created_on=None, group_id=None, name=None, local_vars_configuration=None):  # noqa: E501
        """FormGroup - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_by = None
        self._created_on = None
        self._group_id = None
        self._name = None
        self.discriminator = None

        if created_by is not None:
            self.created_by = created_by
        if created_on is not None:
            self.created_on = created_on
        if group_id is not None:
            self.group_id = group_id
        if name is not None:
            self.name = name

    @property
    def created_by(self):
        """Gets the created_by of this FormGroup.  # noqa: E501

        Id of the user that created this group  # noqa: E501

        :return: The created_by of this FormGroup.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this FormGroup.

        Id of the user that created this group  # noqa: E501

        :param created_by: The created_by of this FormGroup.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this FormGroup.  # noqa: E501

        The date this object was originally created.  # noqa: E501

        :return: The created_on of this FormGroup.  # noqa: E501
        :rtype: str
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this FormGroup.

        The date this object was originally created.  # noqa: E501

        :param created_on: The created_on of this FormGroup.  # noqa: E501
        :type: str
        """

        self._created_on = created_on

    @property
    def group_id(self):
        """Gets the group_id of this FormGroup.  # noqa: E501

        Unique identifier provided by the system.  # noqa: E501

        :return: The group_id of this FormGroup.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this FormGroup.

        Unique identifier provided by the system.  # noqa: E501

        :param group_id: The group_id of this FormGroup.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def name(self):
        """Gets the name of this FormGroup.  # noqa: E501

        Unique name for the group provided by the caller.  # noqa: E501

        :return: The name of this FormGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FormGroup.

        Unique name for the group provided by the caller.  # noqa: E501

        :param name: The name of this FormGroup.  # noqa: E501
        :type: str
        """

        self._name = name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FormGroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FormGroup):
            return True

        return self.to_dict() != other.to_dict()
