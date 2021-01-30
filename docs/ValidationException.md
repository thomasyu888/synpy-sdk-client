# ValidationException

A recursive ValidationException that describes all schema violations for an entire schema tree.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**causing_exceptions** | [**[ValidationException]**](ValidationException.md) | An array of sub-exceptions. | [optional] 
**keyword** | **str** | The JSON schema keyword which was violated. | [optional] 
**message** | **str** | The description of the validation failure. | [optional] 
**pointer_to_violation** | **str** | A JSON Pointer denoting the path from the input document root to its fragment which caused the validation failure. | [optional] 
**schema_location** | **str** | A JSON Pointer denoting the path from the schema JSON root to the violated keyword. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


