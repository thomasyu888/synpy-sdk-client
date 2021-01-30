# FileHandle

The FileHandle interface defines all of the fields that are common to all implementations.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concrete_type** | **str** | This is used to indicate the implementation of this interface. For example, an S3FileHandle should be set to: org.sagebionetworks.repo.model.file.S3FileHandle  | [optional] 
**content_md5** | **str** | The file&#39;s content MD5.  | [optional] 
**content_size** | **int** | The size of the file in bytes. | [optional] 
**content_type** | **str** | Must be: http://en.wikipedia.org/wiki/Internet_media_type  | [optional] 
**created_by** | **str** | The ID Of the user that created this file. | [optional] 
**created_on** | **str** | The date when this file was uploaded. | [optional] 
**etag** | **str** | Synapse employs an Optimistic Concurrency Control (OCC) scheme to handle concurrent updates. Since the E-Tag changes every time an entity is updated it is used to detect when a client&#39;s current representation of an entity is out-of-date.  | [optional] 
**file_name** | **str** | The short, user visible name for this file. | [optional] 
**id** | **str** | The ID of this FileHandle. All references to this FileHandle will use this ID. Synapse will generate this ID when the FileHandle is created.  | [optional] 
**storage_location_id** | **int** | The optional storage location descriptor | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


