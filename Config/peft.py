from dataclasses import dataclass, field
from typing import ClassVar, List

@dataclass
class lora_config:
     r: int=64 #{8,32,64}(small,medium,big)
     lora_alpha: int=32
     target_modules: ClassVar[List[str]]= ["q_proj", "v_proj"]
     bias= "none"
     task_type: str= "CAUSAL_LM"
     lora_dropout: float=0.05
     inference_mode: bool = False

@dataclass
class llama_adapter_config:
     adapter_len: int= 10
     adapter_layers: int= 30 #{2, 16,64} (small,medium,big))
     task_type: str= "CAUSAL_LM"

@dataclass
class prefix_config:
     num_virtual_tokens: int=32 #{32, 64, 128}(small,medium,big)
     task_type: str= "CAUSAL_LM"    
