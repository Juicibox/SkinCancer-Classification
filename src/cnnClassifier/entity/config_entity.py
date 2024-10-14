from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL1: str
    source_URL2: str
    local_data_file1: Path
    local_data_file2: Path
    unzip_dir: Path