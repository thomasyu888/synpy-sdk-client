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


class ListResponse(object):
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
        'next_page_token': 'str',
        'page': 'list[FormData]'
    }

    attribute_map = {
        'next_page_token': 'nextPageToken',
        'page': 'page'
    }

    def __init__(self, next_page_token=None, page=None, local_vars_configuration=None):  # noqa: E501
        """ListResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._next_page_token = None
        self._page = None
        self.discriminator = None

        if next_page_token is not None:
            self.next_page_token = next_page_token
        if page is not None:
            self.page = page

    @property
    def next_page_token(self):
        """Gets the next_page_token of this ListResponse.  # noqa: E501

        The results are automatically paginated. If another page of results exists then a nextPageToken will be provided. Forward the provided nextPageTokens in a subsequent list request to get the next page.   # noqa: E501

        :return: The next_page_token of this ListResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this ListResponse.

        The results are automatically paginated. If another page of results exists then a nextPageToken will be provided. Forward the provided nextPageTokens in a subsequent list request to get the next page.   # noqa: E501

        :param next_page_token: The next_page_token of this ListResponse.  # noqa: E501
        :type: str
        """

        self._next_page_token = next_page_token

    @property
    def page(self):
        """Gets the page of this ListResponse.  # noqa: E501

        A single page of results matching the request.  # noqa: E501

        :return: The page of this ListResponse.  # noqa: E501
        :rtype: list[FormData]
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListResponse.

        A single page of results matching the request.  # noqa: E501

        :param page: The page of this ListResponse.  # noqa: E501
        :type: list[FormData]
        """

        self._page = page

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
        if not isinstance(other, ListResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListResponse):
            return True

        return self.to_dict() != other.to_dict()
