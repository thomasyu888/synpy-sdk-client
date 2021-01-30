# synclient.CertifiedUserServicesApi

All URIs are relative to *https://repo-prod.prod.sagebase.org/repo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_passing_record**](CertifiedUserServicesApi.md#get_passing_record) | **GET** /user/{id}/certifiedUserPassingRecord | Retrieve the Passing Record on the User Certification test for the given user. 
[**set_user_certification_status**](CertifiedUserServicesApi.md#set_user_certification_status) | **PUT** /user/{id}/certificationStatus | Set certification status


# **get_passing_record**
> PassingRecord get_passing_record(id)

Retrieve the Passing Record on the User Certification test for the given user. 

Retrieve the Passing Record on the User Certification test for the given user. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import certified_user_services_api
from synclient.model.passing_record import PassingRecord
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
    api_instance = certified_user_services_api.CertifiedUserServicesApi(api_client)
    id = "id_example" # str | The ID of the Synapse user.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the Passing Record on the User Certification test for the given user. 
        api_response = api_instance.get_passing_record(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling CertifiedUserServicesApi->get_passing_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Synapse user. |

### Return type

[**PassingRecord**](PassingRecord.md)

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

# **set_user_certification_status**
> set_user_certification_status(id)

Set certification status

Setting certification status.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import certified_user_services_api
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
    api_instance = certified_user_services_api.CertifiedUserServicesApi(api_client)
    id = "id_example" # str | The ID of the Synapse user.

    # example passing only required values which don't have defaults set
    try:
        # Set certification status
        api_instance.set_user_certification_status(id)
    except synclient.ApiException as e:
        print("Exception when calling CertifiedUserServicesApi->set_user_certification_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Synapse user. |

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
**410** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

