# synclient.AccessRequirementServicesApi

All URIs are relative to *https://repo-prod.prod.sagebase.org/repo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_lock_access_requirement**](AccessRequirementServicesApi.md#create_lock_access_requirement) | **POST** /entity/{id}/lockAccessRequirement | Add a temporary access restriction that prevents access pending review by the Synapse ACT. 
[**get_entity_access_requirements**](AccessRequirementServicesApi.md#get_entity_access_requirements) | **GET** /entity/{id}/accessRequirement | Retrieve paginated list of ALL Access Requirements associated with an entity.
[**get_team_access_requirements**](AccessRequirementServicesApi.md#get_team_access_requirements) | **GET** /team/{id}/accessRequirement | Retrieve paginated list of ALL Access Requirements associated with a Team.


# **create_lock_access_requirement**
> AccessRequirement create_lock_access_requirement(id)

Add a temporary access restriction that prevents access pending review by the Synapse ACT. 

Add a temporary access restriction that prevents access pending review by the Synapse Access and Compliance Team. This service may be used only by an administrator of the specified entity. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import synclient
from synclient.rest import ApiException
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
    api_instance = synclient.AccessRequirementServicesApi(api_client)
    id = 'id_example' # str | The ID of an Entity.

    try:
        # Add a temporary access restriction that prevents access pending review by the Synapse ACT. 
        api_response = api_instance.create_lock_access_requirement(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccessRequirementServicesApi->create_lock_access_requirement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. | 

### Return type

[**AccessRequirement**](AccessRequirement.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_access_requirements**
> PaginatedResultsOfAccessRequirement get_entity_access_requirements(id, limit=limit, offset=offset)

Retrieve paginated list of ALL Access Requirements associated with an entity.

Retrieve paginated list of ALL Access Requirements associated with an entity. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import synclient
from synclient.rest import ApiException
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
    api_instance = synclient.AccessRequirementServicesApi(api_client)
    id = 'id_example' # str | The ID of an Entity.
limit = 56 # int | Limits the size of the page returned. For example, a page size of 10 require limit = 10. The maximum limit for this call is 50.  (optional)
offset = 56 # int | The index of the pagination offset. For a page size of 10, the first page would be at offset = 0, and the second page would be at offset = 10.  (optional)

    try:
        # Retrieve paginated list of ALL Access Requirements associated with an entity.
        api_response = api_instance.get_entity_access_requirements(id, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccessRequirementServicesApi->get_entity_access_requirements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. | 
 **limit** | **int**| Limits the size of the page returned. For example, a page size of 10 require limit &#x3D; 10. The maximum limit for this call is 50.  | [optional] 
 **offset** | **int**| The index of the pagination offset. For a page size of 10, the first page would be at offset &#x3D; 0, and the second page would be at offset &#x3D; 10.  | [optional] 

### Return type

[**PaginatedResultsOfAccessRequirement**](PaginatedResultsOfAccessRequirement.md)

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

# **get_team_access_requirements**
> PaginatedResultsOfAccessRequirement get_team_access_requirements(id, limit=limit, offset=offset)

Retrieve paginated list of ALL Access Requirements associated with a Team.

Retrieve paginated list of ALL Access Requirements associated with a Team. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import synclient
from synclient.rest import ApiException
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
    api_instance = synclient.AccessRequirementServicesApi(api_client)
    id = 'id_example' # str | the ID of the Team.
limit = 10 # int | Limits the size of the page returned. For example, a page size of 10 require limit = 10. The maximum limit for this call is 50.  (optional) (default to 10)
offset = 0 # int | The index of the pagination offset. For a page size of 10, the first page would be at offset = 0, and the second page would be at offset = 10.  (optional) (default to 0)

    try:
        # Retrieve paginated list of ALL Access Requirements associated with a Team.
        api_response = api_instance.get_team_access_requirements(id, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccessRequirementServicesApi->get_team_access_requirements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID of the Team. | 
 **limit** | **int**| Limits the size of the page returned. For example, a page size of 10 require limit &#x3D; 10. The maximum limit for this call is 50.  | [optional] [default to 10]
 **offset** | **int**| The index of the pagination offset. For a page size of 10, the first page would be at offset &#x3D; 0, and the second page would be at offset &#x3D; 10.  | [optional] [default to 0]

### Return type

[**PaginatedResultsOfAccessRequirement**](PaginatedResultsOfAccessRequirement.md)

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

