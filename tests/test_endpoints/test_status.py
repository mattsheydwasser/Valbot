import pytest
import responses
from hypothesis import given
from hypothesis import strategies as st

import valo_api
from tests.test_endpoints.utils import (
    get_error_responses,
    get_mock_response,
    validateException,
)
from valo_api.config import Config
from valo_api.exceptions.valo_api_exception import ValoAPIException


@given(version=st.sampled_from(["v1"]), region=st.sampled_from(Config.ALL_REGIONS))
@responses.activate
def test_get_status(version: str, region: str):
    print(f"Test get_status with: {locals()}")

    url = f"{Config.BASE_URL}/valorant/{version}/status/{region}"

    responses.add(
        responses.GET,
        url,
        json=get_mock_response(f"status_{version}.json"),
        status=200,
    )

    getattr(valo_api, f"get_status_{version}")(region=region)
    assert len(responses.calls) == 1

    getattr(valo_api, "get_status")(version=version, region=region)
    assert len(responses.calls) == 2


@given(
    version=st.sampled_from(["v1"]),
    region=st.sampled_from(Config.ALL_REGIONS),
    error_response=st.sampled_from(get_error_responses("status")),
)
@responses.activate
def test_get_status_error(version: str, region: str, error_response: dict):
    print(f"Test get_status_error with: {locals()}")

    url = f"{Config.BASE_URL}/valorant/{version}/status/{region}"

    responses.add(
        responses.GET,
        url,
        json=error_response,
        status=int(error_response["status"]) if "status" in error_response else 500,
    )

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, f"get_status_{version}")(region=region)
    assert len(responses.calls) == 1
    validateException(error_response, excinfo)

    with pytest.raises(ValoAPIException) as excinfo:
        getattr(valo_api, "get_status")(version=version, region=region)
    assert len(responses.calls) == 2
    validateException(error_response, excinfo)


if __name__ == "__main__":
    test_get_status()
    test_get_status_error()
