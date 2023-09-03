import datasets
from .utils import Concatenator

def get_preprocessed_scientific_papers_dataset(dataset_config, tokenizer, split):
    dataset = datasets.load_dataset("scientific_papers","pubmed", split=split)

    prompt = (
        f"Summarize this article:\n{{article}}\n---\nSummary:\n{{summary}}{{eos_token}}"
    )

    def apply_prompt_template(sample):
        return {
            "text": prompt.format(
                article=sample["article"],
                summary=sample["abstract"],
                eos_token=tokenizer.eos_token,
            )
        }

    dataset = dataset.map(apply_prompt_template, remove_columns=list(dataset.features))

    dataset = dataset.map(
        lambda sample: tokenizer(sample["text"]),
        batched=True,
        remove_columns=list(dataset.features),
    ).map(Concatenator(), batched=True)
    return dataset
