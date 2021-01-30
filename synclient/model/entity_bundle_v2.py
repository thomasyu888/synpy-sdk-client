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

def lazy_import():
    from synclient.model.access_control_list import AccessControlList
    from synclient.model.annotations_v2 import AnnotationsV2
    from synclient.model.doi_association import DoiAssociation
    from synclient.model.entity import Entity
    from synclient.model.entity_path import EntityPath
    from synclient.model.entity_type import EntityType
    from synclient.model.file_handle import FileHandle
    from synclient.model.restriction_information_response import RestrictionInformationResponse
    from synclient.model.table_bundle import TableBundle
    from synclient.model.user_entity_permissions import UserEntityPermissions
    globals()['AccessControlList'] = AccessControlList
    globals()['AnnotationsV2'] = AnnotationsV2
    globals()['DoiAssociation'] = DoiAssociation
    globals()['Entity'] = Entity
    globals()['EntityPath'] = EntityPath
    globals()['EntityType'] = EntityType
    globals()['FileHandle'] = FileHandle
    globals()['RestrictionInformationResponse'] = RestrictionInformationResponse
    globals()['TableBundle'] = TableBundle
    globals()['UserEntityPermissions'] = UserEntityPermissions


class EntityBundleV2(ModelNormal):
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
        lazy_import()
        return {
            'access_control_list': (AccessControlList,),  # noqa: E501
            'annotations': (AnnotationsV2,),  # noqa: E501
            'benefactor_acl': (AccessControlList,),  # noqa: E501
            'doi_association': (DoiAssociation,),  # noqa: E501
            'entity': (Entity,),  # noqa: E501
            'entity_type': (EntityType,),  # noqa: E501
            'file_handles': ([FileHandle],),  # noqa: E501
            'file_name': (str,),  # noqa: E501
            'has_children': (bool,),  # noqa: E501
            'path': (EntityPath,),  # noqa: E501
            'permissions': (UserEntityPermissions,),  # noqa: E501
            'restriction_information': (RestrictionInformationResponse,),  # noqa: E501
            'root_wiki_id': (str,),  # noqa: E501
            'table_bundle': (TableBundle,),  # noqa: E501
            'thread_count': (float,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'access_control_list': 'accessControlList',  # noqa: E501
        'annotations': 'annotations',  # noqa: E501
        'benefactor_acl': 'benefactorAcl',  # noqa: E501
        'doi_association': 'doiAssociation',  # noqa: E501
        'entity': 'entity',  # noqa: E501
        'entity_type': 'entityType',  # noqa: E501
        'file_handles': 'fileHandles',  # noqa: E501
        'file_name': 'fileName',  # noqa: E501
        'has_children': 'hasChildren',  # noqa: E501
        'path': 'path',  # noqa: E501
        'permissions': 'permissions',  # noqa: E501
        'restriction_information': 'restrictionInformation',  # noqa: E501
        'root_wiki_id': 'rootWikiId',  # noqa: E501
        'table_bundle': 'tableBundle',  # noqa: E501
        'thread_count': 'threadCount',  # noqa: E501
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
        """EntityBundleV2 - a model defined in OpenAPI

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
            access_control_list (AccessControlList): [optional]  # noqa: E501
            annotations (AnnotationsV2): [optional]  # noqa: E501
            benefactor_acl (AccessControlList): [optional]  # noqa: E501
            doi_association (DoiAssociation): [optional]  # noqa: E501
            entity (Entity): [optional]  # noqa: E501
            entity_type (EntityType): [optional]  # noqa: E501
            file_handles ([FileHandle]): FileHandles associated with this Entity. [optional]  # noqa: E501
            file_name (str): If this Entity is a FileEntity, this is its filename. [optional]  # noqa: E501
            has_children (bool): Whether or not this Entity has children. [optional]  # noqa: E501
            path (EntityPath): [optional]  # noqa: E501
            permissions (UserEntityPermissions): [optional]  # noqa: E501
            restriction_information (RestrictionInformationResponse): [optional]  # noqa: E501
            root_wiki_id (str): Id of the root Wiki associated with this Entity. [optional]  # noqa: E501
            table_bundle (TableBundle): [optional]  # noqa: E501
            thread_count (float): Number of disucssion threads that reference this Entity. [optional]  # noqa: E501
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