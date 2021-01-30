# DiscussionThreadBundle

The Thread model object represents a single Thread.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_authors** | **[str]** | The list of userId whose most active on this Thread | [optional] 
**created_by** | **str** | The id of the user that created this Thread | [optional] 
**created_on** | **str** | The timestamp when this Thread was created | [optional] 
**etag** | **str** | Synapse employs an Optimistic Concurrency Control (OCC) scheme to handle concurrent updates. Since the E-Tag changes every time an entity is updated it is used to detect when a client&#39;s current representation of an entity is out-of-date.  | [optional] 
**forum_id** | **str** | The ID of the forum this Thread belongs to | [optional] 
**id** | **str** | The ID of the Thread | [optional] 
**is_deleted** | **bool** | Has this Thread been deleted? | [optional] 
**is_edited** | **bool** | Has the author edited this Thread? | [optional] 
**is_pinned** | **bool** | Has this Thread been pinned? | [optional] 
**last_activity** | **str** | The timestamp when the last activity occurs on this Thread | [optional] 
**message_key** | **str** | The S3 key where the actual message stored | [optional] 
**modified_on** | **str** | The timestamp when this Thread was last modified | [optional] 
**number_of_replies** | **int** | The number of replies to this thread | [optional] 
**number_of_views** | **int** | The number of unique users who has viewed this thread | [optional] 
**project_id** | **str** | The ID of the project this Thread belongs to | [optional] 
**title** | **str** | The title of the Thread | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


