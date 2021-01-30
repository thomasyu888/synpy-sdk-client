# TableFileHandleResults

JSON schema for TableFileHandleResults.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | [**list[SelectColumn]**](SelectColumn.md) | The list of ColumnModels ID that describes the rows of this set. | [optional] 
**rows** | [**list[FileHandleResults]**](FileHandleResults.md) | For each row a list of file handles for each requested column | [optional] 
**table_id** | **str** | The ID of the TableEntity than owns these rows | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


