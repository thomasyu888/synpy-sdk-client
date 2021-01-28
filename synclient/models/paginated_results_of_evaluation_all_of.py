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


class PaginatedResultsOfEvaluationAllOf(object):
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
        'access_type': 'str',
        'active_only': 'str',
        'evaluation_ids': 'str',
        'results': 'list[Evaluation]',
        'total_number_of_results': 'int'
    }

    attribute_map = {
        'access_type': 'accessType',
        'active_only': 'activeOnly',
        'evaluation_ids': 'evaluationIds',
        'results': 'results',
        'total_number_of_results': 'totalNumberOfResults'
    }

    def __init__(self, access_type=None, active_only=None, evaluation_ids=None, results=None, total_number_of_results=None, local_vars_configuration=None):  # noqa: E501
        """PaginatedResultsOfEvaluationAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_type = None
        self._active_only = None
        self._evaluation_ids = None
        self._results = None
        self._total_number_of_results = None
        self.discriminator = None

        if access_type is not None:
            self.access_type = access_type
        if active_only is not None:
            self.active_only = active_only
        if evaluation_ids is not None:
            self.evaluation_ids = evaluation_ids
        if results is not None:
            self.results = results
        if total_number_of_results is not None:
            self.total_number_of_results = total_number_of_results

    @property
    def access_type(self):
        """Gets the access_type of this PaginatedResultsOfEvaluationAllOf.  # noqa: E501

        The type of access for the user to filter for, optional and defaults to ACCESS_TYPE.READ  # noqa: E501

        :return: The access_type of this PaginatedResultsOfEvaluationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        """Sets the access_type of this PaginatedResultsOfEvaluationAllOf.

        The type of access for the user to filter for, optional and defaults to ACCESS_TYPE.READ  # noqa: E501

        :param access_type: The access_type of this PaginatedResultsOfEvaluationAllOf.  # noqa: E501
        :type: str
        """

        self._access_type = access_type

    @property
    def active_only(self):
        """Gets the active_only of this PaginatedResultsOfEvaluationAllOf.  # noqa: E501

        If 'true' then return only those evaluations with rounds defined and for which the current time is in one of the rounds.   # noqa: E501

        :return: The active_only of this PaginatedResultsOfEvaluationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._active_only

    @active_only.setter
    def active_only(self, active_only):
        """Sets the active_only of this PaginatedResultsOfEvaluationAllOf.

        If 'true' then return only those evaluations with rounds defined and for which the current time is in one of the rounds.   # noqa: E501

        :param active_only: The active_only of this PaginatedResultsOfEvaluationAllOf.  # noqa: E501
        :type: str
        """

        self._active_only = active_only

    @property
    def evaluation_ids(self):
        """Gets the evaluation_ids of this PaginatedResultsOfEvaluationAllOf.  # noqa: E501

        an optional, comma-delimited list of evaluation IDs to which the response is limited  # noqa: E501

        :return: The evaluation_ids of this PaginatedResultsOfEvaluationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._evaluation_ids

    @evaluation_ids.setter
    def evaluation_ids(self, evaluation_ids):
        """Sets the evaluation_ids of this PaginatedResultsOfEvaluationAllOf.

        an optional, comma-delimited list of evaluation IDs to which the response is limited  # noqa: E501

        :param evaluation_ids: The evaluation_ids of this PaginatedResultsOfEvaluationAllOf.  # noqa: E501
        :type: str
        """

        self._evaluation_ids = evaluation_ids

    @property
    def results(self):
        """Gets the results of this PaginatedResultsOfEvaluationAllOf.  # noqa: E501

        List of evaluations  # noqa: E501

        :return: The results of this PaginatedResultsOfEvaluationAllOf.  # noqa: E501
        :rtype: list[Evaluation]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this PaginatedResultsOfEvaluationAllOf.

        List of evaluations  # noqa: E501

        :param results: The results of this PaginatedResultsOfEvaluationAllOf.  # noqa: E501
        :type: list[Evaluation]
        """

        self._results = results

    @property
    def total_number_of_results(self):
        """Gets the total_number_of_results of this PaginatedResultsOfEvaluationAllOf.  # noqa: E501

        Number of results per page  # noqa: E501

        :return: The total_number_of_results of this PaginatedResultsOfEvaluationAllOf.  # noqa: E501
        :rtype: int
        """
        return self._total_number_of_results

    @total_number_of_results.setter
    def total_number_of_results(self, total_number_of_results):
        """Sets the total_number_of_results of this PaginatedResultsOfEvaluationAllOf.

        Number of results per page  # noqa: E501

        :param total_number_of_results: The total_number_of_results of this PaginatedResultsOfEvaluationAllOf.  # noqa: E501
        :type: int
        """

        self._total_number_of_results = total_number_of_results

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
        if not isinstance(other, PaginatedResultsOfEvaluationAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaginatedResultsOfEvaluationAllOf):
            return True

        return self.to_dict() != other.to_dict()
