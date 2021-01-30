# MessageToUser

JSON schema for a message to another user
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bcc** | **str** | The email addresses in the &#39;bcc&#39; field of the email message  | [optional] 
**cc** | **str** | The email addresses in the &#39;cc&#39; field of the email message  | [optional] 
**created_by** | **str** | The unique identifier of the sender of this message | [optional] 
**created_on** | **str** | When this message was created | [optional] 
**file_handle_id** | **str** | The S3 file handle storing the body of this message. Note: The file&#39;s mime type should be &#39;text/plain&#39; or &#39;text/html&#39;. If no character encoding is specified, then UTF-8 is assumed.  | [optional] 
**id** | **str** | The unique identifier of the message or comment | [optional] 
**in_reply_to** | **str** | The unique identifier of the message being replied to. Can be null | [optional] 
**in_reply_to_root** | **str** | The unique identifier of the root message being replied to | [optional] 
**is_notification_message** | **bool** | A notification message is sent from a noreply email address, delivery failures are not sent back to the sender | [optional] 
**notification_unsubscribe_endpoint** | **str** | the portal prefix for one-click email unsubscription. A signed, serialized token is appended to create the complete URL. If omitted, the default endpoint will be used.  | [optional] 
**recipients** | **list[str]** | The unique identifiers of the intended recipients of a message | [optional] 
**subject** | **str** | Topic of this message. Optional | [optional] 
**to** | **str** | The email addresses in the &#39;to&#39; field of the email message  | [optional] 
**user_profile_setting_endpoint** | **str** | the portal link to user profile setting page. If omitted, the default endpoint will be used. | [optional] 
**with_profile_setting_link** | **bool** | should the user profile setting link be included in the email? | [optional] 
**with_unsubscribe_link** | **bool** | should the unsubscribe link be included in the email? | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


