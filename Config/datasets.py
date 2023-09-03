
from dataclasses import dataclass

@dataclass
class scientific_papers_dataset:
    dataset: str =  "scientific_papers_dataset"
    train_split: str = "train"
    test_split: str = "validation"
    input_length: int = 8192

