from dataclasses import dataclass

from valorant_api.utils.init_options import InitOptions


@dataclass
class VersionDetailsV1(InitOptions):
    version: str
    clientVersion: str
    branch: str
    region: str
