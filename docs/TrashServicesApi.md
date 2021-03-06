# synclient.TrashServicesApi

All URIs are relative to *https://repo-prod.prod.sagebase.org/repo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**flag_for_purge**](TrashServicesApi.md#flag_for_purge) | **PUT** /trashcan/purge/{id} | Flags the specified entity for priority purge.
[**move_to_trash**](TrashServicesApi.md#move_to_trash) | **PUT** /trashcan/trash/{id} | Moves an entity and its descendants to the trash can.
[**restore_from_trash**](TrashServicesApi.md#restore_from_trash) | **PUT** /trashcan/restore/{id} | Moves an entity and its descendants out of the trash can back to its original parent. 
[**restore_from_trash_to_parent**](TrashServicesApi.md#restore_from_trash_to_parent) | **PUT** /trashcan/restore/{id}/{parentId} | Moves an entity and its descendants out of the trash can to a new parent.
[**view_trash**](TrashServicesApi.md#view_trash) | **GET** /trashcan/view | Retrieves the paginated list of trash entities deleted by the current user.


# **flag_for_purge**
> str flag_for_purge(id)

Flags the specified entity for priority purge.

Flags the specified entity for priority purge. The entity will be deleted as soon as possible. Once purging is done, the entity will be permanently deleted from the system. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import trash_services_api
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
    api_instance = trash_services_api.TrashServicesApi(api_client)
    id = "id_example" # str | The ID of an entity.
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Flags the specified entity for priority purge.
        api_response = api_instance.flag_for_purge(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TrashServicesApi->flag_for_purge: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Flags the specified entity for priority purge.
        api_response = api_instance.flag_for_purge(id, body=body)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TrashServicesApi->flag_for_purge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an entity. |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

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

# **move_to_trash**
> str move_to_trash(id)

Moves an entity and its descendants to the trash can.

Moves an entity and its descendants to the trash can.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import trash_services_api
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
    api_instance = trash_services_api.TrashServicesApi(api_client)
    id = "id_example" # str | The ID of an entity.
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Moves an entity and its descendants to the trash can.
        api_response = api_instance.move_to_trash(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TrashServicesApi->move_to_trash: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Moves an entity and its descendants to the trash can.
        api_response = api_instance.move_to_trash(id, body=body)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TrashServicesApi->move_to_trash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an entity. |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

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

# **restore_from_trash**
> str restore_from_trash(id)

Moves an entity and its descendants out of the trash can back to its original parent. 

Moves an entity and its descendants out of the trash can back to its original parent. An exception is thrown if the original parent does not exist any more. In that case, please use <a href=\"#operation/restoreFromTrash\">PUT /trashcan/restored/{id}/{parentId}</a> to restore to a new parent.  In such a case you must be a member of the Synapse Access and Compliance Team. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import trash_services_api
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
    api_instance = trash_services_api.TrashServicesApi(api_client)
    id = "id_example" # str | The ID of an entity.
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Moves an entity and its descendants out of the trash can back to its original parent. 
        api_response = api_instance.restore_from_trash(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TrashServicesApi->restore_from_trash: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Moves an entity and its descendants out of the trash can back to its original parent. 
        api_response = api_instance.restore_from_trash(id, body=body)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TrashServicesApi->restore_from_trash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an entity. |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

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

# **restore_from_trash_to_parent**
> str restore_from_trash_to_parent(id, parent_id)

Moves an entity and its descendants out of the trash can to a new parent.

Moves an entity and its descendants out of the trash can to a new parent.  NOTE:  This operation cannot be completed if the original parent has been deleted (unless the caller is a member of the Synapse Access and Compliance Team). The service will return a NotFoundException.  This is because of the potential security hole arising from allowing access requirements on folders:  If an entity is in a restricted folder and then deleted, it cannot be restored unless the new parent has the same restriction level as the original one. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import trash_services_api
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
    api_instance = trash_services_api.TrashServicesApi(api_client)
    id = "id_example" # str | The ID of a deleted entity.
    parent_id = "parentId_example" # str | The ID of the new parent entity.
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Moves an entity and its descendants out of the trash can to a new parent.
        api_response = api_instance.restore_from_trash_to_parent(id, parent_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TrashServicesApi->restore_from_trash_to_parent: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Moves an entity and its descendants out of the trash can to a new parent.
        api_response = api_instance.restore_from_trash_to_parent(id, parent_id, body=body)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TrashServicesApi->restore_from_trash_to_parent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of a deleted entity. |
 **parent_id** | **str**| The ID of the new parent entity. |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

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

# **view_trash**
> PaginatedResultsOfTrashedEntity view_trash()

Retrieves the paginated list of trash entities deleted by the current user.

Retrieves the paginated list of trash entities deleted by the current user. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import trash_services_api
from synclient.model.paginated_results_of_trashed_entity import PaginatedResultsOfTrashedEntity
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
    api_instance = trash_services_api.TrashServicesApi(api_client)
    limit = 10 # int | The maximum number of entities to retrieve per page. (optional) if omitted the server will use the default value of 10
    offset = 0 # int | Paginated results. Offset to the current page. (optional) if omitted the server will use the default value of 0
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieves the paginated list of trash entities deleted by the current user.
        api_response = api_instance.view_trash(limit=limit, offset=offset, body=body)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TrashServicesApi->view_trash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of entities to retrieve per page. | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| Paginated results. Offset to the current page. | [optional] if omitted the server will use the default value of 0
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

[**PaginatedResultsOfTrashedEntity**](PaginatedResultsOfTrashedEntity.md)

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

