# RequestInterface

This is the base interface that all Request implements.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_requirement_id** | **str** | The ID of the Access Requirement which requires a request to be submitted to gain access to a dataset. This request contains information that satisfies those requirements.  | [optional] 
**accessor_changes** | [**[AccessorChange]**](AccessorChange.md) | List of user changes. A user can gain access, renew access or have access revoked. | [optional] 
**attachments** | **[str]** | The set of file handle ID of attached files to this request. | [optional] 
**concrete_type** | **str** | Indicates which implementation of RequestInterface this object represents. | [optional] 
**created_by** | **str** | The ID of the user that created this request. | [optional] 
**created_on** | **float** | The date this request was created. | [optional] 
**duc_file_handle_id** | **str** | The Data Use Certificate uploaded by user. | [optional] 
**etag** | **str** | Synapse employs an Optimistic Concurrency Control (OCC) scheme to handle concurrent updates. Since the E-Tag changes every time an entity is updated it is used to detect when a client&#39;s current representation of an entity is out-of-date.  | [optional] 
**id** | **str** | The unique immutable ID for this request. A new ID will be generated for new Request. Once issued, this ID is guaranteed to never change or be re-issued.  | [optional] 
**irb_file_handle_id** | **str** | The Institutional Review Board Approval document uploaded by user. | [optional] 
**modified_by** | **str** | The ID of the user that last modified this request. | [optional] 
**modified_on** | **float** | The date this request was last modified. | [optional] 
**research_project_id** | **str** | The ID of the research project associated with this request. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


