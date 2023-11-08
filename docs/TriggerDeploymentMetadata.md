# TriggerDeploymentMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TriggerDeploymentMetadataTriggerType**](TriggerDeploymentMetadataTriggerType.md) |  | [optional] 
**actor** | [**TriggerDeploymentMetadataActorType**](TriggerDeploymentMetadataActorType.md) |  | [optional] 
**git** | [**GitDeploymentMetadata**](GitDeploymentMetadata.md) |  | [optional] 

## Example

```python
from koyeb.models.trigger_deployment_metadata import TriggerDeploymentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerDeploymentMetadata from a JSON string
trigger_deployment_metadata_instance = TriggerDeploymentMetadata.from_json(json)
# print the JSON string representation of the object
print TriggerDeploymentMetadata.to_json()

# convert the object into a dict
trigger_deployment_metadata_dict = trigger_deployment_metadata_instance.to_dict()
# create an instance of TriggerDeploymentMetadata from a dict
trigger_deployment_metadata_form_dict = trigger_deployment_metadata.from_dict(trigger_deployment_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


