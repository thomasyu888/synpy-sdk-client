# QueryResultBundle

A bundle of information about a query result.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_models** | [**[ColumnModel]**](ColumnModel.md) | The list of ColumnModels for the table. Use mask &#x3D; 0x10 to include in the bundle. | [optional] 
**concrete_type** | **str** | Concrete Type | [optional] 
**facets** | [**[FacetColumnResult]**](FacetColumnResult.md) | The list of facets for the search results | [optional] 
**last_updated_on** | **str** | The date-time when this table/view was last updated. Note: Since views are eventually consistent a view might still be out-of-date even if it was recently updated. Use mask &#x3D; 0x80 to include in the bundle.  | [optional] 
**max_rows_per_page** | **int** | The maximum number of rows that can be retrieved in a single call. This is a function of the columns that are selected in the query. Use mask &#x3D; 0x8 to include in the bundle. | [optional] 
**query_count** | **int** | The total number of rows that match the query. Use mask &#x3D; 0x2 to include in the bundle. | [optional] 
**query_result** | [**QueryResult**](QueryResult.md) |  | [optional] 
**select_columns** | [**[SelectColumn]**](SelectColumn.md) | The list of SelectColumns from the select clause. Use mask &#x3D; 0x4 to include in the bundle. | [optional] 
**sum_file_sizes** | [**SumFileSizes**](SumFileSizes.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


