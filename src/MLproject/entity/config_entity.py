from dataclasses import dataclass # helps to mention class without self
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir:Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file: str
    unzip_data_dir: Path
    all_schema: dict
