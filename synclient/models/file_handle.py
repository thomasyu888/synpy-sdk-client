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


class FileHandle(object):
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
        'concrete_type': 'str',
        'content_md5': 'str',
        'content_size': 'int',
        'content_type': 'str',
        'created_by': 'str',
        'created_on': 'str',
        'etag': 'str',
        'file_name': 'str',
        'id': 'str',
        'storage_location_id': 'int'
    }

    attribute_map = {
        'concrete_type': 'concreteType',
        'content_md5': 'contentMd5',
        'content_size': 'contentSize',
        'content_type': 'contentType',
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'etag': 'etag',
        'file_name': 'fileName',
        'id': 'id',
        'storage_location_id': 'storageLocationId'
    }

    def __init__(self, concrete_type=None, content_md5=None, content_size=None, content_type=None, created_by=None, created_on=None, etag=None, file_name=None, id=None, storage_location_id=None, local_vars_configuration=None):  # noqa: E501
        """FileHandle - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._concrete_type = None
        self._content_md5 = None
        self._content_size = None
        self._content_type = None
        self._created_by = None
        self._created_on = None
        self._etag = None
        self._file_name = None
        self._id = None
        self._storage_location_id = None
        self.discriminator = None

        if concrete_type is not None:
            self.concrete_type = concrete_type
        if content_md5 is not None:
            self.content_md5 = content_md5
        if content_size is not None:
            self.content_size = content_size
        if content_type is not None:
            self.content_type = content_type
        if created_by is not None:
            self.created_by = created_by
        if created_on is not None:
            self.created_on = created_on
        if etag is not None:
            self.etag = etag
        if file_name is not None:
            self.file_name = file_name
        if id is not None:
            self.id = id
        if storage_location_id is not None:
            self.storage_location_id = storage_location_id

    @property
    def concrete_type(self):
        """Gets the concrete_type of this FileHandle.  # noqa: E501

        This is used to indicate the implementation of this interface. For example, an S3FileHandle should be set to: org.sagebionetworks.repo.model.file.S3FileHandle   # noqa: E501

        :return: The concrete_type of this FileHandle.  # noqa: E501
        :rtype: str
        """
        return self._concrete_type

    @concrete_type.setter
    def concrete_type(self, concrete_type):
        """Sets the concrete_type of this FileHandle.

        This is used to indicate the implementation of this interface. For example, an S3FileHandle should be set to: org.sagebionetworks.repo.model.file.S3FileHandle   # noqa: E501

        :param concrete_type: The concrete_type of this FileHandle.  # noqa: E501
        :type: str
        """

        self._concrete_type = concrete_type

    @property
    def content_md5(self):
        """Gets the content_md5 of this FileHandle.  # noqa: E501

        The file's content MD5.   # noqa: E501

        :return: The content_md5 of this FileHandle.  # noqa: E501
        :rtype: str
        """
        return self._content_md5

    @content_md5.setter
    def content_md5(self, content_md5):
        """Sets the content_md5 of this FileHandle.

        The file's content MD5.   # noqa: E501

        :param content_md5: The content_md5 of this FileHandle.  # noqa: E501
        :type: str
        """

        self._content_md5 = content_md5

    @property
    def content_size(self):
        """Gets the content_size of this FileHandle.  # noqa: E501

        The size of the file in bytes.  # noqa: E501

        :return: The content_size of this FileHandle.  # noqa: E501
        :rtype: int
        """
        return self._content_size

    @content_size.setter
    def content_size(self, content_size):
        """Sets the content_size of this FileHandle.

        The size of the file in bytes.  # noqa: E501

        :param content_size: The content_size of this FileHandle.  # noqa: E501
        :type: int
        """

        self._content_size = content_size

    @property
    def content_type(self):
        """Gets the content_type of this FileHandle.  # noqa: E501

        Must be: http://en.wikipedia.org/wiki/Internet_media_type   # noqa: E501

        :return: The content_type of this FileHandle.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this FileHandle.

        Must be: http://en.wikipedia.org/wiki/Internet_media_type   # noqa: E501

        :param content_type: The content_type of this FileHandle.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def created_by(self):
        """Gets the created_by of this FileHandle.  # noqa: E501

        The ID Of the user that created this file.  # noqa: E501

        :return: The created_by of this FileHandle.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this FileHandle.

        The ID Of the user that created this file.  # noqa: E501

        :param created_by: The created_by of this FileHandle.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this FileHandle.  # noqa: E501

        The date when this file was uploaded.  # noqa: E501

        :return: The created_on of this FileHandle.  # noqa: E501
        :rtype: str
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this FileHandle.

        The date when this file was uploaded.  # noqa: E501

        :param created_on: The created_on of this FileHandle.  # noqa: E501
        :type: str
        """

        self._created_on = created_on

    @property
    def etag(self):
        """Gets the etag of this FileHandle.  # noqa: E501

        Synapse employs an Optimistic Concurrency Control (OCC) scheme to handle concurrent updates. Since the E-Tag changes every time an entity is updated it is used to detect when a client's current representation of an entity is out-of-date.   # noqa: E501

        :return: The etag of this FileHandle.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this FileHandle.

        Synapse employs an Optimistic Concurrency Control (OCC) scheme to handle concurrent updates. Since the E-Tag changes every time an entity is updated it is used to detect when a client's current representation of an entity is out-of-date.   # noqa: E501

        :param etag: The etag of this FileHandle.  # noqa: E501
        :type: str
        """

        self._etag = etag

    @property
    def file_name(self):
        """Gets the file_name of this FileHandle.  # noqa: E501

        The short, user visible name for this file.  # noqa: E501

        :return: The file_name of this FileHandle.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this FileHandle.

        The short, user visible name for this file.  # noqa: E501

        :param file_name: The file_name of this FileHandle.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def id(self):
        """Gets the id of this FileHandle.  # noqa: E501

        The ID of this FileHandle. All references to this FileHandle will use this ID. Synapse will generate this ID when the FileHandle is created.   # noqa: E501

        :return: The id of this FileHandle.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FileHandle.

        The ID of this FileHandle. All references to this FileHandle will use this ID. Synapse will generate this ID when the FileHandle is created.   # noqa: E501

        :param id: The id of this FileHandle.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def storage_location_id(self):
        """Gets the storage_location_id of this FileHandle.  # noqa: E501

        The optional storage location descriptor  # noqa: E501

        :return: The storage_location_id of this FileHandle.  # noqa: E501
        :rtype: int
        """
        return self._storage_location_id

    @storage_location_id.setter
    def storage_location_id(self, storage_location_id):
        """Sets the storage_location_id of this FileHandle.

        The optional storage location descriptor  # noqa: E501

        :param storage_location_id: The storage_location_id of this FileHandle.  # noqa: E501
        :type: int
        """

        self._storage_location_id = storage_location_id

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
        if not isinstance(other, FileHandle):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileHandle):
            return True

        return self.to_dict() != other.to_dict()