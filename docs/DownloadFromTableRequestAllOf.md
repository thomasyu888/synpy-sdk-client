# DownloadFromTableRequestAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concrete_type** | **str** | Concrete Type | [optional] 
**csv_table_descriptor** | [**CsvTableDescriptor**](CsvTableDescriptor.md) |  | [optional] 
**entity_id** | **str** | Entity Id | [optional] 
**include_row_id_and_row_version** | **bool** | Should the first two columns contain the row ID and row version? The default value is &#39;true&#39;.  | [optional]  if omitted the server will use the default value of True
**write_header** | **bool** | Should the first line contain the columns names as a header in the resulting file? Set to &#39;true&#39; to include the headers else, &#39;false&#39;. The default value is &#39;true&#39;.  | [optional]  if omitted the server will use the default value of True

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


