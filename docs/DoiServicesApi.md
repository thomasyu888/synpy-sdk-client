# synclient.DoiServicesApi

All URIs are relative to *https://repo-prod.prod.sagebase.org/repo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_create_or_update_doi_results**](DoiServicesApi.md#get_create_or_update_doi_results) | **GET** /doi/async/get/{asyncToken} | Get the results of a call to POST /doi/async/start
[**get_doi_association**](DoiServicesApi.md#get_doi_association) | **GET** /doi/association | Retrieves the DOI for the object.
[**get_doi_v2**](DoiServicesApi.md#get_doi_v2) | **GET** /doi | Retrieves the DOI for the object and its associated DOI metadata.
[**locate**](DoiServicesApi.md#locate) | **GET** /doi/locate | Retrieves the Synapse web portal URL to the object entered.
[**start_create_or_update_doi**](DoiServicesApi.md#start_create_or_update_doi) | **POST** /doi/async/start | Asynchronously creates or updates a DOI in Synapse, with input metadata.


# **get_create_or_update_doi_results**
> DoiResponse get_create_or_update_doi_results(async_token)

Get the results of a call to POST /doi/async/start

Get the results of a call to POST /doi/async/start 

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
    api_instance = synclient.DoiServicesApi(api_client)
    async_token = 'async_token_example' # str | The async job token from the create/update call

    try:
        # Get the results of a call to POST /doi/async/start
        api_response = api_instance.get_create_or_update_doi_results(async_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DoiServicesApi->get_create_or_update_doi_results: %s\n" % e)
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
    api_instance = synclient.DoiServicesApi(api_client)
    async_token = 'async_token_example' # str | The async job token from the create/update call

    try:
        # Get the results of a call to POST /doi/async/start
        api_response = api_instance.get_create_or_update_doi_results(async_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DoiServicesApi->get_create_or_update_doi_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_token** | **str**| The async job token from the create/update call | 

### Return type

[**DoiResponse**](DoiResponse.md)

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

# **get_doi_association**
> DoiAssociation get_doi_association(id, type, version=version)

Retrieves the DOI for the object.

Retrieves the DOI for the object. Note: this call only retrieves the DOI association, if it exists. To retrieve the metadata for the object, see <a href=\"${GET.doi}\">GET /doi</a>' 

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
    api_instance = synclient.DoiServicesApi(api_client)
    id = 'id_example' # str | The ID of the object to retrieve
type = synclient.ObjectType() # ObjectType | The type of the object
version = 56 # int | The version number of the object (optional)

    try:
        # Retrieves the DOI for the object.
        api_response = api_instance.get_doi_association(id, type, version=version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DoiServicesApi->get_doi_association: %s\n" % e)
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
    api_instance = synclient.DoiServicesApi(api_client)
    id = 'id_example' # str | The ID of the object to retrieve
type = synclient.ObjectType() # ObjectType | The type of the object
version = 56 # int | The version number of the object (optional)

    try:
        # Retrieves the DOI for the object.
        api_response = api_instance.get_doi_association(id, type, version=version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DoiServicesApi->get_doi_association: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the object to retrieve | 
 **type** | [**ObjectType**](.md)| The type of the object | 
 **version** | **int**| The version number of the object | [optional] 

### Return type

[**DoiAssociation**](DoiAssociation.md)

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

# **get_doi_v2**
> Doi get_doi_v2(id, type, version=version)

Retrieves the DOI for the object and its associated DOI metadata.

Retrieves the DOI for the object and its associated DOI metadata. Note: this call calls an external API, which may impact performance To just retrieve the DOI association, see: <a href=\"${GET.doi.association}\">GET /doi/association</a> 

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
    api_instance = synclient.DoiServicesApi(api_client)
    id = 'id_example' # str | The ID of the object to retrieve
type = synclient.ObjectType() # ObjectType | The type of the object
version = 56 # int | The version number of the object (optional)

    try:
        # Retrieves the DOI for the object and its associated DOI metadata.
        api_response = api_instance.get_doi_v2(id, type, version=version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DoiServicesApi->get_doi_v2: %s\n" % e)
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
    api_instance = synclient.DoiServicesApi(api_client)
    id = 'id_example' # str | The ID of the object to retrieve
type = synclient.ObjectType() # ObjectType | The type of the object
version = 56 # int | The version number of the object (optional)

    try:
        # Retrieves the DOI for the object and its associated DOI metadata.
        api_response = api_instance.get_doi_v2(id, type, version=version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DoiServicesApi->get_doi_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the object to retrieve | 
 **type** | [**ObjectType**](.md)| The type of the object | 
 **version** | **int**| The version number of the object | [optional] 

### Return type

[**Doi**](Doi.md)

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

# **locate**
> str locate(id, type, redirect=redirect, version=version)

Retrieves the Synapse web portal URL to the object entered.

Retrieves the Synapse web portal URL to the object entered. Note: This call does not check to see if the object exists in Synapse. 

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
    api_instance = synclient.DoiServicesApi(api_client)
    id = 'id_example' # str | The ID of the object to retrieve
type = synclient.ObjectType() # ObjectType | The type of the object
redirect = True # bool | Whether to return the URL or redirect to the URL (optional) (default to True)
version = 56 # int | The version number of the object (optional)

    try:
        # Retrieves the Synapse web portal URL to the object entered.
        api_response = api_instance.locate(id, type, redirect=redirect, version=version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DoiServicesApi->locate: %s\n" % e)
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
    api_instance = synclient.DoiServicesApi(api_client)
    id = 'id_example' # str | The ID of the object to retrieve
type = synclient.ObjectType() # ObjectType | The type of the object
redirect = True # bool | Whether to return the URL or redirect to the URL (optional) (default to True)
version = 56 # int | The version number of the object (optional)

    try:
        # Retrieves the Synapse web portal URL to the object entered.
        api_response = api_instance.locate(id, type, redirect=redirect, version=version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DoiServicesApi->locate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the object to retrieve | 
 **type** | [**ObjectType**](.md)| The type of the object | 
 **redirect** | **bool**| Whether to return the URL or redirect to the URL | [optional] [default to True]
 **version** | **int**| The version number of the object | [optional] 

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

# **start_create_or_update_doi**
> AsyncJobId start_create_or_update_doi(doi_request=doi_request)

Asynchronously creates or updates a DOI in Synapse, with input metadata.

Asynchronously creates or updates a DOI in Synapse, with input metadata. Retrieve the results with <a href=\"${GET.doi.async.get.asyncToken}\">GET /doi/async/get/{asyncToken}</a>. This call may fail if the external DataCite API is down. If the failure is recoverable, it will retry automatically.' 

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
    api_instance = synclient.DoiServicesApi(api_client)
    doi_request = synclient.DoiRequest() # DoiRequest | A request containing a DOI and its metadata to associate with a Synapse object  (optional)

    try:
        # Asynchronously creates or updates a DOI in Synapse, with input metadata.
        api_response = api_instance.start_create_or_update_doi(doi_request=doi_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DoiServicesApi->start_create_or_update_doi: %s\n" % e)
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
    api_instance = synclient.DoiServicesApi(api_client)
    doi_request = synclient.DoiRequest() # DoiRequest | A request containing a DOI and its metadata to associate with a Synapse object  (optional)

    try:
        # Asynchronously creates or updates a DOI in Synapse, with input metadata.
        api_response = api_instance.start_create_or_update_doi(doi_request=doi_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DoiServicesApi->start_create_or_update_doi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doi_request** | [**DoiRequest**](DoiRequest.md)| A request containing a DOI and its metadata to associate with a Synapse object  | [optional] 

### Return type

[**AsyncJobId**](AsyncJobId.md)

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

