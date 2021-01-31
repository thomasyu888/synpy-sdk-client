# AccessApproval

JSON schema for AccessApproval POJO
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessor_id** | **str** | The ID of the principal (user or group) approved for access | [optional] 
**created_by** | **str** | The user that created this object. | [optional] 
**created_on** | **str** | The date this object was created. | [optional] 
**etag** | **str** | Synapse employs an Optimistic Concurrency Control (OCC) scheme to handle concurrent updates. Since the E-Tag changes every time an entity is updated it is used to detect when a client&#39;s current representation of an entity is out-of-date.  | [optional] 
**expired_on** | **str** | The date this object will be expired. | [optional] 
**id** | **int** | The unique immutable ID | [optional] 
**modified_by** | **str** | The user that last modified this object. | [optional] 
**modified_on** | **str** | The date this object was last modified. | [optional] 
**requirement_id** | **int** | The ID of the Access Requirement. | [optional] 
**requirement_version** | **int** | The version of the Access Requirement. | [optional] 
**state** | [**ApprovalState**](ApprovalState.md) |  | [optional] 
**submitter_id** | **str** | The user who performed the necessary action(s) to gain this approval. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


