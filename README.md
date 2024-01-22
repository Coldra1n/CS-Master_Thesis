# Adapting pretrained Text-to-Text models for long scientific document summarization
Master’s thesis in the field of Cognitive Science. The thesis was written under the supervision of 
Dr.Adam Zadrożny PhD National Centre for Nuclear Research and Dr.Anna Anzulewicz PhD Department of Developmental Psychology.

*Summary* :
This research conducted an in-depth adaptation and comparative evaluation of two prominent 
AI models: LONGT5 and LLaMA2. The study compared traditionally full parameters fine-tuned 
LONGT5 with parameter efficient fine-tuning(PEFT) of LLaMA 2. Among PEFT methods we focused on the Llama adapter, prefix tunning, LoRA, and QLoRa where LoRa
showed the best results in terms of efficiency, stability and accuracy. Through diverse metrics, 
LONGT5 showed superiority in ROUGE scores, highlighting its strength in capturing textual 
overlaps. Conversely, LLaMA2 excelled in BARTScores, emphasizing its ability to retain original content's semantic richness. Token length preferences revealed LONGT5's inclination for 
concise outputs (316 tokens) while LLaMA2 favored more detailed summaries (512 tokens). The 
research overviews a trade-off between quantization during inference and the accuracy of generated 
summaries. Advanced generation strategies, such as Contrastive and Beam Search, outperformed 
the basic Greedy method. The main result - Both LONGT5 and LLaMA2 showed strong results 
in the summarization of long scientific documents, nonetheless LLaMA2 offers  more versatility and is more cost-effective.
Models have their zones of strengths and 
weaknesses, with each model shining under specific conditions and metrics.
