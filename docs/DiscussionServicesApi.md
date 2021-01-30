# synclient.DiscussionServicesApi

All URIs are relative to *https://repo-prod.prod.sagebase.org/repo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_threads_for_entity**](DiscussionServicesApi.md#get_threads_for_entity) | **GET** /entity/{id}/threads | This API is used to get N number of threads that belongs to projects user can view and references the given entity. 


# **get_threads_for_entity**
> PaginatedResultsOfDiscussionThreadBundle get_threads_for_entity(id, ascending=ascending, limit=limit, offset=offset, sort=sort)

This API is used to get N number of threads that belongs to projects user can view and references the given entity. 

This API is used to get N number of threads that belongs to projects user can view and references the given entity.  Target users: anyone who has READ permission to the entity. 

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
    api_instance = synclient.DiscussionServicesApi(api_client)
    id = 'id_example' # str | The ID of an Entity.
ascending = True # bool | The direction of sort: true for ascending, and false for descending (optional)
limit = 10 # float | Limits the size of the page returned. For example, a page size of 10 require limit = 10. The maximum Limit for this call is 20.'  (optional) (default to 10)
offset = 0 # float | The index of the pagination offset. For a page size of 10, the first page would be at offset = 0, and the second page would be at offset = 10.'  (optional) (default to 0)
sort = 'sort_example' # str | The field to sort the resulting threads on. Available options DiscussionThreadOrder  (optional)

    try:
        # This API is used to get N number of threads that belongs to projects user can view and references the given entity. 
        api_response = api_instance.get_threads_for_entity(id, ascending=ascending, limit=limit, offset=offset, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_threads_for_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. | 
 **ascending** | **bool**| The direction of sort: true for ascending, and false for descending | [optional] 
 **limit** | **float**| Limits the size of the page returned. For example, a page size of 10 require limit &#x3D; 10. The maximum Limit for this call is 20.&#39;  | [optional] [default to 10]
 **offset** | **float**| The index of the pagination offset. For a page size of 10, the first page would be at offset &#x3D; 0, and the second page would be at offset &#x3D; 10.&#39;  | [optional] [default to 0]
 **sort** | **str**| The field to sort the resulting threads on. Available options DiscussionThreadOrder  | [optional] 

### Return type

[**PaginatedResultsOfDiscussionThreadBundle**](PaginatedResultsOfDiscussionThreadBundle.md)

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

