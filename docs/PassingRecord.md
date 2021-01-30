# PassingRecord

A record of whether a given user passed a given test
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corrections** | [**[ResponseCorrectness]**](ResponseCorrectness.md) | For each response, whether it was correct | [optional] 
**passed** | **bool** | Whether the user passed the given test | [optional] 
**passed_on** | **str** | Date/time when the user passed the test (omitted if the user has not passed) | [optional] 
**quiz_id** | **int** | The id of the quiz | [optional] 
**response_id** | **int** | The id of the user&#39;s response  | [optional] 
**score** | **int** | The score the user received on the test | [optional] 
**user_id** | **str** | The principal id of the user | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


