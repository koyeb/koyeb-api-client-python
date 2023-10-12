# CreateOrganizationInvitationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 

## Example

```python
from koyeb.models.create_organization_invitation_request import CreateOrganizationInvitationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationInvitationRequest from a JSON string
create_organization_invitation_request_instance = CreateOrganizationInvitationRequest.from_json(json)
# print the JSON string representation of the object
print CreateOrganizationInvitationRequest.to_json()

# convert the object into a dict
create_organization_invitation_request_dict = create_organization_invitation_request_instance.to_dict()
# create an instance of CreateOrganizationInvitationRequest from a dict
create_organization_invitation_request_form_dict = create_organization_invitation_request.from_dict(create_organization_invitation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


