# DownloadFromTableResult

The response body of an asynchronous CSV table download job.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concrete_type** | **str** | Concrete Type | [optional] 
**etag** | **str** | Any RowSet returned from Synapse will contain the current etag of the change set. To update any rows from a RowSet the etag must be provided with the POST.  | [optional] 
**headers** | [**[SelectColumn]**](SelectColumn.md) | The list of SelectColumns that describes the rows of this set. | [optional] 
**results_file_handle_id** | **str** | The resulting file handle ID can be used to download the CSV file created by this job. The file will contain all of the data requested in the query SQL provided when the job was started.  | [optional] 
**table_id** | **str** | The ID of the table identified in the from clause of the table query. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


