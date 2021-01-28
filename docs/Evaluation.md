# Evaluation

An Evaluation is the core object of the Evaluation API, used to support collaborative data analysis challenges in Synapse.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_source** | **str** | The Synapse ID of the Entity to which this Evaluation belongs, e.g. a reference to a Synapse project. | [optional] 
**created_on** | **str** | The date on which Evaluation was created. | [optional] 
**description** | **str** | A text description of this Evaluation. | [optional] 
**etag** | **str** | Synapse employs an Optimistic Concurrency Control (OCC) scheme to handle concurrent updates. The eTag changes every time an Evaluation is updated; it is used to detect when a client&#39;s copy of an Evaluation is out-of-date.  | [optional] 
**id** | **str** | The unique immutable ID for this Evaluation. | [optional] 
**name** | **str** | The name of this Evaluation | [optional] 
**owner_id** | **str** | The ID of the Synapse user who created this Evaluation. | [optional] 
**quota** | [**SubmissionQuota**](SubmissionQuota.md) |  | [optional] 
**status** | [**EvaluationStatus**](EvaluationStatus.md) |  | [optional] 
**submission_instructions_message** | **str** | Message to display to users detailing acceptable formatting for Submissions to this Evaluation. | [optional] 
**submission_receipt_message** | **str** | Message to display to users upon successful submission to this Evaluation. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


