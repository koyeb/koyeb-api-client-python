# RegionalDeploymentMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runtime_job_id** | **str** |  | [optional] 

## Example

```python
from koyeb.models.regional_deployment_metadata import RegionalDeploymentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of RegionalDeploymentMetadata from a JSON string
regional_deployment_metadata_instance = RegionalDeploymentMetadata.from_json(json)
# print the JSON string representation of the object
print(RegionalDeploymentMetadata.to_json())

# convert the object into a dict
regional_deployment_metadata_dict = regional_deployment_metadata_instance.to_dict()
# create an instance of RegionalDeploymentMetadata from a dict
regional_deployment_metadata_form_dict = regional_deployment_metadata.from_dict(regional_deployment_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


