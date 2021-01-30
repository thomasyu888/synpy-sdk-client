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
    from synclient.model.doi_all_of import DoiAllOf
    from synclient.model.doi_association import DoiAssociation
    from synclient.model.doi_creator import DoiCreator
    from synclient.model.doi_resource_type import DoiResourceType
    from synclient.model.doi_title import DoiTitle
    from synclient.model.object_type import ObjectType
    globals()['DoiAllOf'] = DoiAllOf
    globals()['DoiAssociation'] = DoiAssociation
    globals()['DoiCreator'] = DoiCreator
    globals()['DoiResourceType'] = DoiResourceType
    globals()['DoiTitle'] = DoiTitle
    globals()['ObjectType'] = ObjectType


class Doi(ModelComposed):
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

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

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
            'object_id': (str,),  # noqa: E501
            'creators': ([DoiCreator],),  # noqa: E501
            'publication_year': (int,),  # noqa: E501
            'titles': ([DoiTitle],),  # noqa: E501
            'associated_by': (str,),  # noqa: E501
            'associated_on': (str,),  # noqa: E501
            'association_id': (str,),  # noqa: E501
            'doi_uri': (str,),  # noqa: E501
            'doi_url': (str,),  # noqa: E501
            'etag': (str,),  # noqa: E501
            'object_type': (ObjectType,),  # noqa: E501
            'object_version': (int,),  # noqa: E501
            'updated_by': (str,),  # noqa: E501
            'updated_on': (str,),  # noqa: E501
            'resource_type': (DoiResourceType,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'object_id': 'objectId',  # noqa: E501
        'creators': 'creators',  # noqa: E501
        'publication_year': 'publicationYear',  # noqa: E501
        'titles': 'titles',  # noqa: E501
        'associated_by': 'associatedBy',  # noqa: E501
        'associated_on': 'associatedOn',  # noqa: E501
        'association_id': 'associationId',  # noqa: E501
        'doi_uri': 'doiUri',  # noqa: E501
        'doi_url': 'doiUrl',  # noqa: E501
        'etag': 'etag',  # noqa: E501
        'object_type': 'objectType',  # noqa: E501
        'object_version': 'objectVersion',  # noqa: E501
        'updated_by': 'updatedBy',  # noqa: E501
        'updated_on': 'updatedOn',  # noqa: E501
        'resource_type': 'resourceType',  # noqa: E501
    }

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, object_id, creators, publication_year, titles, *args, **kwargs):  # noqa: E501
        """Doi - a model defined in OpenAPI

        Args:
            object_id (str): The ID of the digital object in Synapse for which this DOI is created.
            creators ([DoiCreator]): The main researchers involved in producing the data, or the authors of the publication, in priority order. 
            publication_year (int): The year that this resource became publicly accessible. Must be in YYYY format.
            titles ([DoiTitle]): A name or title by which a resource is known.

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
            associated_by (str): The ID of the user that creates this DOI. Provided by Synapse.. [optional]  # noqa: E501
            associated_on (str): The date time this DOI is first created. Provided by Synapse.. [optional]  # noqa: E501
            association_id (str): The unique ID of this DOI stored in Synapse. Provided by Synapse.. [optional]  # noqa: E501
            doi_uri (str): The unique URI of this DOI to which the resource can be resolved. Provided by Synapse.. [optional]  # noqa: E501
            doi_url (str): The DOI URL that will point to the Synapse object. Provided by Synapse.. [optional]  # noqa: E501
            etag (str): For Optimistic Concurrency Control (OCC). Required to successfully update a DOI.. [optional]  # noqa: E501
            object_type (ObjectType): [optional]  # noqa: E501
            object_version (int): The version of the digital object. When null, the DOI is associated with the current version of the object.. [optional]  # noqa: E501
            updated_by (str): The ID of the user that last updated this DOI. Provided by Synapse.. [optional]  # noqa: E501
            updated_on (str): The date time this DOI is last updated. Provided by Synapse.. [optional]  # noqa: E501
            resource_type (DoiResourceType): [optional]  # noqa: E501
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        required_args = {
            'object_id': object_id,
            'creators': creators,
            'publication_year': publication_year,
            'titles': titles,
        }
        # remove args whose value is Null because they are unset
        required_arg_names = list(required_args.keys())
        for required_arg_name in required_arg_names:
            if required_args[required_arg_name] is nulltype.Null:
                del required_args[required_arg_name]
        model_args = {}
        model_args.update(required_args)
        model_args.update(kwargs)
        composed_info = validate_get_composed_info(
            constant_args, model_args, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        unused_args = composed_info[3]

        for var_name, var_value in required_args.items():
            setattr(self, var_name, var_value)
        for var_name, var_value in kwargs.items():
            if var_name in unused_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        not self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error beause the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              DoiAllOf,
              DoiAssociation,
          ],
          'oneOf': [
          ],
        }
