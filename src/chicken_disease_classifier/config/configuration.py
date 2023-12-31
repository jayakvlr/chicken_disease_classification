from chicken_disease_classifier.constants import *
from chicken_disease_classifier.entity.callback_config import PrepareCallBackConfig
from chicken_disease_classifier.entity.dataingestionconfig import DataIngestionConfig
from chicken_disease_classifier.entity.modelconfig import PrepareBaseModelConfig
from chicken_disease_classifier.utils.common import read_yaml,create_directories

class ConfigurationManager:
    def __init__(self,config_filepath=CONFIG_FILE_PATH,params_filepath=PARAMS_FILE_PATH):
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config=self.config.data_ingestion
        create_directories([config.root_dir])
        get_data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return get_data_ingestion_config
    
    def get_prepare_base_model_config(self)->PrepareBaseModelConfig:
        config=self.config.prepare_base_model
        create_directories([config.root_dir])
        base_model_config=PrepareBaseModelConfig(
        root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weight=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )
        return base_model_config  

    def prepare_call_back_config(self)->PrepareCallBackConfig:
        config=self.config.prepare_callbacks
        model_ckpt_dir=os.path.dirname(config.checkpoint_model_filepath)
        create_directories([Path(model_ckpt_dir),Path(config.tensorboard_root_log_dir)])
        prepare_callback_config=PrepareCallBackConfig(
            root_dir=Path(config.root_dir),
            
            tensorboard_root_log_dir=Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath=Path(config.checkpoint_model_filepath))
        return prepare_callback_config 