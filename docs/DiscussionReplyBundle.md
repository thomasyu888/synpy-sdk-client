# DiscussionReplyBundle

The Reply model object represents a single reply in a thread.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | The id of the user that created this Reply | [optional] 
**created_on** | **str** | The timestamp when this Reply was created | [optional] 
**etag** | **str** | Synapse employs an Optimistic Concurrency Control (OCC) scheme to handle concurrent updates. Since the E-Tag changes every time an entity is updated it is used to detect when a client&#39;s current representation of an entity is out-of-date.  | [optional] 
**forum_id** | **str** | The ID of the forum this Reply belongs to | [optional] 
**id** | **str** | The ID of the reply | [optional] 
**is_deleted** | **bool** | Has this Reply been deleted? | [optional] 
**is_edited** | **bool** | Has the author edited this Reply? | [optional] 
**message_key** | **str** | The S3 key where the actual message stored | [optional] 
**modified_on** | **str** | The timestamp when this Reply was last modified | [optional] 
**project_id** | **str** | The ID of the project this Reply belongs to | [optional] 
**thread_id** | **str** | The ID of the thread this Reply belongs to | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


