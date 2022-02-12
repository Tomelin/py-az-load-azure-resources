import os
import json
from datetime import datetime
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

WEST_US = "eastus"
GROUP_NAME = "pjlab"

def run_example():
    """Resource Group management example."""

    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID", None) # your Azure Subscription Id
    credentials = DefaultAzureCredential()
    client = ResourceManagementClient(credentials, subscription_id)
    resource_group_params = {"location": "eastus"}
    group_list = client.resource_groups.list()
    # Show the groups in formatted output
    column_width = 40

    print("Resource Group".ljust(column_width) + "Location")
    print("-" * (column_width * 2))

    # for group in list(group_list):
    for item in group_list:
        # print(f"{group.name:<{column_width}}{group.location}")
        gname = item.id.split('/')[4]

    # # List Resources within the group
    # print("List all of the resources within the group")
        for item in client.resources.list_by_resource_group(gname):
            print_item(item)

        # # # Export the Resource group template
        print("Export Resource Group Template")
        BODY = {
        'resources': ['*']
        }
        print(
            json.dumps(
                client.resource_groups.begin_export_template(
                    gname, BODY).result().template, indent=4
            )
        )
        print("\n\n")

def print_item(group):
    """Print a ResourceGroup instance."""
    print("\tName: {}".format(group.name))
    print("\tId: {}".format(group.id))
    print("\tLocation: {}".format(group.location))
    print("\tTags: {}".format(group.tags))
    # print_properties(group.properties)

def print_properties(props):
    """Print a ResourceGroup properties instance."""
    if props and props.provisioning_state:
        print("\tProperties:")
        print("\t\tProvisioning State: {}".format(props.provisioning_state))
    print("\n\n")


if __name__ == "__main__":
    run_example()
