from typing import List, Union

from valorant_api.endpoints_config import EndpointsConfig
from valorant_api.responses.error_response import ErrorResponse
from valorant_api.responses.website import WebsiteBannerV1
from valorant_api.utils.fetch_endpoint import fetch_endpoint


def get_website_v1(
    countrycode: str, **kwargs
) -> Union[List[WebsiteBannerV1], ErrorResponse]:
    return get_website("v1", countrycode, **kwargs)


def get_website(
    version: str, countrycode: str, **kwargs
) -> Union[List[WebsiteBannerV1], ErrorResponse]:
    response = fetch_endpoint(
        EndpointsConfig.WEBSITE,
        version=version,
        countrycode=countrycode,
        **kwargs,
    )
    response_data = response.json()

    if response.ok is False:
        return ErrorResponse.from_dict(**response_data)

    return [WebsiteBannerV1.from_dict(**banner) for banner in response_data["data"]]
