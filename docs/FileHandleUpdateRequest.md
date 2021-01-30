# FileHandleUpdateRequest

Reuqest that can be used to update the file handle of an FileEntity
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_file_handle_id** | **str** | The id of the new file handle to be associated with the FileEntity. The user performing the request must be the owner of the file handle.  | [optional] 
**old_file_handle_id** | **str** | The id of the file handle currently associated to the FileEntity. Used to avoid conflicting cuncurrent updates, if the id does not match the current file handle id the request will be rejected with a PRECONDITION_FAILED (412) response.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


