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


class CreateDiscussionThread(object):
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
        'forum_id': 'str',
        'message_markdown': 'str',
        'title': 'str'
    }

    attribute_map = {
        'forum_id': 'forumId',
        'message_markdown': 'messageMarkdown',
        'title': 'title'
    }

    def __init__(self, forum_id=None, message_markdown=None, title=None, local_vars_configuration=None):  # noqa: E501
        """CreateDiscussionThread - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._forum_id = None
        self._message_markdown = None
        self._title = None
        self.discriminator = None

        if forum_id is not None:
            self.forum_id = forum_id
        if message_markdown is not None:
            self.message_markdown = message_markdown
        if title is not None:
            self.title = title

    @property
    def forum_id(self):
        """Gets the forum_id of this CreateDiscussionThread.  # noqa: E501

        The ID of the forum this CreateThread belongs to  # noqa: E501

        :return: The forum_id of this CreateDiscussionThread.  # noqa: E501
        :rtype: str
        """
        return self._forum_id

    @forum_id.setter
    def forum_id(self, forum_id):
        """Sets the forum_id of this CreateDiscussionThread.

        The ID of the forum this CreateThread belongs to  # noqa: E501

        :param forum_id: The forum_id of this CreateDiscussionThread.  # noqa: E501
        :type: str
        """

        self._forum_id = forum_id

    @property
    def message_markdown(self):
        """Gets the message_markdown of this CreateDiscussionThread.  # noqa: E501

        The markdown of the Thread's message   # noqa: E501

        :return: The message_markdown of this CreateDiscussionThread.  # noqa: E501
        :rtype: str
        """
        return self._message_markdown

    @message_markdown.setter
    def message_markdown(self, message_markdown):
        """Sets the message_markdown of this CreateDiscussionThread.

        The markdown of the Thread's message   # noqa: E501

        :param message_markdown: The message_markdown of this CreateDiscussionThread.  # noqa: E501
        :type: str
        """

        self._message_markdown = message_markdown

    @property
    def title(self):
        """Gets the title of this CreateDiscussionThread.  # noqa: E501

        The title of the Thread  # noqa: E501

        :return: The title of this CreateDiscussionThread.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CreateDiscussionThread.

        The title of the Thread  # noqa: E501

        :param title: The title of this CreateDiscussionThread.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if not isinstance(other, CreateDiscussionThread):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDiscussionThread):
            return True

        return self.to_dict() != other.to_dict()