# synclient.DiscussionServicesApi

All URIs are relative to *https://repo-prod.prod.sagebase.org/repo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_reply**](DiscussionServicesApi.md#create_reply) | **POST** /reply | Create a new reply to a thread.
[**create_thread**](DiscussionServicesApi.md#create_thread) | **POST** /thread | Create a new thread in a forum.
[**delete_reply**](DiscussionServicesApi.md#delete_reply) | **DELETE** /reply/{replyId} | Delete Reply
[**delete_thread**](DiscussionServicesApi.md#delete_thread) | **DELETE** /thread/{threadId} | Delete a Thread.
[**get_forum**](DiscussionServicesApi.md#get_forum) | **GET** /forum/{forumId} | Get a Forum. 
[**get_forum_by_project_id**](DiscussionServicesApi.md#get_forum_by_project_id) | **GET** /project/{projectId}/forum | Get the Forum of a Project.
[**get_forum_moderators**](DiscussionServicesApi.md#get_forum_moderators) | **GET** /forum/{forumId}/moderators | Returns a page of Forum moderators.
[**get_replies_for_thread**](DiscussionServicesApi.md#get_replies_for_thread) | **GET** /thread/{threadId}/replies | Get N number of replies for a given thread ID.
[**get_reply**](DiscussionServicesApi.md#get_reply) | **GET** /reply/{replyId} | Get a Reply.
[**get_reply_count_for_thread**](DiscussionServicesApi.md#get_reply_count_for_thread) | **GET** /thread/{threadId}/replycount | Get the total number of replies for a given Thread. 
[**get_reply_url**](DiscussionServicesApi.md#get_reply_url) | **GET** /reply/messageUrl | Get the message URL of a reply.
[**get_thread**](DiscussionServicesApi.md#get_thread) | **GET** /thread/{threadId} | Get a thread.
[**get_thread_count**](DiscussionServicesApi.md#get_thread_count) | **GET** /forum/{forumId}/threadcount | Get the total number of threads for a Forum.
[**get_thread_counts**](DiscussionServicesApi.md#get_thread_counts) | **POST** /entity/threadcounts | Get number of threads that belong to projects user can view and references the given entity. 
[**get_thread_url**](DiscussionServicesApi.md#get_thread_url) | **GET** /thread/messageUrl | Get the message URL of a thread.
[**get_threads**](DiscussionServicesApi.md#get_threads) | **GET** /forum/{forumId}/threads | Get N number of threads for a Forum.
[**get_threads_for_entity**](DiscussionServicesApi.md#get_threads_for_entity) | **GET** /entity/{id}/threads | This API is used to get N number of threads that belongs to projects user can view and references the given entity. 
[**pin_thread**](DiscussionServicesApi.md#pin_thread) | **PUT** /thread/{threadId}/pin | Pin a Thread.
[**restore_deleted_thread**](DiscussionServicesApi.md#restore_deleted_thread) | **PUT** /thread/{threadId}/restore | Restore a deleted thread.
[**unpin_thread**](DiscussionServicesApi.md#unpin_thread) | **PUT** /thread/{threadId}/unpin | Unpin a thread.
[**update_reply_message**](DiscussionServicesApi.md#update_reply_message) | **PUT** /reply/{replyId}/message | Update the message of a reply.
[**update_thread_message**](DiscussionServicesApi.md#update_thread_message) | **PUT** /thread/{threadId}/message | Update the message of a thread.
[**update_thread_title**](DiscussionServicesApi.md#update_thread_title) | **PUT** /thread/{threadId}/title | Update the title of a Thread.


# **create_reply**
> DiscussionReplyBundle create_reply()

Create a new reply to a thread.

This API is used to create a new reply to a thread.  Target users: anyone who has READ permission to the project. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import discussion_services_api
from synclient.model.create_discussion_reply import CreateDiscussionReply
from synclient.model.discussion_reply_bundle import DiscussionReplyBundle
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
    api_instance = discussion_services_api.DiscussionServicesApi(api_client)
    create_discussion_reply = CreateDiscussionReply(
        message_markdown="message_markdown_example",
        thread_id="thread_id_example",
    ) # CreateDiscussionReply | - This object contains information needed to create a reply. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new reply to a thread.
        api_response = api_instance.create_reply(create_discussion_reply=create_discussion_reply)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->create_reply: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_discussion_reply** | [**CreateDiscussionReply**](CreateDiscussionReply.md)| - This object contains information needed to create a reply. | [optional]

### Return type

[**DiscussionReplyBundle**](DiscussionReplyBundle.md)

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

# **create_thread**
> DiscussionThreadBundle create_thread()

Create a new thread in a forum.

This API is used to create a new thread in a forum.  Target users: anyone who has READ permission to the project. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import discussion_services_api
from synclient.model.create_discussion_thread import CreateDiscussionThread
from synclient.model.discussion_thread_bundle import DiscussionThreadBundle
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
    api_instance = discussion_services_api.DiscussionServicesApi(api_client)
    create_discussion_thread = CreateDiscussionThread(
        forum_id="forum_id_example",
        message_markdown="message_markdown_example",
        title="title_example",
    ) # CreateDiscussionThread |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new thread in a forum.
        api_response = api_instance.create_thread(create_discussion_thread=create_discussion_thread)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->create_thread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_discussion_thread** | [**CreateDiscussionThread**](CreateDiscussionThread.md)|  | [optional]

### Return type

[**DiscussionThreadBundle**](DiscussionThreadBundle.md)

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

# **delete_reply**
> delete_reply(reply_id)

Delete Reply

This API is used to mark a reply as deleted.  Target users: only forum's moderator can mark a reply as deleted. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import discussion_services_api
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
    api_instance = discussion_services_api.DiscussionServicesApi(api_client)
    reply_id = "replyId_example" # str | The ID of the Reply.

    # example passing only required values which don't have defaults set
    try:
        # Delete Reply
        api_instance.delete_reply(reply_id)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->delete_reply: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reply_id** | **str**| The ID of the Reply. |

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
**204** | This resource was deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_thread**
> delete_thread(thread_id)

Delete a Thread.

This API is used to mark a thread as deleted.  Target users: only forum's moderator can mark a thread as deleted. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import discussion_services_api
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
    api_instance = discussion_services_api.DiscussionServicesApi(api_client)
    thread_id = "threadId_example" # str | The ID of a thread.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Thread.
        api_instance.delete_thread(thread_id)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->delete_thread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| The ID of a thread. |

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
**204** | The resource has been deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forum**
> Forum get_forum(forum_id)

Get a Forum. 

This API is used to get the Forum''s metadata for a given its ID.  Target users: anyone who has READ permission to the project.' 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import discussion_services_api
from synclient.model.forum import Forum
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
    api_instance = discussion_services_api.DiscussionServicesApi(api_client)
    forum_id = "forumId_example" # str | The ID of the Forum.

    # example passing only required values which don't have defaults set
    try:
        # Get a Forum. 
        api_response = api_instance.get_forum(forum_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_forum: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forum_id** | **str**| The ID of the Forum. |

### Return type

[**Forum**](Forum.md)

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

# **get_forum_by_project_id**
> Forum get_forum_by_project_id(project_id)

Get the Forum of a Project.

This API is used to get the Forum's metadata for a given project ID.  Target users: anyone who has READ permission to the project.' 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import discussion_services_api
from synclient.model.forum import Forum
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
    api_instance = discussion_services_api.DiscussionServicesApi(api_client)
    project_id = "projectId_example" # str | The ID of a Project.

    # example passing only required values which don't have defaults set
    try:
        # Get the Forum of a Project.
        api_response = api_instance.get_forum_by_project_id(project_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_forum_by_project_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of a Project. |

### Return type

[**Forum**](Forum.md)

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

# **get_forum_moderators**
> PaginatedIds get_forum_moderators(forum_id)

Returns a page of Forum moderators.

Returns a page of moderators for a given forum ID.  Target users: anyone who has READ permission to the project. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import discussion_services_api
from synclient.model.paginated_ids import PaginatedIds
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
    api_instance = discussion_services_api.DiscussionServicesApi(api_client)
    forum_id = "forumId_example" # str | The ID of the Forum.
    limit = 10 # int | Limits the size of the page returned. (optional) if omitted the server will use the default value of 10
    offset = 0 # int | The index of the pagination offset. For a page size of 10, the first page would be at offset = 0, and the second page would be at offset = 10.'  (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # Returns a page of Forum moderators.
        api_response = api_instance.get_forum_moderators(forum_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_forum_moderators: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a page of Forum moderators.
        api_response = api_instance.get_forum_moderators(forum_id, limit=limit, offset=offset)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_forum_moderators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forum_id** | **str**| The ID of the Forum. |
 **limit** | **int**| Limits the size of the page returned. | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| The index of the pagination offset. For a page size of 10, the first page would be at offset &#x3D; 0, and the second page would be at offset &#x3D; 10.&#39;  | [optional] if omitted the server will use the default value of 0

### Return type

[**PaginatedIds**](PaginatedIds.md)

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

# **get_replies_for_thread**
> PaginatedResultsOfDiscussionReplyBundle get_replies_for_thread(thread_id, filter)

Get N number of replies for a given thread ID.

This API is used to get N number of replies for a given thread ID.  Target users: anyone who has READ permission to the project. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import discussion_services_api
from synclient.model.paginated_results_of_discussion_reply_bundle import PaginatedResultsOfDiscussionReplyBundle
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
    api_instance = discussion_services_api.DiscussionServicesApi(api_client)
    thread_id = "threadId_example" # str | The ID of a thread.
    filter = "DELETED_ONLY" # str | Filter deleted not deleted replies.
    ascending = True # bool | The direction of sort: true for ascending, and false for descending (optional)
    limit = 10 # int | Limits the size of the page returned. For example, a page size of 10 require limit = 10.  (optional) if omitted the server will use the default value of 10
    offset = 0 # int | The index of the pagination offset. For a page size of 10, the first page would be at offset = 0, and the second page would be at offset = 10.'  (optional) if omitted the server will use the default value of 0
    sort = "CREATED_ON" # str | The field to sort the resulting replies on.  (optional) if omitted the server will use the default value of "CREATED_ON"

    # example passing only required values which don't have defaults set
    try:
        # Get N number of replies for a given thread ID.
        api_response = api_instance.get_replies_for_thread(thread_id, filter)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_replies_for_thread: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get N number of replies for a given thread ID.
        api_response = api_instance.get_replies_for_thread(thread_id, filter, ascending=ascending, limit=limit, offset=offset, sort=sort)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_replies_for_thread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| The ID of a thread. |
 **filter** | **str**| Filter deleted not deleted replies. |
 **ascending** | **bool**| The direction of sort: true for ascending, and false for descending | [optional]
 **limit** | **int**| Limits the size of the page returned. For example, a page size of 10 require limit &#x3D; 10.  | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| The index of the pagination offset. For a page size of 10, the first page would be at offset &#x3D; 0, and the second page would be at offset &#x3D; 10.&#39;  | [optional] if omitted the server will use the default value of 0
 **sort** | **str**| The field to sort the resulting replies on.  | [optional] if omitted the server will use the default value of "CREATED_ON"

### Return type

[**PaginatedResultsOfDiscussionReplyBundle**](PaginatedResultsOfDiscussionReplyBundle.md)

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

# **get_reply**
> DiscussionReplyBundle get_reply(reply_id)

Get a Reply.

This API is used to get a reply and its statistic given its ID.  Target users: anyone who has READ permission to the project. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import discussion_services_api
from synclient.model.discussion_reply_bundle import DiscussionReplyBundle
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
    api_instance = discussion_services_api.DiscussionServicesApi(api_client)
    reply_id = "replyId_example" # str | The ID of the Reply.

    # example passing only required values which don't have defaults set
    try:
        # Get a Reply.
        api_response = api_instance.get_reply(reply_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_reply: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reply_id** | **str**| The ID of the Reply. |

### Return type

[**DiscussionReplyBundle**](DiscussionReplyBundle.md)

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

# **get_reply_count_for_thread**
> ReplyCount get_reply_count_for_thread(thread_id, filter)

Get the total number of replies for a given Thread. 

This API is used to get the total number of replies for a given thread ID.  Target users: anyone who has READ permission to the project.' 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import discussion_services_api
from synclient.model.reply_count import ReplyCount
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
    api_instance = discussion_services_api.DiscussionServicesApi(api_client)
    thread_id = "threadId_example" # str | The ID of a thread.
    filter = "DELETED_ONLY" # str | Filter deleted not deleted replies.

    # example passing only required values which don't have defaults set
    try:
        # Get the total number of replies for a given Thread. 
        api_response = api_instance.get_reply_count_for_thread(thread_id, filter)
        pprint(api_response)
    except synclient.ApiException as e:
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

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reply_url**
> MessageURL get_reply_url(message_key)

Get the message URL of a reply.

This API is used to get the message URL of a reply. The message URL is the URL to download the file which contains the reply message.  Target users: anyone who has READ permission to the project. The resulting URL will be signed with Content-Type =\"text/plain; charset=utf-8\"; therefore, this header must be included with the GET on the URL. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import discussion_services_api
from synclient.model.message_url import MessageURL
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
    api_instance = discussion_services_api.DiscussionServicesApi(api_client)
    message_key = "messageKey_example" # str | DiscussionReplyBundle.messageKey

    # example passing only required values which don't have defaults set
    try:
        # Get the message URL of a reply.
        api_response = api_instance.get_reply_url(message_key)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_reply_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_key** | **str**| DiscussionReplyBundle.messageKey |

### Return type

[**MessageURL**](MessageURL.md)

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

# **get_thread**
> DiscussionThreadBundle get_thread(thread_id)

Get a thread.

This API is used to get a thread and its statistic given its ID.  Target users: anyone who has READ permission to the project. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import discussion_services_api
from synclient.model.discussion_thread_bundle import DiscussionThreadBundle
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
    api_instance = discussion_services_api.DiscussionServicesApi(api_client)
    thread_id = "threadId_example" # str | The ID of a thread.

    # example passing only required values which don't have defaults set
    try:
        # Get a thread.
        api_response = api_instance.get_thread(thread_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_thread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| The ID of a thread. |

### Return type

[**DiscussionThreadBundle**](DiscussionThreadBundle.md)

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

# **get_thread_count**
> ThreadCount get_thread_count(forum_id)

Get the total number of threads for a Forum.

This API is used to get the total number of threads for a given forum ID.  Target users: anyone who has READ permission to the project. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import discussion_services_api
from synclient.model.thread_count import ThreadCount
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
    api_instance = discussion_services_api.DiscussionServicesApi(api_client)
    forum_id = "forumId_example" # str | The ID of the Forum.
    filter = "DELETED_ONLY" # str | Filter deleted or not deleted threads. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the total number of threads for a Forum.
        api_response = api_instance.get_thread_count(forum_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_thread_count: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the total number of threads for a Forum.
        api_response = api_instance.get_thread_count(forum_id, filter=filter)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_thread_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forum_id** | **str**| The ID of the Forum. |
 **filter** | **str**| Filter deleted or not deleted threads. | [optional]

### Return type

[**ThreadCount**](ThreadCount.md)

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

# **get_thread_counts**
> EntityThreadCounts get_thread_counts()

Get number of threads that belong to projects user can view and references the given entity. 

This API is used to get list of entity and count pairs, with count is the number of threads that belong to projects user can view and references the given entity.  Target users: anyone who has READ permission to the project. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import discussion_services_api
from synclient.model.entity_id_list import EntityIdList
from synclient.model.entity_thread_counts import EntityThreadCounts
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
    api_instance = discussion_services_api.DiscussionServicesApi(api_client)
    entity_id_list = EntityIdList(
        id_list=[
            "id_list_example",
        ],
    ) # EntityIdList | The requested list. Limit size 20. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get number of threads that belong to projects user can view and references the given entity. 
        api_response = api_instance.get_thread_counts(entity_id_list=entity_id_list)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_thread_counts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id_list** | [**EntityIdList**](EntityIdList.md)| The requested list. Limit size 20. | [optional]

### Return type

[**EntityThreadCounts**](EntityThreadCounts.md)

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

# **get_thread_url**
> MessageURL get_thread_url(message_key)

Get the message URL of a thread.

This API is used to get the message URL of a thread. The message URL is the URL to download the file which contains the thread message.  Target users: anyone who has READ permission to the project.  The resulting URL will be signed with Content-Type =\"text/plain; charset=utf-8\"; therefore, this header must be included with the GET on the URL. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import discussion_services_api
from synclient.model.message_url import MessageURL
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
    api_instance = discussion_services_api.DiscussionServicesApi(api_client)
    message_key = "messageKey_example" # str | Message Key

    # example passing only required values which don't have defaults set
    try:
        # Get the message URL of a thread.
        api_response = api_instance.get_thread_url(message_key)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_thread_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_key** | **str**| Message Key |

### Return type

[**MessageURL**](MessageURL.md)

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

# **get_threads**
> PaginatedResultsOfDiscussionThreadBundle get_threads(forum_id)

Get N number of threads for a Forum.

This API is used to get N number of threads for a given forum ID.  Target users: anyone who has READ permission to the project.' 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import discussion_services_api
from synclient.model.paginated_results_of_discussion_thread_bundle import PaginatedResultsOfDiscussionThreadBundle
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
    api_instance = discussion_services_api.DiscussionServicesApi(api_client)
    forum_id = "forumId_example" # str | The ID of a Forum.
    ascending = True # bool | The direction of sort: true for ascending, and false for descending (optional)
    filter = "DELETED_ONLY" # str | Filter deleted or not deleted threads. (optional)
    limit = 10 # int | Limits the size of the page returned. For example, a page size of 10 require limit = 10.  (optional) if omitted the server will use the default value of 10
    offset = 0 # float | - The index of the pagination offset. For a page size of 10, the first page would be at offset = 0, and the second page would be at offset = 10. (optional) if omitted the server will use the default value of 0
    sort = "NUMBER_OF_REPLIES" # str | The field to sort the resulting threads on. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get N number of threads for a Forum.
        api_response = api_instance.get_threads(forum_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_threads: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get N number of threads for a Forum.
        api_response = api_instance.get_threads(forum_id, ascending=ascending, filter=filter, limit=limit, offset=offset, sort=sort)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_threads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forum_id** | **str**| The ID of a Forum. |
 **ascending** | **bool**| The direction of sort: true for ascending, and false for descending | [optional]
 **filter** | **str**| Filter deleted or not deleted threads. | [optional]
 **limit** | **int**| Limits the size of the page returned. For example, a page size of 10 require limit &#x3D; 10.  | [optional] if omitted the server will use the default value of 10
 **offset** | **float**| - The index of the pagination offset. For a page size of 10, the first page would be at offset &#x3D; 0, and the second page would be at offset &#x3D; 10. | [optional] if omitted the server will use the default value of 0
 **sort** | **str**| The field to sort the resulting threads on. | [optional]

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

# **get_threads_for_entity**
> PaginatedResultsOfDiscussionThreadBundle get_threads_for_entity(id)

This API is used to get N number of threads that belongs to projects user can view and references the given entity. 

This API is used to get N number of threads that belongs to projects user can view and references the given entity.  Target users: anyone who has READ permission to the entity. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import discussion_services_api
from synclient.model.paginated_results_of_discussion_thread_bundle import PaginatedResultsOfDiscussionThreadBundle
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
    api_instance = discussion_services_api.DiscussionServicesApi(api_client)
    id = "id_example" # str | The ID of an Entity.
    ascending = True # bool | The direction of sort: true for ascending, and false for descending (optional)
    limit = 10 # float | Limits the size of the page returned. For example, a page size of 10 require limit = 10. The maximum Limit for this call is 20.'  (optional) if omitted the server will use the default value of 10
    offset = 0 # float | The index of the pagination offset. For a page size of 10, the first page would be at offset = 0, and the second page would be at offset = 10.'  (optional) if omitted the server will use the default value of 0
    sort = "NUMBER_OF_REPLIES" # str | The field to sort the resulting threads on. Available options DiscussionThreadOrder  (optional)

    # example passing only required values which don't have defaults set
    try:
        # This API is used to get N number of threads that belongs to projects user can view and references the given entity. 
        api_response = api_instance.get_threads_for_entity(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_threads_for_entity: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # This API is used to get N number of threads that belongs to projects user can view and references the given entity. 
        api_response = api_instance.get_threads_for_entity(id, ascending=ascending, limit=limit, offset=offset, sort=sort)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->get_threads_for_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. |
 **ascending** | **bool**| The direction of sort: true for ascending, and false for descending | [optional]
 **limit** | **float**| Limits the size of the page returned. For example, a page size of 10 require limit &#x3D; 10. The maximum Limit for this call is 20.&#39;  | [optional] if omitted the server will use the default value of 10
 **offset** | **float**| The index of the pagination offset. For a page size of 10, the first page would be at offset &#x3D; 0, and the second page would be at offset &#x3D; 10.&#39;  | [optional] if omitted the server will use the default value of 0
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

# **pin_thread**
> pin_thread(thread_id)

Pin a Thread.

This API is used to mark a thread as pinned.  Target users: only forum's moderator can mark a thread as pinned. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import discussion_services_api
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
    api_instance = discussion_services_api.DiscussionServicesApi(api_client)
    thread_id = "threadId_example" # str | The ID of a thread.

    # example passing only required values which don't have defaults set
    try:
        # Pin a Thread.
        api_instance.pin_thread(thread_id)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->pin_thread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| The ID of a thread. |

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
**204** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_deleted_thread**
> str restore_deleted_thread(thread_id)

Restore a deleted thread.

This API is used to restore a deleted thread.  Target users: only forum's moderator can restore a deleted thread. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import discussion_services_api
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
    api_instance = discussion_services_api.DiscussionServicesApi(api_client)
    thread_id = "threadId_example" # str | The ID of a thread.

    # example passing only required values which don't have defaults set
    try:
        # Restore a deleted thread.
        api_response = api_instance.restore_deleted_thread(thread_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->restore_deleted_thread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| The ID of a thread. |

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

# **unpin_thread**
> unpin_thread(thread_id)

Unpin a thread.

This API is used to unpin a thread.  Target users: only forum's moderator can unpin a thread. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import discussion_services_api
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
    api_instance = discussion_services_api.DiscussionServicesApi(api_client)
    thread_id = "threadId_example" # str | The ID of a thread.

    # example passing only required values which don't have defaults set
    try:
        # Unpin a thread.
        api_instance.unpin_thread(thread_id)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->unpin_thread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| The ID of a thread. |

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
**204** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_reply_message**
> DiscussionReplyBundle update_reply_message(reply_id)

Update the message of a reply.

This API is used to update the message of a reply.  Target users: only the author of the reply can update its message.' 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import discussion_services_api
from synclient.model.update_reply_message import UpdateReplyMessage
from synclient.model.discussion_reply_bundle import DiscussionReplyBundle
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
    api_instance = discussion_services_api.DiscussionServicesApi(api_client)
    reply_id = "replyId_example" # str | The ID of the Reply.
    update_reply_message = UpdateReplyMessage(
        message_markdown="message_markdown_example",
    ) # UpdateReplyMessage |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the message of a reply.
        api_response = api_instance.update_reply_message(reply_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->update_reply_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the message of a reply.
        api_response = api_instance.update_reply_message(reply_id, update_reply_message=update_reply_message)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->update_reply_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reply_id** | **str**| The ID of the Reply. |
 **update_reply_message** | [**UpdateReplyMessage**](UpdateReplyMessage.md)|  | [optional]

### Return type

[**DiscussionReplyBundle**](DiscussionReplyBundle.md)

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

# **update_thread_message**
> DiscussionThreadBundle update_thread_message(thread_id)

Update the message of a thread.

This API is used to update the message of a thread.  Target users: only the author of the thread can update its message.' 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import discussion_services_api
from synclient.model.update_thread_message import UpdateThreadMessage
from synclient.model.discussion_thread_bundle import DiscussionThreadBundle
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
    api_instance = discussion_services_api.DiscussionServicesApi(api_client)
    thread_id = "threadId_example" # str | The ID of a thread.
    update_thread_message = UpdateThreadMessage(
        message_markdown="message_markdown_example",
    ) # UpdateThreadMessage |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the message of a thread.
        api_response = api_instance.update_thread_message(thread_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->update_thread_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the message of a thread.
        api_response = api_instance.update_thread_message(thread_id, update_thread_message=update_thread_message)
        pprint(api_response)
    except synclient.ApiException as e:
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

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_thread_title**
> DiscussionThreadBundle update_thread_title(thread_id)

Update the title of a Thread.

This API is used to update the title of a thread.  Target users: only the author of the thread can update its title.' 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import discussion_services_api
from synclient.model.discussion_thread_bundle import DiscussionThreadBundle
from synclient.model.update_thread_title import UpdateThreadTitle
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
    api_instance = discussion_services_api.DiscussionServicesApi(api_client)
    thread_id = "threadId_example" # str | The ID of a thread.
    update_thread_title = UpdateThreadTitle(
        title="title_example",
    ) # UpdateThreadTitle |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the title of a Thread.
        api_response = api_instance.update_thread_title(thread_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DiscussionServicesApi->update_thread_title: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the title of a Thread.
        api_response = api_instance.update_thread_title(thread_id, update_thread_title=update_thread_title)
        pprint(api_response)
    except synclient.ApiException as e:
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

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

