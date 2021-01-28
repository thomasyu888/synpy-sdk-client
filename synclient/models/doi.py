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


class Doi(object):
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
        'associated_by': 'str',
        'associated_on': 'str',
        'association_id': 'str',
        'doi_uri': 'str',
        'doi_url': 'str',
        'etag': 'str',
        'object_id': 'str',
        'object_type': 'ObjectType',
        'object_version': 'int',
        'updated_by': 'str',
        'updated_on': 'str',
        'creators': 'list[DoiCreator]',
        'publication_year': 'int',
        'resource_type': 'DoiResourceType',
        'titles': 'list[DoiTitle]'
    }

    attribute_map = {
        'associated_by': 'associatedBy',
        'associated_on': 'associatedOn',
        'association_id': 'associationId',
        'doi_uri': 'doiUri',
        'doi_url': 'doiUrl',
        'etag': 'etag',
        'object_id': 'objectId',
        'object_type': 'objectType',
        'object_version': 'objectVersion',
        'updated_by': 'updatedBy',
        'updated_on': 'updatedOn',
        'creators': 'creators',
        'publication_year': 'publicationYear',
        'resource_type': 'resourceType',
        'titles': 'titles'
    }

    def __init__(self, associated_by=None, associated_on=None, association_id=None, doi_uri=None, doi_url=None, etag=None, object_id=None, object_type=None, object_version=None, updated_by=None, updated_on=None, creators=None, publication_year=None, resource_type=None, titles=None, local_vars_configuration=None):  # noqa: E501
        """Doi - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._associated_by = None
        self._associated_on = None
        self._association_id = None
        self._doi_uri = None
        self._doi_url = None
        self._etag = None
        self._object_id = None
        self._object_type = None
        self._object_version = None
        self._updated_by = None
        self._updated_on = None
        self._creators = None
        self._publication_year = None
        self._resource_type = None
        self._titles = None
        self.discriminator = None

        if associated_by is not None:
            self.associated_by = associated_by
        if associated_on is not None:
            self.associated_on = associated_on
        if association_id is not None:
            self.association_id = association_id
        if doi_uri is not None:
            self.doi_uri = doi_uri
        if doi_url is not None:
            self.doi_url = doi_url
        if etag is not None:
            self.etag = etag
        self.object_id = object_id
        if object_type is not None:
            self.object_type = object_type
        if object_version is not None:
            self.object_version = object_version
        if updated_by is not None:
            self.updated_by = updated_by
        if updated_on is not None:
            self.updated_on = updated_on
        self.creators = creators
        self.publication_year = publication_year
        if resource_type is not None:
            self.resource_type = resource_type
        self.titles = titles

    @property
    def associated_by(self):
        """Gets the associated_by of this Doi.  # noqa: E501

        The ID of the user that creates this DOI. Provided by Synapse.  # noqa: E501

        :return: The associated_by of this Doi.  # noqa: E501
        :rtype: str
        """
        return self._associated_by

    @associated_by.setter
    def associated_by(self, associated_by):
        """Sets the associated_by of this Doi.

        The ID of the user that creates this DOI. Provided by Synapse.  # noqa: E501

        :param associated_by: The associated_by of this Doi.  # noqa: E501
        :type: str
        """

        self._associated_by = associated_by

    @property
    def associated_on(self):
        """Gets the associated_on of this Doi.  # noqa: E501

        The date time this DOI is first created. Provided by Synapse.  # noqa: E501

        :return: The associated_on of this Doi.  # noqa: E501
        :rtype: str
        """
        return self._associated_on

    @associated_on.setter
    def associated_on(self, associated_on):
        """Sets the associated_on of this Doi.

        The date time this DOI is first created. Provided by Synapse.  # noqa: E501

        :param associated_on: The associated_on of this Doi.  # noqa: E501
        :type: str
        """

        self._associated_on = associated_on

    @property
    def association_id(self):
        """Gets the association_id of this Doi.  # noqa: E501

        The unique ID of this DOI stored in Synapse. Provided by Synapse.  # noqa: E501

        :return: The association_id of this Doi.  # noqa: E501
        :rtype: str
        """
        return self._association_id

    @association_id.setter
    def association_id(self, association_id):
        """Sets the association_id of this Doi.

        The unique ID of this DOI stored in Synapse. Provided by Synapse.  # noqa: E501

        :param association_id: The association_id of this Doi.  # noqa: E501
        :type: str
        """

        self._association_id = association_id

    @property
    def doi_uri(self):
        """Gets the doi_uri of this Doi.  # noqa: E501

        The unique URI of this DOI to which the resource can be resolved. Provided by Synapse.  # noqa: E501

        :return: The doi_uri of this Doi.  # noqa: E501
        :rtype: str
        """
        return self._doi_uri

    @doi_uri.setter
    def doi_uri(self, doi_uri):
        """Sets the doi_uri of this Doi.

        The unique URI of this DOI to which the resource can be resolved. Provided by Synapse.  # noqa: E501

        :param doi_uri: The doi_uri of this Doi.  # noqa: E501
        :type: str
        """

        self._doi_uri = doi_uri

    @property
    def doi_url(self):
        """Gets the doi_url of this Doi.  # noqa: E501

        The DOI URL that will point to the Synapse object. Provided by Synapse.  # noqa: E501

        :return: The doi_url of this Doi.  # noqa: E501
        :rtype: str
        """
        return self._doi_url

    @doi_url.setter
    def doi_url(self, doi_url):
        """Sets the doi_url of this Doi.

        The DOI URL that will point to the Synapse object. Provided by Synapse.  # noqa: E501

        :param doi_url: The doi_url of this Doi.  # noqa: E501
        :type: str
        """

        self._doi_url = doi_url

    @property
    def etag(self):
        """Gets the etag of this Doi.  # noqa: E501

        For Optimistic Concurrency Control (OCC). Required to successfully update a DOI.  # noqa: E501

        :return: The etag of this Doi.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this Doi.

        For Optimistic Concurrency Control (OCC). Required to successfully update a DOI.  # noqa: E501

        :param etag: The etag of this Doi.  # noqa: E501
        :type: str
        """

        self._etag = etag

    @property
    def object_id(self):
        """Gets the object_id of this Doi.  # noqa: E501

        The ID of the digital object in Synapse for which this DOI is created.  # noqa: E501

        :return: The object_id of this Doi.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this Doi.

        The ID of the digital object in Synapse for which this DOI is created.  # noqa: E501

        :param object_id: The object_id of this Doi.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and object_id is None:  # noqa: E501
            raise ValueError("Invalid value for `object_id`, must not be `None`")  # noqa: E501

        self._object_id = object_id

    @property
    def object_type(self):
        """Gets the object_type of this Doi.  # noqa: E501


        :return: The object_type of this Doi.  # noqa: E501
        :rtype: ObjectType
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this Doi.


        :param object_type: The object_type of this Doi.  # noqa: E501
        :type: ObjectType
        """

        self._object_type = object_type

    @property
    def object_version(self):
        """Gets the object_version of this Doi.  # noqa: E501

        The version of the digital object. When null, the DOI is associated with the current version of the object.  # noqa: E501

        :return: The object_version of this Doi.  # noqa: E501
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """Sets the object_version of this Doi.

        The version of the digital object. When null, the DOI is associated with the current version of the object.  # noqa: E501

        :param object_version: The object_version of this Doi.  # noqa: E501
        :type: int
        """

        self._object_version = object_version

    @property
    def updated_by(self):
        """Gets the updated_by of this Doi.  # noqa: E501

        The ID of the user that last updated this DOI. Provided by Synapse.  # noqa: E501

        :return: The updated_by of this Doi.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this Doi.

        The ID of the user that last updated this DOI. Provided by Synapse.  # noqa: E501

        :param updated_by: The updated_by of this Doi.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def updated_on(self):
        """Gets the updated_on of this Doi.  # noqa: E501

        The date time this DOI is last updated. Provided by Synapse.  # noqa: E501

        :return: The updated_on of this Doi.  # noqa: E501
        :rtype: str
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this Doi.

        The date time this DOI is last updated. Provided by Synapse.  # noqa: E501

        :param updated_on: The updated_on of this Doi.  # noqa: E501
        :type: str
        """

        self._updated_on = updated_on

    @property
    def creators(self):
        """Gets the creators of this Doi.  # noqa: E501

        The main researchers involved in producing the data, or the authors of the publication, in priority order.   # noqa: E501

        :return: The creators of this Doi.  # noqa: E501
        :rtype: list[DoiCreator]
        """
        return self._creators

    @creators.setter
    def creators(self, creators):
        """Sets the creators of this Doi.

        The main researchers involved in producing the data, or the authors of the publication, in priority order.   # noqa: E501

        :param creators: The creators of this Doi.  # noqa: E501
        :type: list[DoiCreator]
        """
        if self.local_vars_configuration.client_side_validation and creators is None:  # noqa: E501
            raise ValueError("Invalid value for `creators`, must not be `None`")  # noqa: E501

        self._creators = creators

    @property
    def publication_year(self):
        """Gets the publication_year of this Doi.  # noqa: E501

        The year that this resource became publicly accessible. Must be in YYYY format.  # noqa: E501

        :return: The publication_year of this Doi.  # noqa: E501
        :rtype: int
        """
        return self._publication_year

    @publication_year.setter
    def publication_year(self, publication_year):
        """Sets the publication_year of this Doi.

        The year that this resource became publicly accessible. Must be in YYYY format.  # noqa: E501

        :param publication_year: The publication_year of this Doi.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and publication_year is None:  # noqa: E501
            raise ValueError("Invalid value for `publication_year`, must not be `None`")  # noqa: E501

        self._publication_year = publication_year

    @property
    def resource_type(self):
        """Gets the resource_type of this Doi.  # noqa: E501


        :return: The resource_type of this Doi.  # noqa: E501
        :rtype: DoiResourceType
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this Doi.


        :param resource_type: The resource_type of this Doi.  # noqa: E501
        :type: DoiResourceType
        """

        self._resource_type = resource_type

    @property
    def titles(self):
        """Gets the titles of this Doi.  # noqa: E501

        A name or title by which a resource is known.  # noqa: E501

        :return: The titles of this Doi.  # noqa: E501
        :rtype: list[DoiTitle]
        """
        return self._titles

    @titles.setter
    def titles(self, titles):
        """Sets the titles of this Doi.

        A name or title by which a resource is known.  # noqa: E501

        :param titles: The titles of this Doi.  # noqa: E501
        :type: list[DoiTitle]
        """
        if self.local_vars_configuration.client_side_validation and titles is None:  # noqa: E501
            raise ValueError("Invalid value for `titles`, must not be `None`")  # noqa: E501

        self._titles = titles

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
        if not isinstance(other, Doi):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Doi):
            return True

        return self.to_dict() != other.to_dict()
