# NotificationList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notifications** | [**List[Notification]**](Notification.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**count** | **int** |  | [optional] 
**is_read** | **bool** |  | [optional] 
**is_seen** | **bool** |  | [optional] 
**unread** | **int** |  | [optional] 
**unseen** | **int** |  | [optional] 

## Example

```python
from koyeb.models.notification_list import NotificationList

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationList from a JSON string
notification_list_instance = NotificationList.from_json(json)
# print the JSON string representation of the object
print NotificationList.to_json()

# convert the object into a dict
notification_list_dict = notification_list_instance.to_dict()
# create an instance of NotificationList from a dict
notification_list_form_dict = notification_list.from_dict(notification_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


