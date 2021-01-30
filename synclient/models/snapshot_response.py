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


class SnapshotResponse(object):
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
        'snapshot_version_number': 'int'
    }

    attribute_map = {
        'snapshot_version_number': 'snapshotVersionNumber'
    }

    def __init__(self, snapshot_version_number=None, local_vars_configuration=None):  # noqa: E501
        """SnapshotResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._snapshot_version_number = None
        self.discriminator = None

        if snapshot_version_number is not None:
            self.snapshot_version_number = snapshot_version_number

    @property
    def snapshot_version_number(self):
        """Gets the snapshot_version_number of this SnapshotResponse.  # noqa: E501

        The version number of the resulting snapshot.  # noqa: E501

        :return: The snapshot_version_number of this SnapshotResponse.  # noqa: E501
        :rtype: int
        """
        return self._snapshot_version_number

    @snapshot_version_number.setter
    def snapshot_version_number(self, snapshot_version_number):
        """Sets the snapshot_version_number of this SnapshotResponse.

        The version number of the resulting snapshot.  # noqa: E501

        :param snapshot_version_number: The snapshot_version_number of this SnapshotResponse.  # noqa: E501
        :type: int
        """

        self._snapshot_version_number = snapshot_version_number

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
        if not isinstance(other, SnapshotResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnapshotResponse):
            return True

        return self.to_dict() != other.to_dict()