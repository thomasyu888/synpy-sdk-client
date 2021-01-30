# synclient.EntityServicesApi

All URIs are relative to *https://repo-prod.prod.sagebase.org/repo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bind_json_schema_to_entity**](EntityServicesApi.md#bind_json_schema_to_entity) | **PUT** /entity/{id}/schema/binding | Bind a JSON schema to an Entity.
[**change_entity_data_type**](EntityServicesApi.md#change_entity_data_type) | **PUT** /entity/{id}/datatype | Change the.
[**clear_bound_schema**](EntityServicesApi.md#clear_bound_schema) | **DELETE** /entity/{id}/schema/binding | Clear the bound JSON schema from this Entity.
[**create_entity**](EntityServicesApi.md#create_entity) | **POST** /entity | Create a new Entity.
[**create_entity_acl**](EntityServicesApi.md#create_entity_acl) | **POST** /entity/{id}/acl | Create a new Access Control List (ACL), overriding inheritance.
[**delete_activity**](EntityServicesApi.md#delete_activity) | **DELETE** /entity/{id}/generatedBy | Deletes the activity relationship for the current version of an Entity.
[**delete_entity**](EntityServicesApi.md#delete_entity) | **DELETE** /entity/{id} | Deletes an Entity
[**delete_entity_acl**](EntityServicesApi.md#delete_entity_acl) | **DELETE** /entity/{id}/acl | Delete the Access Control List (ACL) for a given Entity.
[**delete_entity_version**](EntityServicesApi.md#delete_entity_version) | **DELETE** /entity/{id}/version/{versionNumber} | Delete a specific version of a FileEntity.
[**file_preview_redirect_url_for_version**](EntityServicesApi.md#file_preview_redirect_url_for_version) | **GET** /entity/{id}/version/{versionNumber}/filepreview | Get the URL of the preview file associated with a specific version of a FileEntity. 
[**get_activity**](EntityServicesApi.md#get_activity) | **GET** /entity/{id}/generatedBy | Get an existing activity for the current version of an Entity.
[**get_activity_for_entity_version**](EntityServicesApi.md#get_activity_for_entity_version) | **GET** /entity/{id}/version/{versionNumber}/generatedBy | Get an existing activity for a specific version of an Entity.
[**get_all_versions_of_entity**](EntityServicesApi.md#get_all_versions_of_entity) | **GET** /entity/{id}/version | Get all versions of an Entity one page at a time.
[**get_bound_json_schema**](EntityServicesApi.md#get_bound_json_schema) | **GET** /entity/{id}/schema/binding | Get information about a JSON schema bound to an Entity.
[**get_children**](EntityServicesApi.md#get_children) | **POST** /entity/children | Get a page of children for a given parent ID.
[**get_entity**](EntityServicesApi.md#get_entity) | **GET** /entity/{id} | Get an Entity
[**get_entity_acl**](EntityServicesApi.md#get_entity_acl) | **GET** /entity/{id}/acl | Get the Access Control List (ACL) for a given entity.
[**get_entity_annotations**](EntityServicesApi.md#get_entity_annotations) | **GET** /entity/{id}/annotations2 | Get the annotations for an entity.
[**get_entity_annotations_v2_for_version**](EntityServicesApi.md#get_entity_annotations_v2_for_version) | **GET** /entity/{id}/version/{versionNumber}/annotations2 | Get an Entity&#39;s annotations for a specific version of a FileEntity.
[**get_entity_benefactor**](EntityServicesApi.md#get_entity_benefactor) | **GET** /entity/{id}/benefactor | Get an Entity&#39;s benefactor.
[**get_entity_file_handles**](EntityServicesApi.md#get_entity_file_handles) | **GET** /entity/{id}/filehandles | Get the FileHandles of the file currently associated with the current version of the Entity. 
[**get_entity_file_handles_for_version**](EntityServicesApi.md#get_entity_file_handles_for_version) | **GET** /entity/{id}/version/{versionNumber}/filehandles | Get the FileHandles of the file associated with a specific version of a FileEntity. 
[**get_entity_for_version**](EntityServicesApi.md#get_entity_for_version) | **GET** /entity/{id}/version/{versionNumber} | Get a specific version of an Entity.
[**get_entity_header_by_md5**](EntityServicesApi.md#get_entity_header_by_md5) | **GET** /entity/md5/{md5} | Gets FileEntities matching the given MD5 string which the user has read access to. 
[**get_entity_id_by_alias**](EntityServicesApi.md#get_entity_id_by_alias) | **GET** /entity/alias/{alias} | Lookup an Entity ID using an alias.
[**get_entity_json**](EntityServicesApi.md#get_entity_json) | **GET** /entity/{id}/json | Get the raw JSON for the given entity.
[**get_entity_path**](EntityServicesApi.md#get_entity_path) | **GET** /entity/{id}/path | Get the full path of an Entity as a List of EntityHeaders.
[**get_entity_schema_validation_results**](EntityServicesApi.md#get_entity_schema_validation_results) | **GET** /entity/{id}/schema/validation | Get the validation results of an Entity against its bound JSON schema.
[**get_entity_schema_validation_statistics**](EntityServicesApi.md#get_entity_schema_validation_statistics) | **GET** /entity/{id}/schema/validation/statistics | Get the summary statistics of the JSON schema validation results for a single container Entity such as a Project or Folder. 
[**get_entity_type**](EntityServicesApi.md#get_entity_type) | **GET** /entity/{id}/type | Get the EntityHeader of an Entity given its ID.
[**get_entity_type_batch**](EntityServicesApi.md#get_entity_type_batch) | **GET** /entity/type | Get a batch of EntityHeader given multile Entity IDs.
[**get_entity_versioned_type_batch**](EntityServicesApi.md#get_entity_versioned_type_batch) | **POST** /entity/header | Get the EntityHeader for a list of references with a POST.
[**get_file_preview_url**](EntityServicesApi.md#get_file_preview_url) | **GET** /entity/{id}/filepreview | Get the URL of the preview file associated with the current version of a FileEntity. 
[**get_invalid_validation_results**](EntityServicesApi.md#get_invalid_validation_results) | **POST** /entity/{id}/schema/validation/invalid | Get a single page of invalid JSON schema validation results for a container Entity (Project or Folder). 
[**get_temporary_credentials_for_entity**](EntityServicesApi.md#get_temporary_credentials_for_entity) | **GET** /entity/{id}/sts | Gets the temporary S3 credentials from STS for the given entity.
[**get_user_entity_permissions**](EntityServicesApi.md#get_user_entity_permissions) | **GET** /entity/{id}/permissions | Get the list of permission that the caller has on a given Entity.
[**has_access**](EntityServicesApi.md#has_access) | **GET** /entity/{id}/access | Determine if the caller have a given permission on a given Entity.
[**lookup_child**](EntityServicesApi.md#lookup_child) | **POST** /entity/child | Retrieve an entityId for a given parent ID and entity name.
[**update_activity_for_entity**](EntityServicesApi.md#update_activity_for_entity) | **PUT** /entity/{id}/generatedBy | Sets the generatedBy relationship for the current version of an Entity.
[**update_entity**](EntityServicesApi.md#update_entity) | **PUT** /entity/{id} | Update an entity.
[**update_entity_acl**](EntityServicesApi.md#update_entity_acl) | **PUT** /entity/{id}/acl | Update an Entity&#39;s ACL.
[**update_entity_annotations**](EntityServicesApi.md#update_entity_annotations) | **PUT** /entity/{id}/annotations2 | Update an Entity&#39;s annotations.
[**update_entity_file_handle**](EntityServicesApi.md#update_entity_file_handle) | **PUT** /entity/{id}/version/{versionNumber}/filehandle | Updates the filehandle.
[**update_entity_with_json**](EntityServicesApi.md#update_entity_with_json) | **PUT** /entity/{id}/json | Update the annotations of an entity using the raw JSON of the entity.


# **bind_json_schema_to_entity**
> JsonSchemaObjectBinding bind_json_schema_to_entity(id)

Bind a JSON schema to an Entity.

Bind a JSON schema to an Entity. The bound schema will be used to validate the Entity''s metadata (annotations). Any child Entity that does not have a bound schema will inherit the first bound schema found in its hierarchy.  Only a single schema can be bound to an Entity at a time. If you have more than one schema to bind to an Entity you will need to create and bind a single composition schema using keywords such as 'anyOf', 'allOf' or 'oneOf' that defines how the schemas should be used for validation.  Note: The caller must be granted the UPDATE ermission on the Entity to bind. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.bind_schema_to_entity_request import BindSchemaToEntityRequest
from synclient.model.json_schema_object_binding import JsonSchemaObjectBinding
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of an Entity.
    bind_schema_to_entity_request = BindSchemaToEntityRequest(
        entity_id="entity_id_example",
        schemaid="schemaid_example",
    ) # BindSchemaToEntityRequest | The request identifies the JSON schema to bind. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Bind a JSON schema to an Entity.
        api_response = api_instance.bind_json_schema_to_entity(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->bind_json_schema_to_entity: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Bind a JSON schema to an Entity.
        api_response = api_instance.bind_json_schema_to_entity(id, bind_schema_to_entity_request=bind_schema_to_entity_request)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->bind_json_schema_to_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. |
 **bind_schema_to_entity_request** | [**BindSchemaToEntityRequest**](BindSchemaToEntityRequest.md)| The request identifies the JSON schema to bind. | [optional]

### Return type

[**JsonSchemaObjectBinding**](JsonSchemaObjectBinding.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_entity_data_type**
> DataTypeResponse change_entity_data_type(id, type)

Change the.

Change the <a href=\"${org.sagebionetworks.repo.model.DataType}\" >DataType</a> of the given entity. The entity's DataType controls how the entity can be accessed. For example, an entity's DataType must be set to 'open_data' in order for anonymous to be allowed to access its contents.  <p>  Note: The caller must be a member of the 'Synapse Access and Compliance Team' (id=464532) in order to change an Entity's type to 'OPEN_DATA'. The caller must be granted UPDATED on the Entity to change the its type to any other value.  </p>' 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.data_type_response import DataTypeResponse
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of an Entity.
    type = "OPEN_DATA" # str | Type of data

    # example passing only required values which don't have defaults set
    try:
        # Change the.
        api_response = api_instance.change_entity_data_type(id, type)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->change_entity_data_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. |
 **type** | **str**| Type of data |

### Return type

[**DataTypeResponse**](DataTypeResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_bound_schema**
> clear_bound_schema(id)

Clear the bound JSON schema from this Entity.

Clear the bound JSON schema from this Entity. The schema will no longer be used to validate this Entity or its children.  Note: The caller must be granted the DELETE permission on the Entity. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of an Entity.

    # example passing only required values which don't have defaults set
    try:
        # Clear the bound JSON schema from this Entity.
        api_instance.clear_bound_schema(id)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->clear_bound_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource has been deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_entity**
> Entity create_entity()

Create a new Entity.

Create a new Entity. This method is used to create Projects, Folders, FileEntities and Records (coming soon). The passed request body should contain the following fields:  <ul>  <li>name - Give your new entity a Name. <b>Note:</b> A name must be unique within the given parent, similar to a file in a folder.</li>  <li>parentId - The ID of the parent Entity, such as a Folder or Project. This field should be excluded when creating a Project.</li>  <li>concreteType - Indicates the type of Entity to create. The value should be one of the following: org.sagebionetworks.repo.model.Project, org.sagebionetworks.repo.model.Folder, or org.sagebionetworks.repo.model.FileEntity</li>  </ul>  <p>  Note: To create an Entity the caller must be granted the <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.CREATE</a> on the parent Entity. Any authenticated caller can create a new Project (with parentId=null).  </p>  <p>  <b>Service Limits</b>  <table border=\"1\">  <tr>  <th>resource</th>  <th>limit</th>  </tr>  <tr>  <td>The maximum number of children for a single parent entity</td>  <td>10 K</td>  </tr>  </table>  </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.entity import Entity
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    generated_by = "generatedBy_example" # str | To track the Provenance of an Entity create, include the ID of the <a href=\"${org.sagebionetworks.repo.model.provenance.Activity}\">Activity</a> that was created to track the change. For more information see: <a href=\"${POST.activity}\">POST /activity</a>. You must be the creator of the <a href=\"${org.sagebionetworks.repo.model.provenance.Activity}\">Activity</a> used here.'  (optional)
    entity = Entity(
        concrete_type="concrete_type_example",
        created_by="created_by_example",
        created_on="created_on_example",
        description="description_example",
        etag="etag_example",
        id="id_example",
        modified_by="modified_by_example",
        modified_on="modified_on_example",
        name="NNR(Mx.EO9uf3y+FjLWeL",
        parent_id="parent_id_example",
    ) # Entity |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new Entity.
        api_response = api_instance.create_entity(generated_by=generated_by, entity=entity)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->create_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generated_by** | **str**| To track the Provenance of an Entity create, include the ID of the &lt;a href&#x3D;\&quot;${org.sagebionetworks.repo.model.provenance.Activity}\&quot;&gt;Activity&lt;/a&gt; that was created to track the change. For more information see: &lt;a href&#x3D;\&quot;${POST.activity}\&quot;&gt;POST /activity&lt;/a&gt;. You must be the creator of the &lt;a href&#x3D;\&quot;${org.sagebionetworks.repo.model.provenance.Activity}\&quot;&gt;Activity&lt;/a&gt; used here.&#39;  | [optional]
 **entity** | [**Entity**](Entity.md)|  | [optional]

### Return type

[**Entity**](Entity.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_entity_acl**
> AccessControlList create_entity_acl(id)

Create a new Access Control List (ACL), overriding inheritance.

Create a new Access Control List (ACL), overriding inheritance.  <p> By default, Entities such as FileEntity and Folder inherit their permission from their containing Project. For such Entities the Project is the Entity's 'benefactor'. This permission inheritance can be overridden by creating an ACL for the Entity. When this occurs the Entity becomes its own benefactor and all permission are determined by its own ACL.  </p>  <p>  If the ACL of an Entity is deleted, then its benefactor will automatically be set to its parent's benefactor.  </p>  <p>  Note: The caller must be granted  <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.CHANGE_PERMISSIONS</a> on the Entity to call this method.  </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.access_control_list import AccessControlList
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of an Entity.
    access_control_list = AccessControlList(
        created_by="created_by_example",
        creation_date="creation_date_example",
        etag="etag_example",
        id="id_example",
        modified_by="modified_by_example",
        modified_on="modified_on_example",
        resource_access=[
            ResourceAccess(
                access_type=[
                    ACCESSTYPE("CREATE"),
                ],
                principal_id=1,
            ),
        ],
    ) # AccessControlList |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new Access Control List (ACL), overriding inheritance.
        api_response = api_instance.create_entity_acl(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->create_entity_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new Access Control List (ACL), overriding inheritance.
        api_response = api_instance.create_entity_acl(id, access_control_list=access_control_list)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->create_entity_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. |
 **access_control_list** | [**AccessControlList**](AccessControlList.md)|  | [optional]

### Return type

[**AccessControlList**](AccessControlList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_activity**
> delete_activity(id)

Deletes the activity relationship for the current version of an Entity.

Deletes the activity relationship for the current version of an Entity. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of an Entity.
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletes the activity relationship for the current version of an Entity.
        api_instance.delete_activity(id)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->delete_activity: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletes the activity relationship for the current version of an Entity.
        api_instance.delete_activity(id, body=body)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->delete_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | This resource has been deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_entity**
> delete_entity(id)

Deletes an Entity

Moves an entity in the trash can, if the skipTrashCan is set to true will flag the entity for purge and it will be deleted as soon as possible.  <p>  Note: To delete an Entity the caller must be granted the  <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.DELETE</a> on the Entity.  </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of an Entity.
    skip_trash_can = True # bool | If true the entity will be flag for priority purge and deleted as soon as possible  (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletes an Entity
        api_instance.delete_entity(id)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->delete_entity: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletes an Entity
        api_instance.delete_entity(id, skip_trash_can=skip_trash_can, body=body)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->delete_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. |
 **skip_trash_can** | **bool**| If true the entity will be flag for priority purge and deleted as soon as possible  | [optional]
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource has been deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_entity_acl**
> delete_entity_acl(id)

Delete the Access Control List (ACL) for a given Entity.

Delete the Access Control List (ACL) for a given Entity.  <p>  By default, Entities such as FileEntity and Folder inherit their permission from their containing Project. For such Entities the Project is the Entity's 'benefactor'. This permission inheritance can be overridden by creating an ACL for the Entity. When this occurs the Entity becomes its own benefactor and all permission are determined by its own ACL.  </p>  <p>  If the ACL of an Entity is deleted, then its benefactor will automatically be set to its parent''s benefactor. The ACL for a Project cannot be deleted.  </p>  <p>  Note: The caller must be granted <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.CHANGE_PERMISSIONS</a> on the Entity to call this method.  </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of an Entity.
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete the Access Control List (ACL) for a given Entity.
        api_instance.delete_entity_acl(id)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->delete_entity_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete the Access Control List (ACL) for a given Entity.
        api_instance.delete_entity_acl(id, body=body)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->delete_entity_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | This resource has been deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_entity_version**
> delete_entity_version(id, version_number)

Delete a specific version of a FileEntity.

Delete a specific version of a FileEntity.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of the Entity
    version_number = 1 # int | The version number of the Entity.
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a specific version of a FileEntity.
        api_instance.delete_entity_version(id, version_number)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->delete_entity_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a specific version of a FileEntity.
        api_instance.delete_entity_version(id, version_number, body=body)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->delete_entity_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Entity |
 **version_number** | **int**| The version number of the Entity. |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource has been deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_preview_redirect_url_for_version**
> str file_preview_redirect_url_for_version(id, version_number)

Get the URL of the preview file associated with a specific version of a FileEntity. 

Get the URL of the preview file associated with a specific version of a FileEntity.  Note: This call will result in a HTTP temporary redirect (307), to the actual file URL if the caller meets all of the download requirements. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of the Entity.
    version_number = 1 # int | The version number of the Entity.
    redirect = True # bool | When set to false, the URL will be returned as text/plain instead of redirecting.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the URL of the preview file associated with a specific version of a FileEntity. 
        api_response = api_instance.file_preview_redirect_url_for_version(id, version_number)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->file_preview_redirect_url_for_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the URL of the preview file associated with a specific version of a FileEntity. 
        api_response = api_instance.file_preview_redirect_url_for_version(id, version_number, redirect=redirect)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->file_preview_redirect_url_for_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Entity. |
 **version_number** | **int**| The version number of the Entity. |
 **redirect** | **bool**| When set to false, the URL will be returned as text/plain instead of redirecting.  | [optional]

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity**
> Activity get_activity(id)

Get an existing activity for the current version of an Entity.

Get an existing activity for the current version of an Entity.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.activity import Activity
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of an Entity.
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Get an existing activity for the current version of an Entity. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get an existing activity for the current version of an Entity.
        api_response = api_instance.get_activity(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_activity: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get an existing activity for the current version of an Entity.
        api_response = api_instance.get_activity(id, body=body)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Get an existing activity for the current version of an Entity. | [optional]

### Return type

[**Activity**](Activity.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity_for_entity_version**
> Activity get_activity_for_entity_version(id, version_number)

Get an existing activity for a specific version of an Entity.

Get an existing activity for a specific version of an Entity.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.activity import Activity
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of the Entity.
    version_number = 1 # int | The version number of the Entity.
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Get an existing activity for a specific version of an Entity. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get an existing activity for a specific version of an Entity.
        api_response = api_instance.get_activity_for_entity_version(id, version_number)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_activity_for_entity_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get an existing activity for a specific version of an Entity.
        api_response = api_instance.get_activity_for_entity_version(id, version_number, body=body)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_activity_for_entity_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Entity. |
 **version_number** | **int**| The version number of the Entity. |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Get an existing activity for a specific version of an Entity. | [optional]

### Return type

[**Activity**](Activity.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_versions_of_entity**
> PaginatedResultsOfVersionInfo get_all_versions_of_entity(id)

Get all versions of an Entity one page at a time.

Get all versions of an Entity one page at a time.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.paginated_results_of_version_info import PaginatedResultsOfVersionInfo
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of the Entity.
    limit = 10 # int | Limits the number of entities that will be fetched for this page. When null it will default to 10.  (optional) if omitted the server will use the default value of 10
    offset = 0 # int | The offset index determines where this page will start from. When null it will default to 0.  (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # Get all versions of an Entity one page at a time.
        api_response = api_instance.get_all_versions_of_entity(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_all_versions_of_entity: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all versions of an Entity one page at a time.
        api_response = api_instance.get_all_versions_of_entity(id, limit=limit, offset=offset)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_all_versions_of_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Entity. |
 **limit** | **int**| Limits the number of entities that will be fetched for this page. When null it will default to 10.  | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| The offset index determines where this page will start from. When null it will default to 0.  | [optional] if omitted the server will use the default value of 0

### Return type

[**PaginatedResultsOfVersionInfo**](PaginatedResultsOfVersionInfo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bound_json_schema**
> JsonSchemaObjectBinding get_bound_json_schema(id)

Get information about a JSON schema bound to an Entity.

Get information about a JSON schema bound to an Entity. Note: Any child Entity that does not have a bound schema will inherit the first bound schema found in its hierarchy.  Note: The caller must be granted the READ permission on the Entity. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.json_schema_object_binding import JsonSchemaObjectBinding
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of an Entity.

    # example passing only required values which don't have defaults set
    try:
        # Get information about a JSON schema bound to an Entity.
        api_response = api_instance.get_bound_json_schema(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_bound_json_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. |

### Return type

[**JsonSchemaObjectBinding**](JsonSchemaObjectBinding.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_children**
> EntityChildrenResponse get_children()

Get a page of children for a given parent ID.

Get a page of children for a given parent ID. This service can also be used to list projects by setting the parentId to NULL in EntityChildrenRequest. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.entity_children_response import EntityChildrenResponse
from synclient.model.entity_children_request import EntityChildrenRequest
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    entity_children_request = EntityChildrenRequest(
        include_sum_file_sizes=False,
        include_total_child_count=False,
        include_types=[
            EntityType("project"),
        ],
        next_page_token="next_page_token_example",
        parent_id="parent_id_example",
        sort_by=SortBy("NAME"),
        sort_direction=SortDirection("ASC"),
    ) # EntityChildrenRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a page of children for a given parent ID.
        api_response = api_instance.get_children(entity_children_request=entity_children_request)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_children: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_children_request** | [**EntityChildrenRequest**](EntityChildrenRequest.md)|  | [optional]

### Return type

[**EntityChildrenResponse**](EntityChildrenResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity**
> Entity get_entity(id)

Get an Entity

Get an Entity using its ID.  <p> Note: To get an Entity the caller must be granted the <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\" >ACCESS_TYPE.READ</a> on the Entity.  </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.entity import Entity
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of an Entity.

    # example passing only required values which don't have defaults set
    try:
        # Get an Entity
        api_response = api_instance.get_entity(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. |

### Return type

[**Entity**](Entity.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_acl**
> AccessControlList get_entity_acl(id)

Get the Access Control List (ACL) for a given entity.

Get the Access Control List (ACL) for a given entity.  <p> Note: If this method is called on an Entity that is inheriting its permission from another Entity a NOT_FOUND (404) response will be generated. The error response message will include the Entity''s benefactor ID. </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.access_control_list import AccessControlList
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of an Entity.

    # example passing only required values which don't have defaults set
    try:
        # Get the Access Control List (ACL) for a given entity.
        api_response = api_instance.get_entity_acl(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_entity_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. |

### Return type

[**AccessControlList**](AccessControlList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_annotations**
> AnnotationsV2 get_entity_annotations(id)

Get the annotations for an entity.

Get the annotations for an entity.  <p>  Note: The caller must be granted the <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\" >ACCESS_TYPE.READ</a> on the Entity, to get its annotations.  </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.annotations_v2 import AnnotationsV2
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of an Entity.

    # example passing only required values which don't have defaults set
    try:
        # Get the annotations for an entity.
        api_response = api_instance.get_entity_annotations(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_entity_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. |

### Return type

[**AnnotationsV2**](AnnotationsV2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_annotations_v2_for_version**
> AnnotationsV2 get_entity_annotations_v2_for_version(id, version_number)

Get an Entity's annotations for a specific version of a FileEntity.

Get an Entity's annotations for a specific version of a FileEntity.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.annotations_v2 import AnnotationsV2
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of the Entity.
    version_number = 1 # int | The version number of the Entity.

    # example passing only required values which don't have defaults set
    try:
        # Get an Entity's annotations for a specific version of a FileEntity.
        api_response = api_instance.get_entity_annotations_v2_for_version(id, version_number)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_entity_annotations_v2_for_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Entity. |
 **version_number** | **int**| The version number of the Entity. |

### Return type

[**AnnotationsV2**](AnnotationsV2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_benefactor**
> EntityHeader get_entity_benefactor(id)

Get an Entity's benefactor.

Get an Entity's benefactor.  <p>  The term 'benefactor' is used indicate which Entity an Entity inherits is ACL from. For example, a newly created Project will have its own ACL and therefore, it will be its own benefactor. A Folder will inherit its ACL (by default) from its containing Project so the Project will be the Folder's benefactor. This method will return the EntityHeader of an Entity's benefactor. </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.entity_header import EntityHeader
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of an Entity.
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get an Entity's benefactor.
        api_response = api_instance.get_entity_benefactor(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_entity_benefactor: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get an Entity's benefactor.
        api_response = api_instance.get_entity_benefactor(id, body=body)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_entity_benefactor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

[**EntityHeader**](EntityHeader.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_file_handles**
> FileHandleResults get_entity_file_handles(id)

Get the FileHandles of the file currently associated with the current version of the Entity. 

Get the FileHandles of the file currently associated with the current version of the Entity.  <p> If a preview exists for the file then the handle of the preview and the file will be returned with this call. </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.file_handle_results import FileHandleResults
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of a File Entity.

    # example passing only required values which don't have defaults set
    try:
        # Get the FileHandles of the file currently associated with the current version of the Entity. 
        api_response = api_instance.get_entity_file_handles(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_entity_file_handles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of a File Entity. |

### Return type

[**FileHandleResults**](FileHandleResults.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_file_handles_for_version**
> FileHandleResults get_entity_file_handles_for_version(id, version_number)

Get the FileHandles of the file associated with a specific version of a FileEntity. 

Get the FileHandles of the file associated with a specific version of a FileEntity.  If a preview exists for the file then the handle of the preview and the file will be returned with this call. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.file_handle_results import FileHandleResults
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of the Entity.
    version_number = 1 # int | The version number of the Entity.

    # example passing only required values which don't have defaults set
    try:
        # Get the FileHandles of the file associated with a specific version of a FileEntity. 
        api_response = api_instance.get_entity_file_handles_for_version(id, version_number)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_entity_file_handles_for_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Entity. |
 **version_number** | **int**| The version number of the Entity. |

### Return type

[**FileHandleResults**](FileHandleResults.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_for_version**
> Entity get_entity_for_version(id, version_number)

Get a specific version of an Entity.

Get a specific version of an Entity.  Note: Only the current version of the Entity can be used for an Entity update. Therefore, only the current version of the Entity will be returned with the actual etag. All older versions will be returned with an eTag '00000000-0000-0000-0000-000000000000'. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.entity import Entity
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of the Entity
    version_number = 1 # int | The version number of the Entity.

    # example passing only required values which don't have defaults set
    try:
        # Get a specific version of an Entity.
        api_response = api_instance.get_entity_for_version(id, version_number)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_entity_for_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Entity |
 **version_number** | **int**| The version number of the Entity. |

### Return type

[**Entity**](Entity.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_header_by_md5**
> PaginatedResultsOfEntityHeader get_entity_header_by_md5(md5)

Gets FileEntities matching the given MD5 string which the user has read access to. 

Gets at most 200 FileEntities matching the given MD5 string which the user has read access to. NOTE: Another option is to create a file view that includes MD5 values. https://docs.synapse.org/articles/views.html 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.paginated_results_of_entity_header import PaginatedResultsOfEntityHeader
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    md5 = "md5_example" # str | File MD5
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets FileEntities matching the given MD5 string which the user has read access to. 
        api_response = api_instance.get_entity_header_by_md5(md5)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_entity_header_by_md5: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets FileEntities matching the given MD5 string which the user has read access to. 
        api_response = api_instance.get_entity_header_by_md5(md5, body=body)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_entity_header_by_md5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **md5** | **str**| File MD5 |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

[**PaginatedResultsOfEntityHeader**](PaginatedResultsOfEntityHeader.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_id_by_alias**
> EntityId get_entity_id_by_alias(alias)

Lookup an Entity ID using an alias.

Lookup an Entity ID using an alias.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.entity_id import EntityId
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    alias = "alias_example" # str | Alias of an Entity

    # example passing only required values which don't have defaults set
    try:
        # Lookup an Entity ID using an alias.
        api_response = api_instance.get_entity_id_by_alias(alias)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_entity_id_by_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Alias of an Entity |

### Return type

[**EntityId**](EntityId.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_json**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_entity_json(id)

Get the raw JSON for the given entity.

Get the raw JSON for the given entity. The resulting JSON can be used for the validation of a entity against a <a href=\"${org.sagebionetworks.repo.model.schema.JsonSchema}\">JsonSchema</a>.  <p>  Note: The caller must be granted the <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\" >ACCESS_TYPE.READ</a> permission on the Entity.  </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of an Entity.

    # example passing only required values which don't have defaults set
    try:
        # Get the raw JSON for the given entity.
        api_response = api_instance.get_entity_json(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_entity_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_path**
> EntityPath get_entity_path(id)

Get the full path of an Entity as a List of EntityHeaders.

Get the full path of an Entity as a List of EntityHeaders. The first EntityHeader will be the Root Entity, and the last EntityHeader will be the requested Entity. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.entity_path import EntityPath
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of an Entity.

    # example passing only required values which don't have defaults set
    try:
        # Get the full path of an Entity as a List of EntityHeaders.
        api_response = api_instance.get_entity_path(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_entity_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. |

### Return type

[**EntityPath**](EntityPath.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_schema_validation_results**
> ValidationResults get_entity_schema_validation_results(id)

Get the validation results of an Entity against its bound JSON schema.

Get the validation results of an Entity against its bound JSON schema. The validation of an Entity against its bound schema is automatic and eventually consistent. The validation results include the etag of the Entity at the time of the last validation. If the returned etag does not match the current etag of the Entity then the results should be considered out-of-date. If an Entity has not been validated for the first time, or if the Entity does not have a bound schema, this method will return a 404 (not-found). Keep checking for the latest validation results.  Note: The caller must be granted the READ permission on the Entity. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.validation_results import ValidationResults
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of the Entity.

    # example passing only required values which don't have defaults set
    try:
        # Get the validation results of an Entity against its bound JSON schema.
        api_response = api_instance.get_entity_schema_validation_results(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_entity_schema_validation_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Entity. |

### Return type

[**ValidationResults**](ValidationResults.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_schema_validation_statistics**
> ValidationSummaryStatistics get_entity_schema_validation_statistics(id)

Get the summary statistics of the JSON schema validation results for a single container Entity such as a Project or Folder. 

Get the The summary statistics of the JSON schema validation results for a single container Entity such as a Project or Folder. Only direct children of the container are included in the results. The statistics include the total number of children in the container, and the counts for both the invalid and valid children. If an Entity has not been validated for the first time, or it does not have bound schema it will be counted as 'unknown'.  The validation of an Entity against its bound schema is automatic and eventually consistent. Keep checking this method to get the latest validation statistics for the given container.  Note: The caller must be granted the READ permission on the container Entity. The resulting statistics will only include children that the caller has the READ permission on. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.validation_summary_statistics import ValidationSummaryStatistics
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of the container Entity.

    # example passing only required values which don't have defaults set
    try:
        # Get the summary statistics of the JSON schema validation results for a single container Entity such as a Project or Folder. 
        api_response = api_instance.get_entity_schema_validation_statistics(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_entity_schema_validation_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the container Entity. |

### Return type

[**ValidationSummaryStatistics**](ValidationSummaryStatistics.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_type**
> EntityHeader get_entity_type(id)

Get the EntityHeader of an Entity given its ID.

Get the EntityHeader of an Entity given its ID. The EntityHeader is a light weight object with basic information about an Entity includes its type. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.entity_header import EntityHeader
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of the Entity.
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the EntityHeader of an Entity given its ID.
        api_response = api_instance.get_entity_type(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_entity_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the EntityHeader of an Entity given its ID.
        api_response = api_instance.get_entity_type(id, body=body)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_entity_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Entity. |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

[**EntityHeader**](EntityHeader.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_type_batch**
> PaginatedResultsOfEntityHeader get_entity_type_batch(batch)

Get a batch of EntityHeader given multile Entity IDs.

Get a batch of EntityHeader given multile Entity IDs. The EntityHeader is a light weight object with basic information about an Entity includes its type. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.paginated_results_of_entity_header import PaginatedResultsOfEntityHeader
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    batch = "batch_example" # str | A comma separated list of Entity IDs to get EntityHeaders for. 

    # example passing only required values which don't have defaults set
    try:
        # Get a batch of EntityHeader given multile Entity IDs.
        api_response = api_instance.get_entity_type_batch(batch)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_entity_type_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch** | **str**| A comma separated list of Entity IDs to get EntityHeaders for.  |

### Return type

[**PaginatedResultsOfEntityHeader**](PaginatedResultsOfEntityHeader.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_versioned_type_batch**
> PaginatedResultsOfEntityHeader get_entity_versioned_type_batch()

Get the EntityHeader for a list of references with a POST.

Get the EntityHeader for a list of references with a POST. If any item in the batch fails (e.g., with a 404) it will be EXCLUDED in the result set. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.paginated_results_of_entity_header import PaginatedResultsOfEntityHeader
from synclient.model.reference_list import ReferenceList
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    reference_list = ReferenceList(
        references=[
            Reference(
                target_id="target_id_example",
                target_version_number=3.14,
            ),
        ],
    ) # ReferenceList |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the EntityHeader for a list of references with a POST.
        api_response = api_instance.get_entity_versioned_type_batch(reference_list=reference_list)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_entity_versioned_type_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_list** | [**ReferenceList**](ReferenceList.md)|  | [optional]

### Return type

[**PaginatedResultsOfEntityHeader**](PaginatedResultsOfEntityHeader.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_preview_url**
> str get_file_preview_url(id)

Get the URL of the preview file associated with the current version of a FileEntity. 

Get the URL of the preview file associated with the current version of a FileEntity.  <p> Note: This call will result in a HTTP temporary redirect (307), to the actual file URL if the caller meets all of the download requirements. </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of a File Entity.
    redirect = True # bool | When set to false, the URL will be returned as text/plain instead of redirecting.  (optional)
    status = 1 # int | Status (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the URL of the preview file associated with the current version of a FileEntity. 
        api_response = api_instance.get_file_preview_url(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_file_preview_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the URL of the preview file associated with the current version of a FileEntity. 
        api_response = api_instance.get_file_preview_url(id, redirect=redirect, status=status)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_file_preview_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of a File Entity. |
 **redirect** | **bool**| When set to false, the URL will be returned as text/plain instead of redirecting.  | [optional]
 **status** | **int**| Status | [optional]

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invalid_validation_results**
> ListValidationResultsResponse get_invalid_validation_results(id)

Get a single page of invalid JSON schema validation results for a container Entity (Project or Folder). 

Get a single page of invalid JSON schema validation results for a container Entity (Project or Folder). The validation of an Entity against its bound schema is automatic and eventually consistent. The validation results include the etag of the Entity at the time of the last validation. If the returned etag does not match the current etag of the Entity then the results should be considered out-of-date.  Note: The caller must be granted the READ permission on the container Entity. The results will only include children that the caller has the READ permission on. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.list_validation_results_response import ListValidationResultsResponse
from synclient.model.list_validation_results_request import ListValidationResultsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of the container Entity.
    list_validation_results_request = ListValidationResultsRequest(
        container_id="container_id_example",
        next_page_token="next_page_token_example",
    ) # ListValidationResultsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a single page of invalid JSON schema validation results for a container Entity (Project or Folder). 
        api_response = api_instance.get_invalid_validation_results(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_invalid_validation_results: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a single page of invalid JSON schema validation results for a container Entity (Project or Folder). 
        api_response = api_instance.get_invalid_validation_results(id, list_validation_results_request=list_validation_results_request)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_invalid_validation_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the container Entity. |
 **list_validation_results_request** | [**ListValidationResultsRequest**](ListValidationResultsRequest.md)|  | [optional]

### Return type

[**ListValidationResultsResponse**](ListValidationResultsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_temporary_credentials_for_entity**
> StsCredentials get_temporary_credentials_for_entity(id, permission)

Gets the temporary S3 credentials from STS for the given entity.

Gets the temporary S3 credentials from STS for the given entity. These credentials are only good for the bucket and base key specified by the returned credentials and expire 12 hours after this API is called.  The specified entity must be a folder with an STS-enabled storage location. If that storage location is external storage, you may request read-only or read-write permissions. If that storage location is Synapse storage, you must request read-only permissions. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.sts_credentials import StsCredentials
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of the Folder with an STS-enabled storage location. 
    permission = "read_only" # str | Read-only or read-write permissions. 

    # example passing only required values which don't have defaults set
    try:
        # Gets the temporary S3 credentials from STS for the given entity.
        api_response = api_instance.get_temporary_credentials_for_entity(id, permission)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_temporary_credentials_for_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Folder with an STS-enabled storage location.  |
 **permission** | **str**| Read-only or read-write permissions.  |

### Return type

[**StsCredentials**](StsCredentials.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_entity_permissions**
> UserEntityPermissions get_user_entity_permissions(id)

Get the list of permission that the caller has on a given Entity.

Get the list of permission that the caller has on a given Entity.  A User's permission on an Entity is a calculation based several factors including the permission granted by the Entity's ACL and the User's group membership. There might also be extra requirement for an Entity, such as special terms-of-use or special restrictions for sensitive data. This means a client cannot accurately calculate a User's permission on an Entity simply by inspecting the Entity''s ACL. Instead, all clients should use this method to get the calculated permission a User has on an Entity. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.user_entity_permissions import UserEntityPermissions
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of an Entity.

    # example passing only required values which don't have defaults set
    try:
        # Get the list of permission that the caller has on a given Entity.
        api_response = api_instance.get_user_entity_permissions(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->get_user_entity_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. |

### Return type

[**UserEntityPermissions**](UserEntityPermissions.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **has_access**
> BooleanResult has_access(id)

Determine if the caller have a given permission on a given Entity.

Determine if the caller have a given permission on a given Entity.  <p>  A User's permission on an Entity is a calculation based several factors including the permission granted by the Entity's ACL and the User's group membership. There might also be extra requirement for an Entity, such as special terms-of-use or special restrictions for sensitive data. This means a client cannot accurately calculate a User's permission on an Entity simply by inspecting the Entity's ACL. Instead, all clients should use this method to get the calculated permission a User has on an Entity. </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.boolean_result import BooleanResult
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of an Entity.
    access_type = "accessType_example" # str | The permission to check. Must be from:  <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE</a>'  (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Determine if the caller have a given permission on a given Entity.
        api_response = api_instance.has_access(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->has_access: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Determine if the caller have a given permission on a given Entity.
        api_response = api_instance.has_access(id, access_type=access_type, body=body)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->has_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. |
 **access_type** | **str**| The permission to check. Must be from:  &lt;a href&#x3D;\&quot;${org.sagebionetworks.repo.model.ACCESS_TYPE}\&quot;&gt;ACCESS_TYPE&lt;/a&gt;&#39;  | [optional]
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

[**BooleanResult**](BooleanResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lookup_child**
> EntityId lookup_child()

Retrieve an entityId for a given parent ID and entity name.

Retrieve an entityId for a given parent ID and entity name. This service can also be used to lookup projectId by setting the parentId to NULL in EntityLookupRequest. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.entity_id import EntityId
from synclient.model.entity_lookup_request import EntityLookupRequest
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    entity_lookup_request = EntityLookupRequest(
        entity_name="entity_name_example",
        parent_id="parent_id_example",
    ) # EntityLookupRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve an entityId for a given parent ID and entity name.
        api_response = api_instance.lookup_child(entity_lookup_request=entity_lookup_request)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->lookup_child: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_lookup_request** | [**EntityLookupRequest**](EntityLookupRequest.md)|  | [optional]

### Return type

[**EntityId**](EntityId.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_activity_for_entity**
> Activity update_activity_for_entity(id, generated_by)

Sets the generatedBy relationship for the current version of an Entity.

Sets the generatedBy relationship for the current version of an Entity.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.activity import Activity
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of an Entity.
    generated_by = "generatedBy_example" # str | The id of the activity to connect to the entity. You must be the creator of the <a href=\"${org.sagebionetworks.repo.model.provenance.Activity}\">Activity</a> used here.' 
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Sets the generatedBy relationship for the current version of an Entity. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Sets the generatedBy relationship for the current version of an Entity.
        api_response = api_instance.update_activity_for_entity(id, generated_by)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->update_activity_for_entity: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Sets the generatedBy relationship for the current version of an Entity.
        api_response = api_instance.update_activity_for_entity(id, generated_by, body=body)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->update_activity_for_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. |
 **generated_by** | **str**| The id of the activity to connect to the entity. You must be the creator of the &lt;a href&#x3D;\&quot;${org.sagebionetworks.repo.model.provenance.Activity}\&quot;&gt;Activity&lt;/a&gt; used here.&#39;  |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Sets the generatedBy relationship for the current version of an Entity. | [optional]

### Return type

[**Activity**](Activity.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entity**
> Entity update_entity(id)

Update an entity.

Update an entity.  <p>  If the Entity is a FileEntity and the dataFileHandleId fields is set to a new value, then a new version will automatically be created for this update if the MD5 of the new file handle does not match the MD5 of the existing file handle or if the file handles do not have an MD5 set. You can also force the creation of a new version using the newVersion parameter  (see below).  </p>  <p>  Synapse employs an Optimistic Concurrency Control (OCC) scheme to handle concurrent updates. Each time an Entity is updated a new etag will be issued to the Entity. When an update is request, Synapse will compare the etag of the passed Entity with the current etag of the Entity. If the etags do not match, then the update will be rejected with a PRECONDITION_FAILED (412) response. When this occurs the caller should get the latest copy of the Entity (see: <a href=\"${GET.entity.id}\">GET /entity/{id}</a>) and re-apply any changes to the object, then re-attempt the Entity update. This ensure the caller has any changes applied by other users before applying their own changes.  </p>  <p>  Note: To update an Entity the caller must be granted the <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.UPDATE</a> on the Entity.  </p>  <p>  <b>Service Limits</b>  <table border=\"1\">  <tr>  <th>resource</th>  <th>limit</th>  </tr>  <tr>  <td>The maximum number of children for a single parent entity</td>  <td>10 K</td>  </tr>  </table>  </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.entity import Entity
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of an Entity.
    generated_by = "generatedBy_example" # str | To track the Provenance of an Entity update, include the ID of the <a href=\"${org.sagebionetworks.repo.model.provenance.Activity}\">Activity</a> that was created to track the change. For more information see: <a href=\"${POST.activity}\">POST /activity</a>. You must be the creator of the <a href=\"${org.sagebionetworks.repo.model.provenance.Activity}\">Activity</a> used here.'  (optional)
    new_version = "newVersion_example" # str | To force the creation of a new version for a <a href=\"${org.sagebionetworks.repo.model.VersionableEntity}\">versionable</a> entity such as a <a href= \"${org.sagebionetworks.repo.model.FileEntity}\">FileEntity</a>, include this optional parameter with a value set to true (i.e. newVersion=true). This parameter is ignored for entities of type  <a href=\"${org.sagebionetworks.repo.model.table.Table}\">Table</a> (See <a href=\"${POST.entity.id.table.snapshot}\">POST /entity/{id}/table/snapshot</a> instead)  (optional)
    entity = Entity(
        concrete_type="concrete_type_example",
        created_by="created_by_example",
        created_on="created_on_example",
        description="description_example",
        etag="etag_example",
        id="id_example",
        modified_by="modified_by_example",
        modified_on="modified_on_example",
        name="NNR(Mx.EO9uf3y+FjLWeL",
        parent_id="parent_id_example",
    ) # Entity |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an entity.
        api_response = api_instance.update_entity(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->update_entity: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an entity.
        api_response = api_instance.update_entity(id, generated_by=generated_by, new_version=new_version, entity=entity)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->update_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. |
 **generated_by** | **str**| To track the Provenance of an Entity update, include the ID of the &lt;a href&#x3D;\&quot;${org.sagebionetworks.repo.model.provenance.Activity}\&quot;&gt;Activity&lt;/a&gt; that was created to track the change. For more information see: &lt;a href&#x3D;\&quot;${POST.activity}\&quot;&gt;POST /activity&lt;/a&gt;. You must be the creator of the &lt;a href&#x3D;\&quot;${org.sagebionetworks.repo.model.provenance.Activity}\&quot;&gt;Activity&lt;/a&gt; used here.&#39;  | [optional]
 **new_version** | **str**| To force the creation of a new version for a &lt;a href&#x3D;\&quot;${org.sagebionetworks.repo.model.VersionableEntity}\&quot;&gt;versionable&lt;/a&gt; entity such as a &lt;a href&#x3D; \&quot;${org.sagebionetworks.repo.model.FileEntity}\&quot;&gt;FileEntity&lt;/a&gt;, include this optional parameter with a value set to true (i.e. newVersion&#x3D;true). This parameter is ignored for entities of type  &lt;a href&#x3D;\&quot;${org.sagebionetworks.repo.model.table.Table}\&quot;&gt;Table&lt;/a&gt; (See &lt;a href&#x3D;\&quot;${POST.entity.id.table.snapshot}\&quot;&gt;POST /entity/{id}/table/snapshot&lt;/a&gt; instead)  | [optional]
 **entity** | [**Entity**](Entity.md)|  | [optional]

### Return type

[**Entity**](Entity.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entity_acl**
> AccessControlList update_entity_acl(id)

Update an Entity's ACL.

Update an Entity's ACL.  <p>  Note: The caller must be granted  <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.CHANGE_PERMISSIONS</a> on the Entity to call this method.  </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.access_control_list import AccessControlList
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of an Entity.
    access_control_list = AccessControlList(
        created_by="created_by_example",
        creation_date="creation_date_example",
        etag="etag_example",
        id="id_example",
        modified_by="modified_by_example",
        modified_on="modified_on_example",
        resource_access=[
            ResourceAccess(
                access_type=[
                    ACCESSTYPE("CREATE"),
                ],
                principal_id=1,
            ),
        ],
    ) # AccessControlList |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an Entity's ACL.
        api_response = api_instance.update_entity_acl(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->update_entity_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an Entity's ACL.
        api_response = api_instance.update_entity_acl(id, access_control_list=access_control_list)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->update_entity_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. |
 **access_control_list** | [**AccessControlList**](AccessControlList.md)|  | [optional]

### Return type

[**AccessControlList**](AccessControlList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entity_annotations**
> AnnotationsV2 update_entity_annotations(id)

Update an Entity's annotations.

Update an Entity's annotations.  <p>  Note: The caller must be granted the <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.UPDATE</a> on the Entity, to update its annotations. </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.annotations_v2 import AnnotationsV2
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of an Entity.
    annotations_v2 = AnnotationsV2(
        annotations={
            "key": AnnotationsValue(
                type=AnnotationsValueType("STRING"),
                value=[
                    "value_example",
                ],
            ),
        },
        etag="etag_example",
        id="id_example",
    ) # AnnotationsV2 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an Entity's annotations.
        api_response = api_instance.update_entity_annotations(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->update_entity_annotations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an Entity's annotations.
        api_response = api_instance.update_entity_annotations(id, annotations_v2=annotations_v2)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->update_entity_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. |
 **annotations_v2** | [**AnnotationsV2**](AnnotationsV2.md)|  | [optional]

### Return type

[**AnnotationsV2**](AnnotationsV2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entity_file_handle**
> str update_entity_file_handle(id, version_number)

Updates the filehandle.

Updates the FileHandle associated with the FileEntity with the provided entity id and version. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from synclient.model.file_handle_update_request import FileHandleUpdateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of the Entity.
    version_number = 1 # int | The version number of the Entity.
    file_handle_update_request = FileHandleUpdateRequest(
        new_file_handle_id="new_file_handle_id_example",
        old_file_handle_id="old_file_handle_id_example",
    ) # FileHandleUpdateRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates the filehandle.
        api_response = api_instance.update_entity_file_handle(id, version_number)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->update_entity_file_handle: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates the filehandle.
        api_response = api_instance.update_entity_file_handle(id, version_number, file_handle_update_request=file_handle_update_request)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->update_entity_file_handle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Entity. |
 **version_number** | **int**| The version number of the Entity. |
 **file_handle_update_request** | [**FileHandleUpdateRequest**](FileHandleUpdateRequest.md)|  | [optional]

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entity_with_json**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_entity_with_json(id)

Update the annotations of an entity using the raw JSON of the entity.

Update the annotations of an entity using the raw JSON of the entity.  <p>  See: <a href=\"${GET.entity.id.json}\">GET entity/{id}/json</a> to get the JSON of an entity.  </p>  <p> Note: The caller must be granted the <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\" >ACCESS_TYPE.UPDATE and ACCESS_TYPE.READ</a> permission on the Entity. </p>' 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import entity_services_api
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entity_services_api.EntityServicesApi(api_client)
    id = "id_example" # str | The ID of an Entity.
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the annotations of an entity using the raw JSON of the entity.
        api_response = api_instance.update_entity_with_json(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->update_entity_with_json: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the annotations of an entity using the raw JSON of the entity.
        api_response = api_instance.update_entity_with_json(id, body=body)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EntityServicesApi->update_entity_with_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

