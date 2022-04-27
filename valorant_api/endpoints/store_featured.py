from typing import Union

from valorant_api.endpoints_config import EndpointsConfig
from valorant_api.responses.error_response import ErrorResponse
from valorant_api.responses.store_featured import StoreFeaturedV1
from valorant_api.utils.fetch_endpoint import fetch_endpoint


def get_store_featured_v1(**kwargs) -> Union[StoreFeaturedV1, ErrorResponse]:
    return get_store_featured("v1", **kwargs)


def get_store_featured(version: str, **kwargs) -> Union[StoreFeaturedV1, ErrorResponse]:
    response = fetch_endpoint(
        EndpointsConfig.STORE_FEATURED,
        version=version,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        return ErrorResponse.from_dict(**response_data)

    return StoreFeaturedV1.from_dict(**response_data["data"])
