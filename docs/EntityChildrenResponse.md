# EntityChildrenResponse

Response of EntityHeaders for the children of a given parent Entity
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page_token** | **str** | Token that can be used to get the next page. Null if there are no more results. | [optional] 
**page** | [**list[EntityHeader]**](EntityHeader.md) | The headers of each child. | [optional] 
**sum_file_sizes_bytes** | **int** | The sum of the file sizes (bytes) with the requested parentId and types. Only returned if requested. | [optional] 
**total_child_count** | **int** | The total number of children with the requested parentId and types. Only returned if requested. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


