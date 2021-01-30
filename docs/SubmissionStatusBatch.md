# SubmissionStatusBatch

A batch of status objects, to be updated en masse.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_token** | **str** | A token required to accept a batch submission for all but the first batch. | [optional] 
**is_first_batch** | **bool** | true if and only if this is the first batch to upload | [optional] 
**is_last_batch** | **bool** | true if and only if this is the last batch to upload | [optional] 
**statuses** | [**[SubmissionStatusModel]**](SubmissionStatusModel.md) | A collection of Submission Statuses | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


