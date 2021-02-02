# synclient.AsynchronousJobServicesApi

All URIs are relative to *https://repo-prod.prod.sagebase.org/repo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_job_status**](AsynchronousJobServicesApi.md#get_job_status) | **GET** /asynchronous/job/{jobId} | Get Asynchronous Job.
[**launch_new_job**](AsynchronousJobServicesApi.md#launch_new_job) | **POST** /asynchronous/job | Launch new Asynchronous jobs.
[**stop_job**](AsynchronousJobServicesApi.md#stop_job) | **GET** /asynchronous/job/{jobId}/cancel | Stop a Asynchronous Job.


# **get_job_status**
> AsynchronousJobStatus get_job_status(job_id)

Get Asynchronous Job.

Once a job is launched its progress can be monitored by getting its status with this method. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import asynchronous_job_services_api
from synclient.model.asynchronous_job_status import AsynchronousJobStatus
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
    api_instance = asynchronous_job_services_api.AsynchronousJobServicesApi(api_client)
    job_id = "jobId_example" # str | The ID of a Asynchronous Job.

    # example passing only required values which don't have defaults set
    try:
        # Get Asynchronous Job.
        api_response = api_instance.get_job_status(job_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling AsynchronousJobServicesApi->get_job_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The ID of a Asynchronous Job. |

### Return type

[**AsynchronousJobStatus**](AsynchronousJobStatus.md)

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

# **launch_new_job**
> AsynchronousJobStatus launch_new_job()

Launch new Asynchronous jobs.

This method is used to launch new jobs. The type of job that will be launched is determined by the passed  AsynchronousJobBody.  The following are the currently supported job types:  * UploadToTableRequest * DownloadFromTableRequest  Note: Each job types has different access requirements. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import asynchronous_job_services_api
from synclient.model.asynchronous_job_status import AsynchronousJobStatus
from synclient.model.asynchronous_request_body import AsynchronousRequestBody
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
    api_instance = asynchronous_job_services_api.AsynchronousJobServicesApi(api_client)
    asynchronous_request_body = AsynchronousRequestBody(
        concrete_type="concrete_type_example",
    ) # AsynchronousRequestBody |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Launch new Asynchronous jobs.
        api_response = api_instance.launch_new_job(asynchronous_request_body=asynchronous_request_body)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling AsynchronousJobServicesApi->launch_new_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asynchronous_request_body** | [**AsynchronousRequestBody**](AsynchronousRequestBody.md)|  | [optional]

### Return type

[**AsynchronousJobStatus**](AsynchronousJobStatus.md)

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

# **stop_job**
> stop_job(job_id)

Stop a Asynchronous Job.

Once a job is launched it can be cancelled if the job is set up to be cancelable. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import asynchronous_job_services_api
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
    api_instance = asynchronous_job_services_api.AsynchronousJobServicesApi(api_client)
    job_id = "jobId_example" # str | The ID of a Asynchronous Job.

    # example passing only required values which don't have defaults set
    try:
        # Stop a Asynchronous Job.
        api_instance.stop_job(job_id)
    except synclient.ApiException as e:
        print("Exception when calling AsynchronousJobServicesApi->stop_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The ID of a Asynchronous Job. |

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

