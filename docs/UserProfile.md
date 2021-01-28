# UserProfile

JSON schema for UserProfile POJO
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**r_studio_url** | **str** | URL for RStudio server assigned to the user | [optional] 
**company** | **str** | This person&#39;s current affiliation  | [optional] 
**created_on** | **str** | The date this profile was created. | [optional] 
**display_name** | **str** | Will always be null. | [optional] 
**email** | **str** | Users can have more than one email. See emails | [optional] 
**emails** | **list[str]** | The list of user email addresses registered to this user. | [optional] 
**etag** | **str** | Synapse employs an Optimistic Concurrency Control (OCC) scheme to handle concurrent updates. Since the E-Tag changes every time an entity is updated it is used to detect when a client&#39;s current representation of an entity is out-of-date.  | [optional] 
**first_name** | **str** | This person&#39;s given name (forename)  | [optional] 
**industry** | **str** | The industry/discipline that this person is associated with | [optional] 
**last_name** | **str** | This person&#39;s family name (surname)  | [optional] 
**location** | **str** | This person&#39;s location  | [optional] 
**notification_settings** | [**Settings**](Settings.md) |  | [optional] 
**open_ids** | **list[str]** | &#39;The list of OpenIds bound to this user&#39;s account.&#39;  | [optional] 
**owner_id** | **str** | &#39;A foreign key to the ID of the &#39;principal&#39; object for the user.&#39;  | [optional] 
**position** | **str** | This person&#39;s current position title  | [optional] 
**preferences** | [**list[UserPreference]**](UserPreference.md) | User preferences | [optional] 
**profile_picure_file_handle_id** | **str** | The FileHandle.id of the user&#39;s profile picture.  | [optional] 
**summary** | **str** | A summary description about this person | [optional] 
**team_name** | **str** | This person&#39;s default team name  | [optional] 
**url** | **str** | A link to more information about this person | [optional] 
**user_name** | **str** | A name chosen by the user that uniquely identifies them. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


