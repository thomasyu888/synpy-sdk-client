# Doi

JSON schema for fields associated with a DOI and its metadata.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_id** | **str** | The ID of the digital object in Synapse for which this DOI is created. | 
**creators** | [**[DoiCreator]**](DoiCreator.md) | The main researchers involved in producing the data, or the authors of the publication, in priority order.  | 
**publication_year** | **int** | The year that this resource became publicly accessible. Must be in YYYY format. | 
**titles** | [**[DoiTitle]**](DoiTitle.md) | A name or title by which a resource is known. | 
**associated_by** | **str** | The ID of the user that creates this DOI. Provided by Synapse. | [optional] 
**associated_on** | **str** | The date time this DOI is first created. Provided by Synapse. | [optional] 
**association_id** | **str** | The unique ID of this DOI stored in Synapse. Provided by Synapse. | [optional] 
**doi_uri** | **str** | The unique URI of this DOI to which the resource can be resolved. Provided by Synapse. | [optional] 
**doi_url** | **str** | The DOI URL that will point to the Synapse object. Provided by Synapse. | [optional] 
**etag** | **str** | For Optimistic Concurrency Control (OCC). Required to successfully update a DOI. | [optional] 
**object_type** | [**ObjectType**](ObjectType.md) |  | [optional] 
**object_version** | **int** | The version of the digital object. When null, the DOI is associated with the current version of the object. | [optional] 
**updated_by** | **str** | The ID of the user that last updated this DOI. Provided by Synapse. | [optional] 
**updated_on** | **str** | The date time this DOI is last updated. Provided by Synapse. | [optional] 
**resource_type** | [**DoiResourceType**](DoiResourceType.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


