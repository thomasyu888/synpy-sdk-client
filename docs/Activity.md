# Activity

Interface for JSON schema for Activity POJO.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | The user that created this object. | [optional] 
**created_on** | **str** | The date this object was created. | [optional] 
**description** | **str** | A description of this Activity. | [optional] 
**etag** | **str** | Synapse employs an Optimistic Concurrency Control (OCC) scheme to handle concurrent updates. Since the E-Tag changes every time an entity is updated it is used to detect when a client&#39;s current representation of an entity is out-of-date.  | [optional] 
**id** | **str** | The unique immutable ID | [optional] 
**modified_by** | **str** | The user that last modified this object. | [optional] 
**modified_on** | **str** | The date this object was last modified. | [optional] 
**name** | **str** | A name for this Activity. | [optional] 
**used** | [**list[Used]**](Used.md) | The entities used by this Activity. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


