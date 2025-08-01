# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T12:03:28+00:00



import argparse
import json
import os
from datetime import datetime
from typing import *
from typing import Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, BaseSecurity
from fastapi import Header, Path, Query
from pydantic import conint

from models import (
    ClaimDevicesByClaimCodeResponse,
    DescribeDeviceResponse,
    DevicesDeviceIdFinalizeClaimPutRequest,
    DevicesDeviceIdMethodsPostRequest,
    DevicesDeviceIdStatePutRequest,
    FinalizeDeviceClaimResponse,
    ForbiddenException,
    GetDeviceMethodsResponse,
    InitiateDeviceClaimResponse,
    InternalFailureException,
    InvalidRequestException,
    InvokeDeviceMethodResponse,
    ListDeviceEventsResponse,
    ListDevicesResponse,
    ListTagsForResourceResponse,
    PreconditionFailedException,
    RangeNotSatisfiableException,
    ResourceConflictException,
    ResourceNotFoundException,
    TagKeys,
    TagsResourceArnPostRequest,
    UnclaimDeviceResponse,
    UpdateDeviceStateResponse,
)

app = MCPProxy(
    contact={
        'email': 'mike.ralphson@gmail.com',
        'name': 'Mike Ralphson',
        'url': 'https://github.com/mermade/aws2openapi',
        'x-twitter': 'PermittedSoc',
    },
    description='Describes all of the AWS IoT 1-Click device-related API operations for the service.\n Also provides sample requests, responses, and errors for the supported web services\n protocols.',
    license={'name': 'Apache 2.0 License', 'url': 'http://www.apache.org/licenses/'},
    termsOfService='https://aws.amazon.com/service-terms/',
    title='AWS IoT 1-Click Devices Service',
    version='2018-05-14',
    servers=[
        {
            'description': 'The AWS IoT 1-Click Devices Service multi-region endpoint',
            'url': 'http://devices.iot1click.{region}.amazonaws.com',
            'variables': {
                'region': {
                    'default': 'us-east-1',
                    'description': 'The AWS region',
                    'enum': [
                        'us-east-1',
                        'us-east-2',
                        'us-west-1',
                        'us-west-2',
                        'us-gov-west-1',
                        'us-gov-east-1',
                        'ca-central-1',
                        'eu-north-1',
                        'eu-west-1',
                        'eu-west-2',
                        'eu-west-3',
                        'eu-central-1',
                        'eu-south-1',
                        'af-south-1',
                        'ap-northeast-1',
                        'ap-northeast-2',
                        'ap-northeast-3',
                        'ap-southeast-1',
                        'ap-southeast-2',
                        'ap-east-1',
                        'ap-south-1',
                        'sa-east-1',
                        'me-south-1',
                    ],
                }
            },
        },
        {
            'description': 'The AWS IoT 1-Click Devices Service multi-region endpoint',
            'url': 'https://devices.iot1click.{region}.amazonaws.com',
            'variables': {
                'region': {
                    'default': 'us-east-1',
                    'description': 'The AWS region',
                    'enum': [
                        'us-east-1',
                        'us-east-2',
                        'us-west-1',
                        'us-west-2',
                        'us-gov-west-1',
                        'us-gov-east-1',
                        'ca-central-1',
                        'eu-north-1',
                        'eu-west-1',
                        'eu-west-2',
                        'eu-west-3',
                        'eu-central-1',
                        'eu-south-1',
                        'af-south-1',
                        'ap-northeast-1',
                        'ap-northeast-2',
                        'ap-northeast-3',
                        'ap-southeast-1',
                        'ap-southeast-2',
                        'ap-east-1',
                        'ap-south-1',
                        'sa-east-1',
                        'me-south-1',
                    ],
                }
            },
        },
        {
            'description': 'The AWS IoT 1-Click Devices Service endpoint for China (Beijing) and China (Ningxia)',
            'url': 'http://devices.iot1click.{region}.amazonaws.com.cn',
            'variables': {
                'region': {
                    'default': 'cn-north-1',
                    'description': 'The AWS region',
                    'enum': ['cn-north-1', 'cn-northwest-1'],
                }
            },
        },
        {
            'description': 'The AWS IoT 1-Click Devices Service endpoint for China (Beijing) and China (Ningxia)',
            'url': 'https://devices.iot1click.{region}.amazonaws.com.cn',
            'variables': {
                'region': {
                    'default': 'cn-north-1',
                    'description': 'The AWS region',
                    'enum': ['cn-north-1', 'cn-northwest-1'],
                }
            },
        },
    ],
)


@app.put(
    '/claims/{claimCode}',
    description=""" Adds device(s) to your account (i.e., claim one or more devices) if and only if you
 received a claim code with the device(s). """,
    tags=['device_claim_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def claim_devices_by_claim_code(
    claim_code: str = Path(..., alias='claimCode'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/devices',
    description=""" Lists the 1-Click compatible devices associated with your AWS account. """,
    tags=['device_listing_operations'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def list_devices(
    device_type: Optional[str] = Query(None, alias='deviceType'),
    max_results: Optional[conint(ge=1, le=250)] = Query(None, alias='maxResults'),
    next_token: Optional[str] = Query(None, alias='nextToken'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/devices/{deviceId}',
    description=""" Given a device ID, returns a DescribeDeviceResponse object describing the
 details of the device. """,
    tags=['device_claim_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def describe_device(
    device_id: str = Path(..., alias='deviceId'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/devices/{deviceId}/events#fromTimeStamp&toTimeStamp',
    description=""" Using a device ID, returns a DeviceEventsResponse object containing an
 array of events for the device. """,
    tags=['device_listing_operations'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def list_device_events(
    device_id: str = Path(..., alias='deviceId'),
    from_time_stamp: datetime = Query(..., alias='fromTimeStamp'),
    max_results: Optional[conint(ge=1, le=250)] = Query(None, alias='maxResults'),
    next_token: Optional[str] = Query(None, alias='nextToken'),
    to_time_stamp: datetime = Query(..., alias='toTimeStamp'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.put(
    '/devices/{deviceId}/finalize-claim',
    description=""" <p>Given a device ID, finalizes the claim request for the associated device.</p><note>
 <p>Claiming a device consists of initiating a claim, then publishing a device event,
 and finalizing the claim. For a device of type button, a device event can
 be published by simply clicking the device.</p>
 </note> """,
    tags=['device_claim_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def finalize_device_claim(
    device_id: str = Path(..., alias='deviceId'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: DevicesDeviceIdFinalizeClaimPutRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.put(
    '/devices/{deviceId}/initiate-claim',
    description=""" <p>Given a device ID, initiates a claim request for the associated device.</p><note>
 <p>Claiming a device consists of initiating a claim, then publishing a device event,
 and finalizing the claim. For a device of type button, a device event can
 be published by simply clicking the device.</p>
 </note> """,
    tags=['device_claim_management', 'resource_tagging_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def initiate_device_claim(
    device_id: str = Path(..., alias='deviceId'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/devices/{deviceId}/methods',
    description=""" Given a device ID, returns the invokable methods associated with the device. """,
    tags=['device_claim_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def get_device_methods(
    device_id: str = Path(..., alias='deviceId'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/devices/{deviceId}/methods',
    description=""" Given a device ID, issues a request to invoke a named device method (with possible
 parameters). See the "Example POST" code snippet below. """,
    tags=['device_claim_management', 'device_state_control'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def invoke_device_method(
    device_id: str = Path(..., alias='deviceId'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: DevicesDeviceIdMethodsPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.put(
    '/devices/{deviceId}/state',
    description=""" Using a Boolean value (true or false), this operation
 enables or disables the device given a device ID. """,
    tags=['device_state_control'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def update_device_state(
    device_id: str = Path(..., alias='deviceId'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: DevicesDeviceIdStatePutRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.put(
    '/devices/{deviceId}/unclaim',
    description=""" Disassociates a device from your AWS account using its device ID. """,
    tags=['device_claim_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def unclaim_device(
    device_id: str = Path(..., alias='deviceId'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/tags/{resource-arn}',
    description=""" Lists the tags associated with the specified resource ARN. """,
    tags=['resource_tagging_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def list_tags_for_resource(
    resource_arn: str = Path(..., alias='resource-arn'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/tags/{resource-arn}',
    description=""" Adds or updates the tags associated with the resource ARN. See <a href="https://docs.aws.amazon.com/iot-1-click/latest/developerguide/1click-appendix.html#1click-limits">AWS IoT 1-Click Service Limits</a> for the maximum number of tags allowed per
 resource. """,
    tags=['resource_tagging_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def tag_resource(
    resource_arn: str = Path(..., alias='resource-arn'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: TagsResourceArnPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/tags/{resource-arn}#tagKeys',
    description=""" Using tag keys, deletes the tags (key/value pairs) associated with the specified
 resource ARN. """,
    tags=['resource_tagging_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def untag_resource(
    resource_arn: str = Path(..., alias='resource-arn'),
    tag_keys: TagKeys = Query(..., alias='tagKeys'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
