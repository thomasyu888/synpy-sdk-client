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


class ValidationSummaryStatistics(object):
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
        'container_id': 'str',
        'generated_on': 'str',
        'number_of_invalid_children': 'int',
        'number_of_unknown_children': 'int',
        'number_of_valid_children': 'int',
        'total_number_of_children': 'int'
    }

    attribute_map = {
        'container_id': 'containerId',
        'generated_on': 'generatedOn',
        'number_of_invalid_children': 'numberOfInvalidChildren',
        'number_of_unknown_children': 'numberOfUnknownChildren',
        'number_of_valid_children': 'numberOfValidChildren',
        'total_number_of_children': 'totalNumberOfChildren'
    }

    def __init__(self, container_id=None, generated_on=None, number_of_invalid_children=None, number_of_unknown_children=None, number_of_valid_children=None, total_number_of_children=None, local_vars_configuration=None):  # noqa: E501
        """ValidationSummaryStatistics - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._container_id = None
        self._generated_on = None
        self._number_of_invalid_children = None
        self._number_of_unknown_children = None
        self._number_of_valid_children = None
        self._total_number_of_children = None
        self.discriminator = None

        if container_id is not None:
            self.container_id = container_id
        if generated_on is not None:
            self.generated_on = generated_on
        if number_of_invalid_children is not None:
            self.number_of_invalid_children = number_of_invalid_children
        if number_of_unknown_children is not None:
            self.number_of_unknown_children = number_of_unknown_children
        if number_of_valid_children is not None:
            self.number_of_valid_children = number_of_valid_children
        if total_number_of_children is not None:
            self.total_number_of_children = total_number_of_children

    @property
    def container_id(self):
        """Gets the container_id of this ValidationSummaryStatistics.  # noqa: E501

        The ID of the container Entity.  # noqa: E501

        :return: The container_id of this ValidationSummaryStatistics.  # noqa: E501
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """Sets the container_id of this ValidationSummaryStatistics.

        The ID of the container Entity.  # noqa: E501

        :param container_id: The container_id of this ValidationSummaryStatistics.  # noqa: E501
        :type: str
        """

        self._container_id = container_id

    @property
    def generated_on(self):
        """Gets the generated_on of this ValidationSummaryStatistics.  # noqa: E501

        The date-time when the statistics were calculated.  # noqa: E501

        :return: The generated_on of this ValidationSummaryStatistics.  # noqa: E501
        :rtype: str
        """
        return self._generated_on

    @generated_on.setter
    def generated_on(self, generated_on):
        """Sets the generated_on of this ValidationSummaryStatistics.

        The date-time when the statistics were calculated.  # noqa: E501

        :param generated_on: The generated_on of this ValidationSummaryStatistics.  # noqa: E501
        :type: str
        """

        self._generated_on = generated_on

    @property
    def number_of_invalid_children(self):
        """Gets the number_of_invalid_children of this ValidationSummaryStatistics.  # noqa: E501

        The total number of children that are invalid according to their bound JSON schema.  # noqa: E501

        :return: The number_of_invalid_children of this ValidationSummaryStatistics.  # noqa: E501
        :rtype: int
        """
        return self._number_of_invalid_children

    @number_of_invalid_children.setter
    def number_of_invalid_children(self, number_of_invalid_children):
        """Sets the number_of_invalid_children of this ValidationSummaryStatistics.

        The total number of children that are invalid according to their bound JSON schema.  # noqa: E501

        :param number_of_invalid_children: The number_of_invalid_children of this ValidationSummaryStatistics.  # noqa: E501
        :type: int
        """

        self._number_of_invalid_children = number_of_invalid_children

    @property
    def number_of_unknown_children(self):
        """Gets the number_of_unknown_children of this ValidationSummaryStatistics.  # noqa: E501

        The total number of children that do not have validation results. This can occur when a child does not have a bound JSON schema or when a child has not been validated yet.  # noqa: E501

        :return: The number_of_unknown_children of this ValidationSummaryStatistics.  # noqa: E501
        :rtype: int
        """
        return self._number_of_unknown_children

    @number_of_unknown_children.setter
    def number_of_unknown_children(self, number_of_unknown_children):
        """Sets the number_of_unknown_children of this ValidationSummaryStatistics.

        The total number of children that do not have validation results. This can occur when a child does not have a bound JSON schema or when a child has not been validated yet.  # noqa: E501

        :param number_of_unknown_children: The number_of_unknown_children of this ValidationSummaryStatistics.  # noqa: E501
        :type: int
        """

        self._number_of_unknown_children = number_of_unknown_children

    @property
    def number_of_valid_children(self):
        """Gets the number_of_valid_children of this ValidationSummaryStatistics.  # noqa: E501

        The total number of children that are valid according to their bound JSON schema.  # noqa: E501

        :return: The number_of_valid_children of this ValidationSummaryStatistics.  # noqa: E501
        :rtype: int
        """
        return self._number_of_valid_children

    @number_of_valid_children.setter
    def number_of_valid_children(self, number_of_valid_children):
        """Sets the number_of_valid_children of this ValidationSummaryStatistics.

        The total number of children that are valid according to their bound JSON schema.  # noqa: E501

        :param number_of_valid_children: The number_of_valid_children of this ValidationSummaryStatistics.  # noqa: E501
        :type: int
        """

        self._number_of_valid_children = number_of_valid_children

    @property
    def total_number_of_children(self):
        """Gets the total_number_of_children of this ValidationSummaryStatistics.  # noqa: E501

        The total number of children in the container.  # noqa: E501

        :return: The total_number_of_children of this ValidationSummaryStatistics.  # noqa: E501
        :rtype: int
        """
        return self._total_number_of_children

    @total_number_of_children.setter
    def total_number_of_children(self, total_number_of_children):
        """Sets the total_number_of_children of this ValidationSummaryStatistics.

        The total number of children in the container.  # noqa: E501

        :param total_number_of_children: The total_number_of_children of this ValidationSummaryStatistics.  # noqa: E501
        :type: int
        """

        self._total_number_of_children = total_number_of_children

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
        if not isinstance(other, ValidationSummaryStatistics):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ValidationSummaryStatistics):
            return True

        return self.to_dict() != other.to_dict()
