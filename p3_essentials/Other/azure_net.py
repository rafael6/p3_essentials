__author__ = 'rafael'

# TODO: Install library
from azure.mgmt.compute import ComputeManagementClient, ComputeManagementClientConfiguration
from azure.mgmt.network import NetworkManagementClient, NetworkManagementClientConfiguration

# TODO: Replace this with your subscription id
subscription_id = '33333333-3333-3333-3333-333333333333'
# TODO: See above how to get a Credentials instance
credentials = ...

compute_client = ComputeManagementClient(
    ComputeManagementClientConfiguration(
        credentials,
        subscription_id
    )
)

network_client = NetworkManagementClient(
    NetworkManagementClientConfiguration(
        credentials,
        subscription_id
    )
)