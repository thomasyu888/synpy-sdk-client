# Submission

A submission to request access to controlled data.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_requirement_id** | **str** | The ID of the Access Requirement which requires a request to be submitted to gain access to a dataset. This submission contains information that satisfies those requirements. | [optional] 
**access_requirement_version** | **int** | The version of the Access Requirement which requires a request to be submitted to gain access to a dataset. This submission contains information that satisfies those requirements. | [optional] 
**accessor_changes** | [**[AccessorChange]**](AccessorChange.md) | List of user changes. A user can gain access, renew access or have access revoked. | [optional] 
**attachments** | **[str]** | The set of file handle ID of attached files to this request. | [optional] 
**duc_file_handle_id** | **str** | The Data Use Certificate uploaded by user. | [optional] 
**etag** | **str** | Synapse employs an Optimistic Concurrency Control (OCC) scheme to handle concurrent updates. Since the E-Tag changes every time an entity is updated it is used to detect when a client&#39;s current representation of an entity is out-of-date.  | [optional] 
**id** | **str** | The unique immutable ID for this submission. A new ID will be generated for new Submission. Once issued, this ID is guaranteed to never change or be re-issued. | [optional] 
**irb_file_handle_id** | **str** | The Institutional Review Board Approval document uploaded by user. | [optional] 
**is_renewal_submission** | **bool** | True if this submission is a renewal submission. | [optional] 
**modified_by** | **str** | The ID of the user that last modified the status of this submission. | [optional] 
**modified_on** | **str** | The date this submission was reviewed or was cancelled. | [optional] 
**publication** | **str** | Link(s) to publication that used the controlled data. | [optional] 
**rejected_reason** | **str** | The reason this submission is rejected, if it&#39;s rejected.  | [optional] 
**request_id** | **str** | The ID of the Request which is used to create this submission. | [optional] 
**research_project_snapshot** | [**ResearchProject**](ResearchProject.md) |  | [optional] 
**state** | [**SubmissionState**](SubmissionState.md) |  | [optional] 
**subject_id** | **str** | The ID of the subject user interested in. This information will be used to help user navigate back to where they were to continue their work. | [optional] 
**subject_type** | [**RestrictableObjectType**](RestrictableObjectType.md) |  | [optional] 
**submitted_by** | **str** | The ID of the user that submit this submission. | [optional] 
**submitted_on** | **str** | The date this submission was created. | [optional] 
**summary_of_use** | **str** | Summary of how the data has been used. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


