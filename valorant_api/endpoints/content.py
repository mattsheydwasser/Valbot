from typing import Union

from valorant_api.endpoints_config import EndpointsConfig
from valorant_api.responses.content import ContentV1
from valorant_api.responses.error_response import ErrorResponse
from valorant_api.utils.fetch_endpoint import fetch_endpoint


def get_content_v1(**kwargs) -> Union[ContentV1, ErrorResponse]:
    return get_content("v1", **kwargs)


def get_content(version: str, **kwargs) -> Union[ContentV1, ErrorResponse]:
    response = fetch_endpoint(
        EndpointsConfig.CONTENT,
        version=version,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        return ErrorResponse.from_dict(**response_data)

    return ContentV1.from_dict(**response_data)
