# RowTable

Represents a single row of a TableEntity
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **str** | For queries against EntityViews with query.includeEtag&#x3D;true, this field will contain the etag of the entity. Will be null for all other cases. | [optional] 
**row_id** | **int** | The immutable ID issued to a new row. | [optional] 
**values** | **list[str]** | The values for each column of this row. To delete a row, set this to an empty list: [] | [optional] 
**version_number** | **int** | The version number of this row. Each row version is immutable, so when a row is updated a new version is created. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


