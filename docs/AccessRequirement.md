# AccessRequirement

Interface for JSON schema for AccessRequirement. The Access Requirement mechanism is distinct from the access control list in that it is controlled not by the entity owner but by a separate authority: Access Requirements are created and maintained by the Synapse Access and Compliance Team (ACT). ACTAccessRequirements can only be approved by the ACT. Self-sign Access Requirements can be approved by the user desiring access, but said user first has to meet 'terms of use' associated with the requirement. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | [**ACCESSTYPE**](ACCESSTYPE.md) |  | [optional] 
**concrete_type** | **str** | Indicates which type of AccessRequirement this object represents. Provided by the system, the user may not set this field. | [optional] 
**created_by** | **str** | The user that created this object. Provided by the system, the user may not set this field. | [optional] 
**created_on** | **str** | The date this object was created. Provided by the system, the user may not set this field. | [optional] 
**description** | **str** | Short optional description for the AR. Limited to 50 characters. | [optional] 
**etag** | **str** | Synapse employs an Optimistic Concurrency Control (OCC) scheme to handle concurrent updates. Since the E-Tag changes every time an entity is updated it is used to detect when a client&#39;s current representation of an object is out-of-date.  | [optional] 
**id** | **float** | The unique immutable ID. Provided by the system, the user may not set this field. | [optional] 
**modified_by** | **str** | The user that last modified this object. Provided by the system, the user may not set this field. | [optional] 
**modified_on** | **str** | The date this object was last modified. Provided by the system, the user may not set this field. | [optional] 
**subject_ids** | [**list[RestrictableObjectDescriptor]**](RestrictableObjectDescriptor.md) | The IDs of the items controlled by this Access Requirement. Required when creating or updating. | [optional] 
**version_number** | **int** | The version number issued to this version on the object. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


