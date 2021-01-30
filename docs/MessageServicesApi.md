# synclient.MessageServicesApi

All URIs are relative to *https://repo-prod.prod.sagebase.org/repo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_message_to_entity_owner**](MessageServicesApi.md#send_message_to_entity_owner) | **POST** /entity/{id}/message | Adds the owner of the given entity as an additional recipient of the message.


# **send_message_to_entity_owner**
> MessageToUser send_message_to_entity_owner(id, message_to_user=message_to_user)

Adds the owner of the given entity as an additional recipient of the message.

Adds the owner of the given entity as an additional recipient of the message. 

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
    api_instance = synclient.MessageServicesApi(api_client)
    id = 'id_example' # str | The ID of an Entity.
message_to_user = synclient.MessageToUser() # MessageToUser |  (optional)

    try:
        # Adds the owner of the given entity as an additional recipient of the message.
        api_response = api_instance.send_message_to_entity_owner(id, message_to_user=message_to_user)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessageServicesApi->send_message_to_entity_owner: %s\n" % e)
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
    api_instance = synclient.MessageServicesApi(api_client)
    id = 'id_example' # str | The ID of an Entity.
message_to_user = synclient.MessageToUser() # MessageToUser |  (optional)

    try:
        # Adds the owner of the given entity as an additional recipient of the message.
        api_response = api_instance.send_message_to_entity_owner(id, message_to_user=message_to_user)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessageServicesApi->send_message_to_entity_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. | 
 **message_to_user** | [**MessageToUser**](MessageToUser.md)|  | [optional] 

### Return type

[**MessageToUser**](MessageToUser.md)

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

