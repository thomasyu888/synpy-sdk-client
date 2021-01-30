# synclient.DockerCommitServicesApi

All URIs are relative to *https://repo-prod.prod.sagebase.org/repo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_docker_commit**](DockerCommitServicesApi.md#add_docker_commit) | **POST** /entity/{id}/dockerCommit | Add a commit (tag and digest) for an external/unmanaged Docker repository.
[**list_docker_tags**](DockerCommitServicesApi.md#list_docker_tags) | **GET** /entity/{id}/dockerTag | List the tagged commits (tag/digest pairs) for the given Docker repository.


# **add_docker_commit**
> add_docker_commit(id)

Add a commit (tag and digest) for an external/unmanaged Docker repository.

Add a commit (tag and digest) for an external/unmanaged Docker repository. (Commits for managed repositories are added via direct integration with the Synapse Docker registry.) 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import docker_commit_services_api
from synclient.model.docker_commit import DockerCommit
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
    api_instance = docker_commit_services_api.DockerCommitServicesApi(api_client)
    id = "id_example" # str | the ID of the Docker repository entity
    docker_commit = DockerCommit(
        created_on="created_on_example",
        digest="digest_example",
        tag="tag_example",
    ) # DockerCommit | the new tag/digest pair for the repository (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a commit (tag and digest) for an external/unmanaged Docker repository.
        api_instance.add_docker_commit(id)
    except synclient.ApiException as e:
        print("Exception when calling DockerCommitServicesApi->add_docker_commit: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a commit (tag and digest) for an external/unmanaged Docker repository.
        api_instance.add_docker_commit(id, docker_commit=docker_commit)
    except synclient.ApiException as e:
        print("Exception when calling DockerCommitServicesApi->add_docker_commit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID of the Docker repository entity |
 **docker_commit** | [**DockerCommit**](DockerCommit.md)| the new tag/digest pair for the repository | [optional]

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
**204** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_docker_tags**
> PaginatedResultsOfDockerCommit list_docker_tags(id)

List the tagged commits (tag/digest pairs) for the given Docker repository.

List the tagged commits (tag/digest pairs) for the given Docker repository.  Only the most recent digest for each tag is returned since, following Docker's convention, a tag may be reassigned to a newer commit. The list may be sorted by date or tag.  The default is to sort by date, descending (newest first).' 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import docker_commit_services_api
from synclient.model.paginated_results_of_docker_commit import PaginatedResultsOfDockerCommit
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
    api_instance = docker_commit_services_api.DockerCommitServicesApi(api_client)
    id = "id_example" # str | the ID of the Docker repository entity
    ascending = False # bool | Ascending (optional) if omitted the server will use the default value of False
    limit = 20 # int | pagination parameter, optional (default is 20) (optional) if omitted the server will use the default value of 20
    offset = 0 # int | pagination parameter, optional (default is 0) (optional) if omitted the server will use the default value of 0
    sort = "sort_example" # str | Sort results (optional)

    # example passing only required values which don't have defaults set
    try:
        # List the tagged commits (tag/digest pairs) for the given Docker repository.
        api_response = api_instance.list_docker_tags(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DockerCommitServicesApi->list_docker_tags: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List the tagged commits (tag/digest pairs) for the given Docker repository.
        api_response = api_instance.list_docker_tags(id, ascending=ascending, limit=limit, offset=offset, sort=sort)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DockerCommitServicesApi->list_docker_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID of the Docker repository entity |
 **ascending** | **bool**| Ascending | [optional] if omitted the server will use the default value of False
 **limit** | **int**| pagination parameter, optional (default is 20) | [optional] if omitted the server will use the default value of 20
 **offset** | **int**| pagination parameter, optional (default is 0) | [optional] if omitted the server will use the default value of 0
 **sort** | **str**| Sort results | [optional]

### Return type

[**PaginatedResultsOfDockerCommit**](PaginatedResultsOfDockerCommit.md)

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

