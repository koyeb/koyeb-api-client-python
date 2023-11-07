# GetOrganizationInvitationReply


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitation** | [**OrganizationInvitation**](OrganizationInvitation.md) |  | [optional] 

## Example

```python
from koyeb.models.get_organization_invitation_reply import GetOrganizationInvitationReply

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganizationInvitationReply from a JSON string
get_organization_invitation_reply_instance = GetOrganizationInvitationReply.from_json(json)
# print the JSON string representation of the object
print GetOrganizationInvitationReply.to_json()

# convert the object into a dict
get_organization_invitation_reply_dict = get_organization_invitation_reply_instance.to_dict()
# create an instance of GetOrganizationInvitationReply from a dict
get_organization_invitation_reply_form_dict = get_organization_invitation_reply.from_dict(get_organization_invitation_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


