# ValidationSummaryStatistics

Summary statistics for the JSON schema validation results for the children of an Entity container (Project or Folder)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_id** | **str** | The ID of the container Entity. | [optional] 
**generated_on** | **str** | The date-time when the statistics were calculated. | [optional] 
**number_of_invalid_children** | **int** | The total number of children that are invalid according to their bound JSON schema. | [optional] 
**number_of_unknown_children** | **int** | The total number of children that do not have validation results. This can occur when a child does not have a bound JSON schema or when a child has not been validated yet. | [optional] 
**number_of_valid_children** | **int** | The total number of children that are valid according to their bound JSON schema. | [optional] 
**total_number_of_children** | **int** | The total number of children in the container. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


