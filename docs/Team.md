# Team

JSON schema for Team POJO
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_public_join** | **bool** | true for teams which members can join without an invitation or approval | [optional] 
**created_by** | **str** | The ID of the user that created this Team. | [optional] 
**created_on** | **str** | The date this Team was created. | [optional] 
**description** | **str** | A short description of this Team. | [optional] 
**etag** | **str** | Synapse employs an Optimistic Concurrency Control (OCC) scheme to handle concurrent updates. Since the E-Tag changes every time a Team is updated it is used to detect when a client&#39;s current representation of a Team is out-of-date.  | [optional] 
**icon** | **str** | fileHandleId for icon image of the Team | [optional] 
**id** | **str** | The id of the Team. | [optional] 
**modified_by** | **str** | The ID of the user that last modified this Team. | [optional] 
**modified_on** | **str** | The date this Team was last modified. | [optional] 
**name** | **str** | The name of the Team. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


