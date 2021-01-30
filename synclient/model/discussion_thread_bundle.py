"""
    Platform Repository Service

    Platform Repository Service - Sage Bionetworks Platform   # noqa: E501

    The version of the OpenAPI document: develop-SNAPSHOT
    Contact: thomas.yu@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from synclient.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)


class DiscussionThreadBundle(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'active_authors': ([str],),  # noqa: E501
            'created_by': (str,),  # noqa: E501
            'created_on': (str,),  # noqa: E501
            'etag': (str,),  # noqa: E501
            'forum_id': (str,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'is_deleted': (bool,),  # noqa: E501
            'is_edited': (bool,),  # noqa: E501
            'is_pinned': (bool,),  # noqa: E501
            'last_activity': (str,),  # noqa: E501
            'message_key': (str,),  # noqa: E501
            'modified_on': (str,),  # noqa: E501
            'number_of_replies': (int,),  # noqa: E501
            'number_of_views': (int,),  # noqa: E501
            'project_id': (str,),  # noqa: E501
            'title': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'active_authors': 'activeAuthors',  # noqa: E501
        'created_by': 'createdBy',  # noqa: E501
        'created_on': 'createdOn',  # noqa: E501
        'etag': 'etag',  # noqa: E501
        'forum_id': 'forumId',  # noqa: E501
        'id': 'id',  # noqa: E501
        'is_deleted': 'isDeleted',  # noqa: E501
        'is_edited': 'isEdited',  # noqa: E501
        'is_pinned': 'isPinned',  # noqa: E501
        'last_activity': 'lastActivity',  # noqa: E501
        'message_key': 'messageKey',  # noqa: E501
        'modified_on': 'modifiedOn',  # noqa: E501
        'number_of_replies': 'numberOfReplies',  # noqa: E501
        'number_of_views': 'numberOfViews',  # noqa: E501
        'project_id': 'projectId',  # noqa: E501
        'title': 'title',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """DiscussionThreadBundle - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            active_authors ([str]): The list of userId whose most active on this Thread. [optional]  # noqa: E501
            created_by (str): The id of the user that created this Thread. [optional]  # noqa: E501
            created_on (str): The timestamp when this Thread was created. [optional]  # noqa: E501
            etag (str): Synapse employs an Optimistic Concurrency Control (OCC) scheme to handle concurrent updates. Since the E-Tag changes every time an entity is updated it is used to detect when a client's current representation of an entity is out-of-date. . [optional]  # noqa: E501
            forum_id (str): The ID of the forum this Thread belongs to. [optional]  # noqa: E501
            id (str): The ID of the Thread. [optional]  # noqa: E501
            is_deleted (bool): Has this Thread been deleted?. [optional]  # noqa: E501
            is_edited (bool): Has the author edited this Thread?. [optional]  # noqa: E501
            is_pinned (bool): Has this Thread been pinned?. [optional]  # noqa: E501
            last_activity (str): The timestamp when the last activity occurs on this Thread. [optional]  # noqa: E501
            message_key (str): The S3 key where the actual message stored. [optional]  # noqa: E501
            modified_on (str): The timestamp when this Thread was last modified. [optional]  # noqa: E501
            number_of_replies (int): The number of replies to this thread. [optional]  # noqa: E501
            number_of_views (int): The number of unique users who has viewed this thread. [optional]  # noqa: E501
            project_id (str): The ID of the project this Thread belongs to. [optional]  # noqa: E501
            title (str): The title of the Thread. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
