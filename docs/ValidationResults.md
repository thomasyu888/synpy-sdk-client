# ValidationResults

Results of validating an object against a schema
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_validation_messages** | **[str]** | If the object is not valid according to the schema, a the flat list of error messages will be provided with one error message per sub-schema.  | [optional] 
**is_valid** | **bool** | True if the object is currently valid according to the schema. | [optional] 
**object_etag** | **str** | The etag of the object at the time of validation. Note: If this etag does not match the current etag of the object then these validation results should be considered out of date.  | [optional] 
**object_id** | **str** | The identifier of the object that was validated. | [optional] 
**object_type** | [**ObjectTypeSchema**](ObjectTypeSchema.md) |  | [optional] 
**schemaid** | **str** | The $id of the schema that the object was validated against. | [optional] 
**validated_on** | **str** | The date-time this object was validated | [optional] 
**validation_error_message** | **str** | If the object is not valid according to the schema, a simple one line error message will be provided.  | [optional] 
**validation_exception** | [**ValidationException**](ValidationException.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


