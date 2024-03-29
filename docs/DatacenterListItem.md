# DatacenterListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**region_id** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**coordinates** | **List[str]** |  | [optional] 

## Example

```python
from koyeb.models.datacenter_list_item import DatacenterListItem

# TODO update the JSON string below
json = "{}"
# create an instance of DatacenterListItem from a JSON string
datacenter_list_item_instance = DatacenterListItem.from_json(json)
# print the JSON string representation of the object
print(DatacenterListItem.to_json())

# convert the object into a dict
datacenter_list_item_dict = datacenter_list_item_instance.to_dict()
# create an instance of DatacenterListItem from a dict
datacenter_list_item_form_dict = datacenter_list_item.from_dict(datacenter_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


