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


class SubmissionEligibility(object):
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
        'is_eligible': 'bool',
        'is_quota_filled': 'bool',
        'is_registered': 'bool'
    }

    attribute_map = {
        'is_eligible': 'isEligible',
        'is_quota_filled': 'isQuotaFilled',
        'is_registered': 'isRegistered'
    }

    def __init__(self, is_eligible=None, is_quota_filled=None, is_registered=None, local_vars_configuration=None):  # noqa: E501
        """SubmissionEligibility - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._is_eligible = None
        self._is_quota_filled = None
        self._is_registered = None
        self.discriminator = None

        if is_eligible is not None:
            self.is_eligible = is_eligible
        if is_quota_filled is not None:
            self.is_quota_filled = is_quota_filled
        if is_registered is not None:
            self.is_registered = is_registered

    @property
    def is_eligible(self):
        """Gets the is_eligible of this SubmissionEligibility.  # noqa: E501

        true if all criteria are met  # noqa: E501

        :return: The is_eligible of this SubmissionEligibility.  # noqa: E501
        :rtype: bool
        """
        return self._is_eligible

    @is_eligible.setter
    def is_eligible(self, is_eligible):
        """Sets the is_eligible of this SubmissionEligibility.

        true if all criteria are met  # noqa: E501

        :param is_eligible: The is_eligible of this SubmissionEligibility.  # noqa: E501
        :type: bool
        """

        self._is_eligible = is_eligible

    @property
    def is_quota_filled(self):
        """Gets the is_quota_filled of this SubmissionEligibility.  # noqa: E501

        true if team/individual has reached the submission quota (for the given submission round)  # noqa: E501

        :return: The is_quota_filled of this SubmissionEligibility.  # noqa: E501
        :rtype: bool
        """
        return self._is_quota_filled

    @is_quota_filled.setter
    def is_quota_filled(self, is_quota_filled):
        """Sets the is_quota_filled of this SubmissionEligibility.

        true if team/individual has reached the submission quota (for the given submission round)  # noqa: E501

        :param is_quota_filled: The is_quota_filled of this SubmissionEligibility.  # noqa: E501
        :type: bool
        """

        self._is_quota_filled = is_quota_filled

    @property
    def is_registered(self):
        """Gets the is_registered of this SubmissionEligibility.  # noqa: E501

        true if team/individual is registered for challenge  # noqa: E501

        :return: The is_registered of this SubmissionEligibility.  # noqa: E501
        :rtype: bool
        """
        return self._is_registered

    @is_registered.setter
    def is_registered(self, is_registered):
        """Sets the is_registered of this SubmissionEligibility.

        true if team/individual is registered for challenge  # noqa: E501

        :param is_registered: The is_registered of this SubmissionEligibility.  # noqa: E501
        :type: bool
        """

        self._is_registered = is_registered

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
        if not isinstance(other, SubmissionEligibility):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubmissionEligibility):
            return True

        return self.to_dict() != other.to_dict()
