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


class JsonSchemaVersionInfo(object):
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
        'id': 'str',
        'created_by': 'str',
        'created_on': 'str',
        'json_sha256_hex': 'str',
        'organization_id': 'str',
        'organization_name': 'str',
        'schema_id': 'str',
        'schema_name': 'str',
        'semantic_version': 'str',
        'version_id': 'str'
    }

    attribute_map = {
        'id': '$id',
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'json_sha256_hex': 'jsonSHA256Hex',
        'organization_id': 'organizationId',
        'organization_name': 'organizationName',
        'schema_id': 'schemaId',
        'schema_name': 'schemaName',
        'semantic_version': 'semanticVersion',
        'version_id': 'versionId'
    }

    def __init__(self, id=None, created_by=None, created_on=None, json_sha256_hex=None, organization_id=None, organization_name=None, schema_id=None, schema_name=None, semantic_version=None, version_id=None, local_vars_configuration=None):  # noqa: E501
        """JsonSchemaVersionInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_by = None
        self._created_on = None
        self._json_sha256_hex = None
        self._organization_id = None
        self._organization_name = None
        self._schema_id = None
        self._schema_name = None
        self._semantic_version = None
        self._version_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_by is not None:
            self.created_by = created_by
        if created_on is not None:
            self.created_on = created_on
        if json_sha256_hex is not None:
            self.json_sha256_hex = json_sha256_hex
        if organization_id is not None:
            self.organization_id = organization_id
        if organization_name is not None:
            self.organization_name = organization_name
        if schema_id is not None:
            self.schema_id = schema_id
        if schema_name is not None:
            self.schema_name = schema_name
        if semantic_version is not None:
            self.semantic_version = semantic_version
        if version_id is not None:
            self.version_id = version_id

    @property
    def id(self):
        """Gets the id of this JsonSchemaVersionInfo.  # noqa: E501

        The full '$id' of this schema version   # noqa: E501

        :return: The id of this JsonSchemaVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JsonSchemaVersionInfo.

        The full '$id' of this schema version   # noqa: E501

        :param id: The id of this JsonSchemaVersionInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this JsonSchemaVersionInfo.  # noqa: E501

        The ID of the user that created this JSON schema version.  # noqa: E501

        :return: The created_by of this JsonSchemaVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this JsonSchemaVersionInfo.

        The ID of the user that created this JSON schema version.  # noqa: E501

        :param created_by: The created_by of this JsonSchemaVersionInfo.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this JsonSchemaVersionInfo.  # noqa: E501

        The date this JSON schema version was created.  # noqa: E501

        :return: The created_on of this JsonSchemaVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this JsonSchemaVersionInfo.

        The date this JSON schema version was created.  # noqa: E501

        :param created_on: The created_on of this JsonSchemaVersionInfo.  # noqa: E501
        :type: str
        """

        self._created_on = created_on

    @property
    def json_sha256_hex(self):
        """Gets the json_sha256_hex of this JsonSchemaVersionInfo.  # noqa: E501

        The SHA-256 hexadecimal hash of the UTF-8 encoded JSON schema.  # noqa: E501

        :return: The json_sha256_hex of this JsonSchemaVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._json_sha256_hex

    @json_sha256_hex.setter
    def json_sha256_hex(self, json_sha256_hex):
        """Sets the json_sha256_hex of this JsonSchemaVersionInfo.

        The SHA-256 hexadecimal hash of the UTF-8 encoded JSON schema.  # noqa: E501

        :param json_sha256_hex: The json_sha256_hex of this JsonSchemaVersionInfo.  # noqa: E501
        :type: str
        """

        self._json_sha256_hex = json_sha256_hex

    @property
    def organization_id(self):
        """Gets the organization_id of this JsonSchemaVersionInfo.  # noqa: E501

        The Synapse issued numeric identifier for the organization.  # noqa: E501

        :return: The organization_id of this JsonSchemaVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this JsonSchemaVersionInfo.

        The Synapse issued numeric identifier for the organization.  # noqa: E501

        :param organization_id: The organization_id of this JsonSchemaVersionInfo.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def organization_name(self):
        """Gets the organization_name of this JsonSchemaVersionInfo.  # noqa: E501

        The name of the organization to which this schema belongs.  # noqa: E501

        :return: The organization_name of this JsonSchemaVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._organization_name

    @organization_name.setter
    def organization_name(self, organization_name):
        """Sets the organization_name of this JsonSchemaVersionInfo.

        The name of the organization to which this schema belongs.  # noqa: E501

        :param organization_name: The organization_name of this JsonSchemaVersionInfo.  # noqa: E501
        :type: str
        """

        self._organization_name = organization_name

    @property
    def schema_id(self):
        """Gets the schema_id of this JsonSchemaVersionInfo.  # noqa: E501

        The Synapse issued numeric identifier for the schema.  # noqa: E501

        :return: The schema_id of this JsonSchemaVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._schema_id

    @schema_id.setter
    def schema_id(self, schema_id):
        """Sets the schema_id of this JsonSchemaVersionInfo.

        The Synapse issued numeric identifier for the schema.  # noqa: E501

        :param schema_id: The schema_id of this JsonSchemaVersionInfo.  # noqa: E501
        :type: str
        """

        self._schema_id = schema_id

    @property
    def schema_name(self):
        """Gets the schema_name of this JsonSchemaVersionInfo.  # noqa: E501

        The name of the this schema.  # noqa: E501

        :return: The schema_name of this JsonSchemaVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this JsonSchemaVersionInfo.

        The name of the this schema.  # noqa: E501

        :param schema_name: The schema_name of this JsonSchemaVersionInfo.  # noqa: E501
        :type: str
        """

        self._schema_name = schema_name

    @property
    def semantic_version(self):
        """Gets the semantic_version of this JsonSchemaVersionInfo.  # noqa: E501

        The semantic version label provided when this version was created. Can be null if a semantic version was not provided when this version was created.   # noqa: E501

        :return: The semantic_version of this JsonSchemaVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._semantic_version

    @semantic_version.setter
    def semantic_version(self, semantic_version):
        """Sets the semantic_version of this JsonSchemaVersionInfo.

        The semantic version label provided when this version was created. Can be null if a semantic version was not provided when this version was created.   # noqa: E501

        :param semantic_version: The semantic_version of this JsonSchemaVersionInfo.  # noqa: E501
        :type: str
        """

        self._semantic_version = semantic_version

    @property
    def version_id(self):
        """Gets the version_id of this JsonSchemaVersionInfo.  # noqa: E501

        The Synapse issued numeric identifier for this version.  # noqa: E501

        :return: The version_id of this JsonSchemaVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this JsonSchemaVersionInfo.

        The Synapse issued numeric identifier for this version.  # noqa: E501

        :param version_id: The version_id of this JsonSchemaVersionInfo.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

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
        if not isinstance(other, JsonSchemaVersionInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JsonSchemaVersionInfo):
            return True

        return self.to_dict() != other.to_dict()