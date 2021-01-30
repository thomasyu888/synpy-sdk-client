# FormData

User's data gathered from a form template. All FormData belongs to a single FormGroup. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | Id of the user that created this object | [optional] 
**created_on** | **str** | The date this object was originally created. | [optional] 
**data_file_handle_id** | **str** | The identifier of the data FileHandle for this object. | [optional] 
**etag** | **str** | Will change whenever there is a change to the this data or its status. | [optional] 
**form_data_id** | **str** | The system issued identifier that uniquely identifies this object. | [optional] 
**group_id** | **str** | The identifier of the group that manages this data. Required. | [optional] 
**modified_on** | **str** | The date this object was last modified. | [optional] 
**name** | **str** | User provided name for this submission. Required. | [optional] 
**submission_status** | [**SubmissionStatusForm**](SubmissionStatusForm.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


