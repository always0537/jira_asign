from dataclasses import dataclass
from enum import Enum

class User(Enum):
    DD = '712020:18e6998f-bdc7-4baf-9174-96eaaf362739'
    WC = '712020:31cc91e3-e63a-40e7-8262-566848b91afd'
    EVA = '62cb96056eba719837215570'
    JEAN = '62007f1d6ba61b006fb4519b'
    MAX = '5c6b800c0a6eb0652cb1e4ea'
    NAVID = '5c4aadbcc694663913aa155a'
    VINCENT = '712020:1e8f94c5-5d0a-46a7-8d17-7e179be2045b'
    TZ = '712020:90a1b51d-a379-4e6b-963e-b6f78089fb8c'
    YUFFIE = '712020:901bc397-e5c0-4cbd-999d-5e620e41774a'

@dataclass
class AutomationDescription:
    environment: "Environment"
    google_driver_url: str
    jenkins_url: str

@dataclass
class DefectDescription:
    environment: "Environment"
    fix_version: str

@dataclass
class RegressionDescription:
    environment: "Environment"
    test_scope: str

class Environment(Enum):
    CLEAN_INSTALL_DOCKER_ENVIRONMENT = "Clean Install Docker Environment"
    ONLINE_UPGRADE_DOCKER_ENVIRONMENT = "Online Upgrade Docker Environment"
    OFFLINE_UPGRADE_DOCKER_ENVIRONMENT = "Offline Upgrade Docker Environment"