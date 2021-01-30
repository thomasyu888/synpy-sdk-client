# SnapshotRequest

Request to create a new snapshot of a table or view. The provided comment, label, and activity ID will be applied to the current version thereby creating a snapshot and locking the current version. After the snapshot is created a new version will be started with an 'in-progress' label. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_activity_id** | **str** | Optional. If createNewSnapshot&#x3D;true, the Activity ID to be applied to the snapshot version. Null by default  | [optional] 
**snapshot_comment** | **str** | Optional. If createNewSnapshot&#x3D;true, the comment to be applied to the snapshot version. Null by default  | [optional] 
**snapshot_label** | **str** | Optional. If createNewSnapshot&#x3D;true, the label to be applied to the snapshot version. Null by default  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


