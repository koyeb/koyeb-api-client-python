# DeploymentScalingTargetSleepIdleDelay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** | Delay in seconds after which a service which received 0 request is scaled to 0. This is not configurable and must be set to 300 (5 minutes). Get in touch to tune it. | [optional] 

## Example

```python
from koyeb.models.deployment_scaling_target_sleep_idle_delay import DeploymentScalingTargetSleepIdleDelay

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentScalingTargetSleepIdleDelay from a JSON string
deployment_scaling_target_sleep_idle_delay_instance = DeploymentScalingTargetSleepIdleDelay.from_json(json)
# print the JSON string representation of the object
print(DeploymentScalingTargetSleepIdleDelay.to_json())

# convert the object into a dict
deployment_scaling_target_sleep_idle_delay_dict = deployment_scaling_target_sleep_idle_delay_instance.to_dict()
# create an instance of DeploymentScalingTargetSleepIdleDelay from a dict
deployment_scaling_target_sleep_idle_delay_from_dict = DeploymentScalingTargetSleepIdleDelay.from_dict(deployment_scaling_target_sleep_idle_delay_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


