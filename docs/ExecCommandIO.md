# ExecCommandIO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **bytearray** | Data is base64 encoded | [optional] 
**close** | **bool** | Indicate last data frame | [optional] 

## Example

```python
from koyeb.models.exec_command_io import ExecCommandIO

# TODO update the JSON string below
json = "{}"
# create an instance of ExecCommandIO from a JSON string
exec_command_io_instance = ExecCommandIO.from_json(json)
# print the JSON string representation of the object
print(ExecCommandIO.to_json())

# convert the object into a dict
exec_command_io_dict = exec_command_io_instance.to_dict()
# create an instance of ExecCommandIO from a dict
exec_command_io_form_dict = exec_command_io.from_dict(exec_command_io_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


