# synclient.MessageServicesApi

All URIs are relative to *https://repo-prod.prod.sagebase.org/repo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_message_to_entity_owner**](MessageServicesApi.md#send_message_to_entity_owner) | **POST** /entity/{id}/message | Adds the owner of the given entity as an additional recipient of the message.


# **send_message_to_entity_owner**
> MessageToUser send_message_to_entity_owner(id)

Adds the owner of the given entity as an additional recipient of the message.

Adds the owner of the given entity as an additional recipient of the message. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import message_services_api
from synclient.model.message_to_user import MessageToUser
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
    api_instance = message_services_api.MessageServicesApi(api_client)
    id = "id_example" # str | The ID of an Entity.
    message_to_user = MessageToUser(
        bcc="bcc_example",
        cc="cc_example",
        created_by="created_by_example",
        created_on="created_on_example",
        file_handle_id="file_handle_id_example",
        id="id_example",
        in_reply_to="in_reply_to_example",
        in_reply_to_root="in_reply_to_root_example",
        is_notification_message=True,
        notification_unsubscribe_endpoint="notification_unsubscribe_endpoint_example",
        recipients=[
            "recipients_example",
        ],
        subject="subject_example",
        to="to_example",
        user_profile_setting_endpoint="user_profile_setting_endpoint_example",
        with_profile_setting_link=True,
        with_unsubscribe_link=True,
    ) # MessageToUser |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Adds the owner of the given entity as an additional recipient of the message.
        api_response = api_instance.send_message_to_entity_owner(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling MessageServicesApi->send_message_to_entity_owner: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Adds the owner of the given entity as an additional recipient of the message.
        api_response = api_instance.send_message_to_entity_owner(id, message_to_user=message_to_user)
        pprint(api_response)
    except synclient.ApiException as e:
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

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

