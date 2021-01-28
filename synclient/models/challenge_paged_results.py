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


class ChallengePagedResults(object):
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
        'total_number_of_results': 'int',
        'results': 'list[Challenge]'
    }

    attribute_map = {
        'total_number_of_results': 'totalNumberOfResults',
        'results': 'results'
    }

    def __init__(self, total_number_of_results=None, results=None, local_vars_configuration=None):  # noqa: E501
        """ChallengePagedResults - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._total_number_of_results = None
        self._results = None
        self.discriminator = None

        if total_number_of_results is not None:
            self.total_number_of_results = total_number_of_results
        if results is not None:
            self.results = results

    @property
    def total_number_of_results(self):
        """Gets the total_number_of_results of this ChallengePagedResults.  # noqa: E501

        The total number of results  # noqa: E501

        :return: The total_number_of_results of this ChallengePagedResults.  # noqa: E501
        :rtype: int
        """
        return self._total_number_of_results

    @total_number_of_results.setter
    def total_number_of_results(self, total_number_of_results):
        """Sets the total_number_of_results of this ChallengePagedResults.

        The total number of results  # noqa: E501

        :param total_number_of_results: The total_number_of_results of this ChallengePagedResults.  # noqa: E501
        :type: int
        """

        self._total_number_of_results = total_number_of_results

    @property
    def results(self):
        """Gets the results of this ChallengePagedResults.  # noqa: E501

        The list of results for this page  # noqa: E501

        :return: The results of this ChallengePagedResults.  # noqa: E501
        :rtype: list[Challenge]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this ChallengePagedResults.

        The list of results for this page  # noqa: E501

        :param results: The results of this ChallengePagedResults.  # noqa: E501
        :type: list[Challenge]
        """

        self._results = results

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
        if not isinstance(other, ChallengePagedResults):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChallengePagedResults):
            return True

        return self.to_dict() != other.to_dict()
