# PaginatedResultsOfEvaluationAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | **str** | The type of access for the user to filter for, optional and defaults to ACCESS_TYPE.READ | [optional] 
**active_only** | **str** | If &#39;true&#39; then return only those evaluations with rounds defined and for which the current time is in one of the rounds.  | [optional] 
**evaluation_ids** | **str** | an optional, comma-delimited list of evaluation IDs to which the response is limited | [optional] 
**results** | [**list[Evaluation]**](Evaluation.md) | List of evaluations | [optional] 
**total_number_of_results** | **int** | Number of results per page | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


