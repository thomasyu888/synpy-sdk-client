# synclient.DiscussionServicesApi

All URIs are relative to *https://repo-prod.prod.sagebase.org/repo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_thread**](DiscussionServicesApi.md#create_thread) | **POST** /thread | Create a new thread in a forum.
[**delete_thread**](DiscussionServicesApi.md#delete_thread) | **DELETE** /thread/{threadId} | Delete a Thread.
[**get_replies_for_thread**](DiscussionServicesApi.md#get_replies_for_thread) | **GET** /thread/{threadId}/replies | Get N number of replies for a given thread ID.
[**get_reply_count_for_thread**](DiscussionServicesApi.md#get_reply_count_for_thread) | **GET** /thread/{threadId}/replycount | Get the total number of replies for a given Thread. 
[**get_thread**](DiscussionServicesApi.md#get_thread) | **GET** /thread/{threadId} | Get a thread.
[**get_thread_counts**](DiscussionServicesApi.md#get_thread_counts) | **POST** /entity/threadcounts | Get number of threads that belong to projects user can view and references the given entity. 
[**get_thread_url**](DiscussionServicesApi.md#get_thread_url) | **GET** /thread/messageUrl | Get the message URL of a thread.
[**get_threads_for_entity**](DiscussionServicesApi.md#get_threads_for_entity) | **GET** /entity/{id}/threads | This API is used to get N number of threads that belongs to projects user can view and references the given entity. 
[**pin_thread**](DiscussionServicesApi.md#pin_thread) | **PUT** /thread/{threadId}/pin | Pin a Thread.
[**restore_deleted_thread**](DiscussionServicesApi.md#restore_deleted_thread) | **PUT** /thread/{threadId}/restore | Restore a deleted thread.
[**unpin_thread**](DiscussionServicesApi.md#unpin_thread) | **PUT** /thread/{threadId}/unpin | Unpin a thread.
[**update_thread_message**](DiscussionServicesApi.md#update_thread_message) | **PUT** /thread/{threadId}/message | Update the message of a thread.
[**update_thread_title**](DiscussionServicesApi.md#update_thread_title) | **PUT** /thread/{threadId}/title | Update the title of a Thread.


# **create_thread**
> DiscussionThreadBundle create_thread(create_discussion_thread=create_discussion_thread)

Create a new thread in a forum.

This API is used to create a new thread in a forum.  Target users: anyone who has READ permission to the project. 

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
configuration = synclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synclient.DiscussionServicesApi(api_client)
    create_discussion_thread = synclient.CreateDiscussionThread() # CreateDiscussionThread |  (optional)

    try:
        # Create a new thread in a forum.
        api_response = api_instance.create_thread(create_discussion_thread=create_discussion_thread)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DiscussionServicesApi->create_thread: %s\n" % e)
```

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

# Configure HTTP basic authorization: basicAuth
configuration = synclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synclient.DiscussionServicesApi(api_client)
    create_discussion_thread = synclient.CreateDiscussionThread() # CreateDiscussionThread |  (optional)

    try:
        # Create a new thread in a forum.
        api_response = api_instance.create_thread(create_discussion_thread=create_discussion_thread)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DiscussionServicesApi->create_thread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_discussion_thread** | [**CreateDiscussionThread**](CreateDiscussionThread.md)|  | [optional] 

### Return type

[**DiscussionThreadBundle**](DiscussionThreadBundle.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_thread**
> delete_thread(thread_id)

Delete a Thread.

This API is used to mark a thread as deleted.  Target users: only forum's moderator can mark a thread as deleted. 

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
configuration = synclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synclient.DiscussionServicesApi(api_client)
    thread_id = 'thread_id_example' # str | The ID of a thread.

    try:
        # Delete a Thread.
        api_instance.delete_thread(thread_id)
    except ApiException as e:
        print("Exception when calling DiscussionServicesApi->delete_thread: %s\n" % e)
```

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

# Configure HTTP basic authorization: basicAuth
configuration = synclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synclient.DiscussionServicesApi(api_client)
    thread_id = 'thread_id_example' # str | The ID of a thread.

    try:
        # Delete a Thread.
        api_instance.delete_thread(thread_id)
    except ApiException as e:
        print("Exception when calling DiscussionServicesApi->delete_thread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| The ID of a thread. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource has been deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_replies_for_thread**
> PaginatedResultsOfDiscussionReplyBundle get_replies_for_thread(thread_id, filter, ascending=ascending, limit=limit, offset=offset, sort=sort)

Get N number of replies for a given thread ID.

This API is used to get N number of replies for a given thread ID.  Target users: anyone who has READ permission to the project. 

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
configuration = synclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synclient.DiscussionServicesApi(api_client)
    thread_id = 'thread_id_example' # str | The ID of a thread.
filter = 'filter_example' # str | Filter deleted not deleted replies.
ascending = True # bool | The direction of sort: true for ascending, and false for descending (optional)
limit = 10 # int | Limits the size of the page returned. For example, a page size of 10 require limit = 10.  (optional) (default to 10)
offset = 0 # int | The index of the pagination offset. For a page size of 10, the first page would be at offset = 0, and the second page would be at offset = 10.'  (optional) (default to 0)
sort = 'sort_example' # str | The field to sort the resulting replies on.  (optional)

    try:
        # Get N number of replies for a given thread ID.
        api_response = api_instance.get_replies_for_thread(thread_id, filter, ascending=ascending, limit=limit, offset=offset, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_replies_for_thread: %s\n" % e)
```

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

# Configure HTTP basic authorization: basicAuth
configuration = synclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synclient.DiscussionServicesApi(api_client)
    thread_id = 'thread_id_example' # str | The ID of a thread.
filter = 'filter_example' # str | Filter deleted not deleted replies.
ascending = True # bool | The direction of sort: true for ascending, and false for descending (optional)
limit = 10 # int | Limits the size of the page returned. For example, a page size of 10 require limit = 10.  (optional) (default to 10)
offset = 0 # int | The index of the pagination offset. For a page size of 10, the first page would be at offset = 0, and the second page would be at offset = 10.'  (optional) (default to 0)
sort = 'sort_example' # str | The field to sort the resulting replies on.  (optional)

    try:
        # Get N number of replies for a given thread ID.
        api_response = api_instance.get_replies_for_thread(thread_id, filter, ascending=ascending, limit=limit, offset=offset, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_replies_for_thread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| The ID of a thread. | 
 **filter** | **str**| Filter deleted not deleted replies. | 
 **ascending** | **bool**| The direction of sort: true for ascending, and false for descending | [optional] 
 **limit** | **int**| Limits the size of the page returned. For example, a page size of 10 require limit &#x3D; 10.  | [optional] [default to 10]
 **offset** | **int**| The index of the pagination offset. For a page size of 10, the first page would be at offset &#x3D; 0, and the second page would be at offset &#x3D; 10.&#39;  | [optional] [default to 0]
 **sort** | **str**| The field to sort the resulting replies on.  | [optional] 

### Return type

[**PaginatedResultsOfDiscussionReplyBundle**](PaginatedResultsOfDiscussionReplyBundle.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reply_count_for_thread**
> ReplyCount get_reply_count_for_thread(thread_id, filter)

Get the total number of replies for a given Thread. 

This API is used to get the total number of replies for a given thread ID.  Target users: anyone who has READ permission to the project.' 

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
configuration = synclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synclient.DiscussionServicesApi(api_client)
    thread_id = 'thread_id_example' # str | The ID of a thread.
filter = 'filter_example' # str | Filter deleted not deleted replies.

    try:
        # Get the total number of replies for a given Thread. 
        api_response = api_instance.get_reply_count_for_thread(thread_id, filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_reply_count_for_thread: %s\n" % e)
```

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

# Configure HTTP basic authorization: basicAuth
configuration = synclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synclient.DiscussionServicesApi(api_client)
    thread_id = 'thread_id_example' # str | The ID of a thread.
filter = 'filter_example' # str | Filter deleted not deleted replies.

    try:
        # Get the total number of replies for a given Thread. 
        api_response = api_instance.get_reply_count_for_thread(thread_id, filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_reply_count_for_thread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| The ID of a thread. | 
 **filter** | **str**| Filter deleted not deleted replies. | 

### Return type

[**ReplyCount**](ReplyCount.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_thread**
> DiscussionThreadBundle get_thread(thread_id)

Get a thread.

This API is used to get a thread and its statistic given its ID.  Target users: anyone who has READ permission to the project. 

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
configuration = synclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synclient.DiscussionServicesApi(api_client)
    thread_id = 'thread_id_example' # str | The ID of a thread.

    try:
        # Get a thread.
        api_response = api_instance.get_thread(thread_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_thread: %s\n" % e)
```

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

# Configure HTTP basic authorization: basicAuth
configuration = synclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synclient.DiscussionServicesApi(api_client)
    thread_id = 'thread_id_example' # str | The ID of a thread.

    try:
        # Get a thread.
        api_response = api_instance.get_thread(thread_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_thread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| The ID of a thread. | 

### Return type

[**DiscussionThreadBundle**](DiscussionThreadBundle.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_thread_counts**
> EntityThreadCounts get_thread_counts(entity_id_list=entity_id_list)

Get number of threads that belong to projects user can view and references the given entity. 

This API is used to get list of entity and count pairs, with count is the number of threads that belong to projects user can view and references the given entity.  Target users: anyone who has READ permission to the project. 

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
configuration = synclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synclient.DiscussionServicesApi(api_client)
    entity_id_list = synclient.EntityIdList() # EntityIdList | The requested list. Limit size 20. (optional)

    try:
        # Get number of threads that belong to projects user can view and references the given entity. 
        api_response = api_instance.get_thread_counts(entity_id_list=entity_id_list)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_thread_counts: %s\n" % e)
```

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

# Configure HTTP basic authorization: basicAuth
configuration = synclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synclient.DiscussionServicesApi(api_client)
    entity_id_list = synclient.EntityIdList() # EntityIdList | The requested list. Limit size 20. (optional)

    try:
        # Get number of threads that belong to projects user can view and references the given entity. 
        api_response = api_instance.get_thread_counts(entity_id_list=entity_id_list)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_thread_counts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id_list** | [**EntityIdList**](EntityIdList.md)| The requested list. Limit size 20. | [optional] 

### Return type

[**EntityThreadCounts**](EntityThreadCounts.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_thread_url**
> MessageURL get_thread_url(message_key)

Get the message URL of a thread.

This API is used to get the message URL of a thread. The message URL is the URL to download the file which contains the thread message.  Target users: anyone who has READ permission to the project.  The resulting URL will be signed with Content-Type =\"text/plain; charset=utf-8\"; therefore, this header must be included with the GET on the URL. 

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
configuration = synclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synclient.DiscussionServicesApi(api_client)
    message_key = 'message_key_example' # str | Message Key

    try:
        # Get the message URL of a thread.
        api_response = api_instance.get_thread_url(message_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_thread_url: %s\n" % e)
```

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

# Configure HTTP basic authorization: basicAuth
configuration = synclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synclient.DiscussionServicesApi(api_client)
    message_key = 'message_key_example' # str | Message Key

    try:
        # Get the message URL of a thread.
        api_response = api_instance.get_thread_url(message_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_thread_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_key** | **str**| Message Key | 

### Return type

[**MessageURL**](MessageURL.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threads_for_entity**
> PaginatedResultsOfDiscussionThreadBundle get_threads_for_entity(id, ascending=ascending, limit=limit, offset=offset, sort=sort)

This API is used to get N number of threads that belongs to projects user can view and references the given entity. 

This API is used to get N number of threads that belongs to projects user can view and references the given entity.  Target users: anyone who has READ permission to the entity. 

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
configuration = synclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

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

# Configure HTTP basic authorization: basicAuth
configuration = synclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

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

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pin_thread**
> pin_thread(thread_id)

Pin a Thread.

This API is used to mark a thread as pinned.  Target users: only forum's moderator can mark a thread as pinned. 

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
configuration = synclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synclient.DiscussionServicesApi(api_client)
    thread_id = 'thread_id_example' # str | The ID of a thread.

    try:
        # Pin a Thread.
        api_instance.pin_thread(thread_id)
    except ApiException as e:
        print("Exception when calling DiscussionServicesApi->pin_thread: %s\n" % e)
```

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

# Configure HTTP basic authorization: basicAuth
configuration = synclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synclient.DiscussionServicesApi(api_client)
    thread_id = 'thread_id_example' # str | The ID of a thread.

    try:
        # Pin a Thread.
        api_instance.pin_thread(thread_id)
    except ApiException as e:
        print("Exception when calling DiscussionServicesApi->pin_thread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| The ID of a thread. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_deleted_thread**
> str restore_deleted_thread(thread_id)

Restore a deleted thread.

This API is used to restore a deleted thread.  Target users: only forum's moderator can restore a deleted thread. 

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
configuration = synclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synclient.DiscussionServicesApi(api_client)
    thread_id = 'thread_id_example' # str | The ID of a thread.

    try:
        # Restore a deleted thread.
        api_response = api_instance.restore_deleted_thread(thread_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DiscussionServicesApi->restore_deleted_thread: %s\n" % e)
```

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

# Configure HTTP basic authorization: basicAuth
configuration = synclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synclient.DiscussionServicesApi(api_client)
    thread_id = 'thread_id_example' # str | The ID of a thread.

    try:
        # Restore a deleted thread.
        api_response = api_instance.restore_deleted_thread(thread_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DiscussionServicesApi->restore_deleted_thread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| The ID of a thread. | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpin_thread**
> unpin_thread(thread_id)

Unpin a thread.

This API is used to unpin a thread.  Target users: only forum's moderator can unpin a thread. 

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
configuration = synclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synclient.DiscussionServicesApi(api_client)
    thread_id = 'thread_id_example' # str | The ID of a thread.

    try:
        # Unpin a thread.
        api_instance.unpin_thread(thread_id)
    except ApiException as e:
        print("Exception when calling DiscussionServicesApi->unpin_thread: %s\n" % e)
```

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

# Configure HTTP basic authorization: basicAuth
configuration = synclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synclient.DiscussionServicesApi(api_client)
    thread_id = 'thread_id_example' # str | The ID of a thread.

    try:
        # Unpin a thread.
        api_instance.unpin_thread(thread_id)
    except ApiException as e:
        print("Exception when calling DiscussionServicesApi->unpin_thread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| The ID of a thread. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_thread_message**
> DiscussionThreadBundle update_thread_message(thread_id, update_thread_message=update_thread_message)

Update the message of a thread.

This API is used to update the message of a thread.  Target users: only the author of the thread can update its message.' 

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
configuration = synclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synclient.DiscussionServicesApi(api_client)
    thread_id = 'thread_id_example' # str | The ID of a thread.
update_thread_message = synclient.UpdateThreadMessage() # UpdateThreadMessage |  (optional)

    try:
        # Update the message of a thread.
        api_response = api_instance.update_thread_message(thread_id, update_thread_message=update_thread_message)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DiscussionServicesApi->update_thread_message: %s\n" % e)
```

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

# Configure HTTP basic authorization: basicAuth
configuration = synclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synclient.DiscussionServicesApi(api_client)
    thread_id = 'thread_id_example' # str | The ID of a thread.
update_thread_message = synclient.UpdateThreadMessage() # UpdateThreadMessage |  (optional)

    try:
        # Update the message of a thread.
        api_response = api_instance.update_thread_message(thread_id, update_thread_message=update_thread_message)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DiscussionServicesApi->update_thread_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| The ID of a thread. | 
 **update_thread_message** | [**UpdateThreadMessage**](UpdateThreadMessage.md)|  | [optional] 

### Return type

[**DiscussionThreadBundle**](DiscussionThreadBundle.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_thread_title**
> DiscussionThreadBundle update_thread_title(thread_id, update_thread_title=update_thread_title)

Update the title of a Thread.

This API is used to update the title of a thread.  Target users: only the author of the thread can update its title.' 

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
configuration = synclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synclient.DiscussionServicesApi(api_client)
    thread_id = 'thread_id_example' # str | The ID of a thread.
update_thread_title = synclient.UpdateThreadTitle() # UpdateThreadTitle |  (optional)

    try:
        # Update the title of a Thread.
        api_response = api_instance.update_thread_title(thread_id, update_thread_title=update_thread_title)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DiscussionServicesApi->update_thread_title: %s\n" % e)
```

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

# Configure HTTP basic authorization: basicAuth
configuration = synclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synclient.DiscussionServicesApi(api_client)
    thread_id = 'thread_id_example' # str | The ID of a thread.
update_thread_title = synclient.UpdateThreadTitle() # UpdateThreadTitle |  (optional)

    try:
        # Update the title of a Thread.
        api_response = api_instance.update_thread_title(thread_id, update_thread_title=update_thread_title)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DiscussionServicesApi->update_thread_title: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| The ID of a thread. | 
 **update_thread_title** | [**UpdateThreadTitle**](UpdateThreadTitle.md)|  | [optional] 

### Return type

[**DiscussionThreadBundle**](DiscussionThreadBundle.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

