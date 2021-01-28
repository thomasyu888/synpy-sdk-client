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


class AnnotationsAnnotation(object):
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
        'double_annos': 'list[DoubleAnnotation]',
        'long_annos': 'list[LongAnnotation]',
        'object_id': 'str',
        'scope_id': 'str',
        'string_annos': 'list[StringAnnotation]',
        'version': 'int'
    }

    attribute_map = {
        'double_annos': 'doubleAnnos',
        'long_annos': 'longAnnos',
        'object_id': 'objectId',
        'scope_id': 'scopeId',
        'string_annos': 'stringAnnos',
        'version': 'version'
    }

    def __init__(self, double_annos=None, long_annos=None, object_id=None, scope_id=None, string_annos=None, version=None, local_vars_configuration=None):  # noqa: E501
        """AnnotationsAnnotation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._double_annos = None
        self._long_annos = None
        self._object_id = None
        self._scope_id = None
        self._string_annos = None
        self._version = None
        self.discriminator = None

        if double_annos is not None:
            self.double_annos = double_annos
        if long_annos is not None:
            self.long_annos = long_annos
        if object_id is not None:
            self.object_id = object_id
        if scope_id is not None:
            self.scope_id = scope_id
        if string_annos is not None:
            self.string_annos = string_annos
        if version is not None:
            self.version = version

    @property
    def double_annos(self):
        """Gets the double_annos of this AnnotationsAnnotation.  # noqa: E501

        A list of DoubleAnnnotations  # noqa: E501

        :return: The double_annos of this AnnotationsAnnotation.  # noqa: E501
        :rtype: list[DoubleAnnotation]
        """
        return self._double_annos

    @double_annos.setter
    def double_annos(self, double_annos):
        """Sets the double_annos of this AnnotationsAnnotation.

        A list of DoubleAnnnotations  # noqa: E501

        :param double_annos: The double_annos of this AnnotationsAnnotation.  # noqa: E501
        :type: list[DoubleAnnotation]
        """

        self._double_annos = double_annos

    @property
    def long_annos(self):
        """Gets the long_annos of this AnnotationsAnnotation.  # noqa: E501

        A list of LongAnnnotations  # noqa: E501

        :return: The long_annos of this AnnotationsAnnotation.  # noqa: E501
        :rtype: list[LongAnnotation]
        """
        return self._long_annos

    @long_annos.setter
    def long_annos(self, long_annos):
        """Sets the long_annos of this AnnotationsAnnotation.

        A list of LongAnnnotations  # noqa: E501

        :param long_annos: The long_annos of this AnnotationsAnnotation.  # noqa: E501
        :type: list[LongAnnotation]
        """

        self._long_annos = long_annos

    @property
    def object_id(self):
        """Gets the object_id of this AnnotationsAnnotation.  # noqa: E501

        The Synapse ID of the object with which these Annotations are associated  # noqa: E501

        :return: The object_id of this AnnotationsAnnotation.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this AnnotationsAnnotation.

        The Synapse ID of the object with which these Annotations are associated  # noqa: E501

        :param object_id: The object_id of this AnnotationsAnnotation.  # noqa: E501
        :type: str
        """

        self._object_id = object_id

    @property
    def scope_id(self):
        """Gets the scope_id of this AnnotationsAnnotation.  # noqa: E501

        The Synapse ID of the umbrella object above the object with which these Annotations are associated  # noqa: E501

        :return: The scope_id of this AnnotationsAnnotation.  # noqa: E501
        :rtype: str
        """
        return self._scope_id

    @scope_id.setter
    def scope_id(self, scope_id):
        """Sets the scope_id of this AnnotationsAnnotation.

        The Synapse ID of the umbrella object above the object with which these Annotations are associated  # noqa: E501

        :param scope_id: The scope_id of this AnnotationsAnnotation.  # noqa: E501
        :type: str
        """

        self._scope_id = scope_id

    @property
    def string_annos(self):
        """Gets the string_annos of this AnnotationsAnnotation.  # noqa: E501

        A list of StringAnnnotations  # noqa: E501

        :return: The string_annos of this AnnotationsAnnotation.  # noqa: E501
        :rtype: list[StringAnnotation]
        """
        return self._string_annos

    @string_annos.setter
    def string_annos(self, string_annos):
        """Sets the string_annos of this AnnotationsAnnotation.

        A list of StringAnnnotations  # noqa: E501

        :param string_annos: The string_annos of this AnnotationsAnnotation.  # noqa: E501
        :type: list[StringAnnotation]
        """

        self._string_annos = string_annos

    @property
    def version(self):
        """Gets the version of this AnnotationsAnnotation.  # noqa: E501

        The system controlled version of this collection of annotations  # noqa: E501

        :return: The version of this AnnotationsAnnotation.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AnnotationsAnnotation.

        The system controlled version of this collection of annotations  # noqa: E501

        :param version: The version of this AnnotationsAnnotation.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if not isinstance(other, AnnotationsAnnotation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AnnotationsAnnotation):
            return True

        return self.to_dict() != other.to_dict()
