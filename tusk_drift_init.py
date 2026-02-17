import os
from drift import TuskDrift

TuskDrift.initialize(
    env="development",
    log_level="debug",
    api_key=os.environ.get("TUSK_API_KEY"),
)
