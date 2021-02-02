# AsynchronousJobStatus

Object used to track the status of an Asynchronous Job.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changed_on** | **str** | The date-time when the status of this table last changed. | [optional] 
**error_details** | **str** | When processing fails, this is the full stack trace of the error. | [optional] 
**error_message** | **str** | When processing fails, this is a one line error message. | [optional] 
**etag** | **str** | The etag of the status will change whenever the status changes. | [optional] 
**exception** | **str** | The exception that needs to be thrown | [optional] 
**job_canceling** | **bool** | Was the job being asked to cancel. | [optional] 
**job_id** | **str** | The ID if the job issued when this job request was issued. | [optional] 
**job_state** | [**AsynchJobState**](AsynchJobState.md) |  | [optional] 
**progress_current** | **int** | The progress current value indicates how much progress has been made. For example: If progressTotal &#x3D; 100; and progressCurrent &#x3D; 50; then the work is 50% complete.  | [optional] 
**progress_message** | **str** | The current message of the progress tracker. | [optional] 
**progress_total** | **int** | The progress total indicates the total amount of work to complete. For example: If progressTotal &#x3D; 100; and progressCurrent &#x3D; 50; then the work is 50% complete.  | [optional] 
**request_body** | [**AsynchronousRequestBody**](AsynchronousRequestBody.md) |  | [optional] 
**response_body** | [**AsynchronousResponseBody**](AsynchronousResponseBody.md) |  | [optional] 
**runtime_ms** | **float** | The number of milliseconds from the start to completion of this job. | [optional] 
**started_by_user_id** | **int** | The ID of the user that started the job | [optional] 
**started_on** | **str** | The date-time when the status of this table last changed to PROCESSING. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


