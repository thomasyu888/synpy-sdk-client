# SubmissionStatusModel

A SubmissionStatus is a secondary, mutable object associated with a Submission. This object should be used to contain scoring data about the Submission. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | [**AnnotationsAnnotation**](AnnotationsAnnotation.md) |  | [optional] 
**can_cancel** | **bool** | Can this submission be cancelled? By default, this will be set to False. Users can read this value. Only the queue&#39;s scoring application can change this value.  | [optional] 
**cancel_requested** | **bool** | Has user requested to cancel this submission? By default, this will be set to False. Submission owner can read and request to change this value. | [optional] 
**entity_id** | **str** | The Synapse ID of the Entity in this Submission. | [optional] 
**etag** | **str** | Synapse employs an Optimistic Concurrency Control (OCC) scheme to handle concurrent updates. The eTag changes every time an SubmissionStatus is updated; it is used to detect when a client&#39;s copy of an SubmissionStatus is out-of-date.  | [optional] 
**id** | **str** | The unique, immutable Synapse ID of the Submission. | [optional] 
**modified_on** | **str** | The date on which this SubmissionStatus was last modified. | [optional] 
**status** | [**SubmissionStatusEnum**](SubmissionStatusEnum.md) |  | [optional] 
**status_version** | **float** | A version of the status, auto-generated and auto-incremented by the system and read-only to the client. | [optional] 
**submission_annotations** | [**AnnotationsV2**](AnnotationsV2.md) |  | [optional] 
**version_number** | **int** | The version number of the Entity in this Submission. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


