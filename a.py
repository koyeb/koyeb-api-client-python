import time
import os
import koyeb
from koyeb.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.koyeb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = koyeb.Configuration(
    host = "https://app.koyeb.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'


# Enter a context with an instance of the API client
with koyeb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = koyeb.AppsApi(api_client)
    app = koyeb.CreateApp() # CreateApp | 

    try:
        # Create App
        api_response = api_instance.create_app(app)
        print("The response of AppsApi->create_app:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppsApi->create_app: %s\n" % e)
