from dataclasses import dataclass
from pathlib import Path

@dataclass
class PrepareBaseModelConfig:
    root_dir:Path
    base_model_path:Path
    updated_base_model_path : Path
    params_image_size:list
    params_learning_rate:float
    params_include_top:bool
    params_weight: str
    params_classes:int
