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
    from synclient.model.type import TYPE
    globals()['TYPE'] = TYPE


class JsonSchema(ModelNormal):
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
            'id': (str,),  # noqa: E501
            'ref': (str,),  # noqa: E501
            'schema': (str,),  # noqa: E501
            'const': (str,),  # noqa: E501
            '_else': (JsonSchema,),  # noqa: E501
            'enum': ([str],),  # noqa: E501
            '_if': (JsonSchema,),  # noqa: E501
            'all_of': ([JsonSchema],),  # noqa: E501
            'any_of': ([JsonSchema],),  # noqa: E501
            'definitions': ({str: (JsonSchema,)},),  # noqa: E501
            'description': (str,),  # noqa: E501
            'format': (str,),  # noqa: E501
            'items': (JsonSchema,),  # noqa: E501
            'max_length': (int,),  # noqa: E501
            'min_length': (int,),  # noqa: E501
            'one_of': ([JsonSchema],),  # noqa: E501
            'pattern': (str,),  # noqa: E501
            'properties': ({str: (JsonSchema,)},),  # noqa: E501
            'required': ([str],),  # noqa: E501
            'source': (str,),  # noqa: E501
            'then': (JsonSchema,),  # noqa: E501
            'title': (str,),  # noqa: E501
            'type': (TYPE,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': '$id',  # noqa: E501
        'ref': '$ref',  # noqa: E501
        'schema': '$schema',  # noqa: E501
        'const': '_const',  # noqa: E501
        '_else': '_else',  # noqa: E501
        'enum': '_enum',  # noqa: E501
        '_if': '_if',  # noqa: E501
        'all_of': 'allOf',  # noqa: E501
        'any_of': 'anyOf',  # noqa: E501
        'definitions': 'definitions',  # noqa: E501
        'description': 'description',  # noqa: E501
        'format': 'format',  # noqa: E501
        'items': 'items',  # noqa: E501
        'max_length': 'maxLength',  # noqa: E501
        'min_length': 'minLength',  # noqa: E501
        'one_of': 'oneOf',  # noqa: E501
        'pattern': 'pattern',  # noqa: E501
        'properties': 'properties',  # noqa: E501
        'required': 'required',  # noqa: E501
        'source': 'source',  # noqa: E501
        'then': 'then',  # noqa: E501
        'title': 'title',  # noqa: E501
        'type': 'type',  # noqa: E501
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
        """JsonSchema - a model defined in OpenAPI

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
            id (str): https://json-schema.org/draft/2019-09/json-schema-core.html#rfc.section.8.2.2 . [optional]  # noqa: E501
            ref (str): https://json-schema.org/draft/2019-09/json-schema-core.html#rfc.section.8.2.4.1 . [optional]  # noqa: E501
            schema (str): https://json-schema.org/draft/2019-09/json-schema-core.html#rfc.section.8.1.1 . [optional]  # noqa: E501
            const (str): https://json-schema.org/draft/2019-09/json-schema-validation.html#rfc.section.6.1.3 . [optional]  # noqa: E501
            _else (JsonSchema): [optional]  # noqa: E501
            enum ([str]): https://json-schema.org/draft/2019-09/json-schema-validation.html#rfc.section.6.1.2 . [optional]  # noqa: E501
            _if (JsonSchema): [optional]  # noqa: E501
            all_of ([JsonSchema]): Use allOf to 'extend' or 'implement' one or more schemas. https://json-schema.org/draft/2019-09/json-schema-core.html#rfc.section.9.2.1.1 . [optional]  # noqa: E501
            any_of ([JsonSchema]): https://json-schema.org/draft/2019-09/json-schema-core.html#rfc.section.9.2.1.2 . [optional]  # noqa: E501
            definitions ({str: (JsonSchema,)}): In an effort to support draft-07 implementations, we are using 'definitions' instead of '$defs'. https://json-schema.org/draft/2019-09/json-schema-validation.html#rfc.appendix.A . [optional]  # noqa: E501
            description (str): https://json-schema.org/draft/2019-09/json-schema-hypermedia.html#rfc.section.6.5.2' . [optional]  # noqa: E501
            format (str): https://json-schema.org/draft/2019-09/json-schema-validation.html#rfc.section.7.3' . [optional]  # noqa: E501
            items (JsonSchema): [optional]  # noqa: E501
            max_length (int): https://tools.ietf.org/html/draft-handrews-json-schema-validation-02#section-6.3.1'. [optional]  # noqa: E501
            min_length (int): https://tools.ietf.org/html/draft-handrews-json-schema-validation-02#section-6.3.2' . [optional]  # noqa: E501
            one_of ([JsonSchema]): https://json-schema.org/draft/2019-09/json-schema-core.html#rfc.section.9.2.1.3' . [optional]  # noqa: E501
            pattern (str): https://tools.ietf.org/html/draft-handrews-json-schema-validation-02#section-6.3.3 . [optional]  # noqa: E501
            properties ({str: (JsonSchema,)}): https://json-schema.org/draft/2019-09/json-schema-core.html#rfc.section.9.3.2.1. [optional]  # noqa: E501
            required ([str]): https://json-schema.org/draft/2019-09/json-schema-validation.html#rfc.section.6.5.3. [optional]  # noqa: E501
            source (str): Used to indicate that this schema is derived from another object/schema. The value should be a URL reference to the original work. The 'source' is solely descriptive and should have no impact on validation. . [optional]  # noqa: E501
            then (JsonSchema): [optional]  # noqa: E501
            title (str): https://json-schema.org/draft/2019-09/json-schema-hypermedia.html#rfc.section.6.5.1 . [optional]  # noqa: E501
            type (TYPE): [optional]  # noqa: E501
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
