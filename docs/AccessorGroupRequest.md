# AccessorGroupRequest

A request to retrieve a page of accessor groups. Accessors will be group by submitter and access requirement.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_requirement_id** | **str** | The condition to filter by AccessRequirement. Use null to ignore this filter.&#39;  | [optional] 
**expire_before** | **str** | The condition to filter by expiration. Use null to ignore this filter.&#39;  | [optional] 
**next_page_token** | **str** | The token to get the next page result. Use null to get the first page.&#39;  | [optional] 
**submitter_id** | **str** | The condition to filter by submitter. Use null to ignore this filter.&#39;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


