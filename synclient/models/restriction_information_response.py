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


class RestrictionInformationResponse(object):
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
        'has_unmet_access_requirement': 'bool',
        'restriction_level': 'RestrictionLevel'
    }

    attribute_map = {
        'has_unmet_access_requirement': 'hasUnmetAccessRequirement',
        'restriction_level': 'restrictionLevel'
    }

    def __init__(self, has_unmet_access_requirement=None, restriction_level=None, local_vars_configuration=None):  # noqa: E501
        """RestrictionInformationResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._has_unmet_access_requirement = None
        self._restriction_level = None
        self.discriminator = None

        if has_unmet_access_requirement is not None:
            self.has_unmet_access_requirement = has_unmet_access_requirement
        if restriction_level is not None:
            self.restriction_level = restriction_level

    @property
    def has_unmet_access_requirement(self):
        """Gets the has_unmet_access_requirement of this RestrictionInformationResponse.  # noqa: E501

        True if user has at least one unmet access requirement on this restrict-able object; false otherwise.  # noqa: E501

        :return: The has_unmet_access_requirement of this RestrictionInformationResponse.  # noqa: E501
        :rtype: bool
        """
        return self._has_unmet_access_requirement

    @has_unmet_access_requirement.setter
    def has_unmet_access_requirement(self, has_unmet_access_requirement):
        """Sets the has_unmet_access_requirement of this RestrictionInformationResponse.

        True if user has at least one unmet access requirement on this restrict-able object; false otherwise.  # noqa: E501

        :param has_unmet_access_requirement: The has_unmet_access_requirement of this RestrictionInformationResponse.  # noqa: E501
        :type: bool
        """

        self._has_unmet_access_requirement = has_unmet_access_requirement

    @property
    def restriction_level(self):
        """Gets the restriction_level of this RestrictionInformationResponse.  # noqa: E501


        :return: The restriction_level of this RestrictionInformationResponse.  # noqa: E501
        :rtype: RestrictionLevel
        """
        return self._restriction_level

    @restriction_level.setter
    def restriction_level(self, restriction_level):
        """Sets the restriction_level of this RestrictionInformationResponse.


        :param restriction_level: The restriction_level of this RestrictionInformationResponse.  # noqa: E501
        :type: RestrictionLevel
        """

        self._restriction_level = restriction_level

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
        if not isinstance(other, RestrictionInformationResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RestrictionInformationResponse):
            return True

        return self.to_dict() != other.to_dict()
