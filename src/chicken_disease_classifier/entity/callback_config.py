from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class PrepareCallBackConfig:
    root_dir:Path
    tensorboard_root_log_dir: Path
    checkpoint_model_filepath: Path