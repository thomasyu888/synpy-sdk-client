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


class Activity(object):
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
        'description': 'str',
        'etag': 'str',
        'id': 'str',
        'modified_by': 'str',
        'modified_on': 'str',
        'name': 'str',
        'used': 'list[Used]'
    }

    attribute_map = {
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'description': 'description',
        'etag': 'etag',
        'id': 'id',
        'modified_by': 'modifiedBy',
        'modified_on': 'modifiedOn',
        'name': 'name',
        'used': 'used'
    }

    def __init__(self, created_by=None, created_on=None, description=None, etag=None, id=None, modified_by=None, modified_on=None, name=None, used=None, local_vars_configuration=None):  # noqa: E501
        """Activity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_by = None
        self._created_on = None
        self._description = None
        self._etag = None
        self._id = None
        self._modified_by = None
        self._modified_on = None
        self._name = None
        self._used = None
        self.discriminator = None

        if created_by is not None:
            self.created_by = created_by
        if created_on is not None:
            self.created_on = created_on
        if description is not None:
            self.description = description
        if etag is not None:
            self.etag = etag
        if id is not None:
            self.id = id
        if modified_by is not None:
            self.modified_by = modified_by
        if modified_on is not None:
            self.modified_on = modified_on
        if name is not None:
            self.name = name
        if used is not None:
            self.used = used

    @property
    def created_by(self):
        """Gets the created_by of this Activity.  # noqa: E501

        The user that created this object.  # noqa: E501

        :return: The created_by of this Activity.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Activity.

        The user that created this object.  # noqa: E501

        :param created_by: The created_by of this Activity.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this Activity.  # noqa: E501

        The date this object was created.  # noqa: E501

        :return: The created_on of this Activity.  # noqa: E501
        :rtype: str
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Activity.

        The date this object was created.  # noqa: E501

        :param created_on: The created_on of this Activity.  # noqa: E501
        :type: str
        """

        self._created_on = created_on

    @property
    def description(self):
        """Gets the description of this Activity.  # noqa: E501

        A description of this Activity.  # noqa: E501

        :return: The description of this Activity.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Activity.

        A description of this Activity.  # noqa: E501

        :param description: The description of this Activity.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def etag(self):
        """Gets the etag of this Activity.  # noqa: E501

        Synapse employs an Optimistic Concurrency Control (OCC) scheme to handle concurrent updates. Since the E-Tag changes every time an entity is updated it is used to detect when a client's current representation of an entity is out-of-date.   # noqa: E501

        :return: The etag of this Activity.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this Activity.

        Synapse employs an Optimistic Concurrency Control (OCC) scheme to handle concurrent updates. Since the E-Tag changes every time an entity is updated it is used to detect when a client's current representation of an entity is out-of-date.   # noqa: E501

        :param etag: The etag of this Activity.  # noqa: E501
        :type: str
        """

        self._etag = etag

    @property
    def id(self):
        """Gets the id of this Activity.  # noqa: E501

        The unique immutable ID  # noqa: E501

        :return: The id of this Activity.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Activity.

        The unique immutable ID  # noqa: E501

        :param id: The id of this Activity.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def modified_by(self):
        """Gets the modified_by of this Activity.  # noqa: E501

        The user that last modified this object.  # noqa: E501

        :return: The modified_by of this Activity.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this Activity.

        The user that last modified this object.  # noqa: E501

        :param modified_by: The modified_by of this Activity.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def modified_on(self):
        """Gets the modified_on of this Activity.  # noqa: E501

        The date this object was last modified.  # noqa: E501

        :return: The modified_on of this Activity.  # noqa: E501
        :rtype: str
        """
        return self._modified_on

    @modified_on.setter
    def modified_on(self, modified_on):
        """Sets the modified_on of this Activity.

        The date this object was last modified.  # noqa: E501

        :param modified_on: The modified_on of this Activity.  # noqa: E501
        :type: str
        """

        self._modified_on = modified_on

    @property
    def name(self):
        """Gets the name of this Activity.  # noqa: E501

        A name for this Activity.  # noqa: E501

        :return: The name of this Activity.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Activity.

        A name for this Activity.  # noqa: E501

        :param name: The name of this Activity.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def used(self):
        """Gets the used of this Activity.  # noqa: E501

        The entities used by this Activity.  # noqa: E501

        :return: The used of this Activity.  # noqa: E501
        :rtype: list[Used]
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this Activity.

        The entities used by this Activity.  # noqa: E501

        :param used: The used of this Activity.  # noqa: E501
        :type: list[Used]
        """

        self._used = used

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
        if not isinstance(other, Activity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Activity):
            return True

        return self.to_dict() != other.to_dict()