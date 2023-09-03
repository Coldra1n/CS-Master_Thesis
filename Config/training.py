
from dataclasses import dataclass
from typing import ClassVar


@dataclass # for testing on 1 GPU/for training
class train_config:
    model_name: str="NousResearch/Llama-2-7b-hf"
    enable_fsdp: bool=False #True
    low_cpu_fsdp: bool=False 
    run_validation: bool=True
    batch_size_training: int=4 #128
    num_epochs: int=1 #3
    num_workers_dataloader: int=1
    lr: float=1e-4
    weight_decay: float=0.0
    gamma: float= 0.85
    seed: int=39
    use_fp16: bool=False
    mixed_precision: bool=True
    val_batch_size: int=64
    dataset = "scientific_papers_dataset"
    micro_batch_size: int=4  64,128
    peft_method: str = "lora" # None , llama_adapter, prefix
    use_peft: bool=True #False
    output_dir: str = "PATH/to/save/PEFT/model"
    freeze_layers: bool = False
    num_freeze_layers: int = 1
    quantization: bool = True #False
    one_gpu: bool = False #True
    save_model: bool = True
    dist_checkpoint_root_folder: str="PATH/to/save/FSDP/model" # will be used if using FSDP
    dist_checkpoint_folder: str="fine-tuned" # will be used if using FSDP
    save_optimizer: bool=True # will be used if using FSDP
    use_fast_kernels: bool = True # Enable using SDPA from PyTroch Accelerated Transformers, make use Flash Attention and Xformer memory-efficient kernels

    
    
    
