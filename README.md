# 1) Fine-Tuning Large Language Models (LLMs) ON Colab 100% Free GPU 

**Welcome! Here, you'll discover how to fine-tune any LLM for your specific needs using your own dataset. Whether it's for your shop, office, school, or any other business, you can create a custom Q&A chatbot tailored to your requirements. Let's dive into how you can structure a chat template and fine-tune an LLM model using Hugging Face Transformers.**
<br><br>

## 1.0 Cuda Setup With Pytorch to run LLM locally on your GPU

| Content                                       | Click Below |
| ------------------------------------------- | :-------: |
| a) Cuda Setup With Pytorch       | [🔗](https://github.com/mirajdeepbhandari/GenAI_Reference/blob/main/llm%20finetuning/cuda%20and%20pytourch%20setup%20for%20llm.pdf)  |

<br><br>
## 1.1) SFT Fine-Tuning on Models (Train on Custom DataSet Code)

| Content                                       | Click Below |
| ------------------------------------------- | :-------: |
| a) Fine Tune Llama 2 Chat Model (Code)      | [🔗](#fine-tuning-llama-2-steps)  |
| b) Fine Tune Gemma 2b-it Chat Model (Code)  | [🔗](#fine-tuning-gemma-steps)  |
| c) Fine Tune Mistral-7B For Chat (Code)   | [🔗](#fine-tuning-Mistral-steps)  |
| d) Unsloth Fine Tune Mistral-7b (code)           | [🔗](#fine-tuning-unsloth)  |

<br><br>
## 1.2) Find Chat Template for Fine-Tuning of any Models 
| Notebook File                               | Click Below |
| ------------------------------------------- | :-------: |
| Get Chat Template for llms for tuning (Code)| [🔗](https://github.com/mirajdeepbhandari/GenAI_Reference/blob/main/llm%20finetuning/formation_of_chat_template_of_any_llm.ipynb)  |


<br><br>
<a id="fine-tuning-llama-2-steps"></a>
### a) SFT Fine Tuning on Llama 2 Steps:

| Steps                                                        | Description                                               | Resources                                                                             |
| ----------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| 1) Prepare the txt file containing questions and answers    | Collect and organize questions and corresponding answers  | [🔗](https://github.com/mirajdeepbhandari/GenAI_Reference/blob/main/llm%20finetuning/llma%202%20chat%20model/qna%20deep%20dataset.txt) Example of dataset                                                            |
| 2) Format the txt file into Llama Accepting Template CSV        | Convert the data into a format compatible with Llama 2    | [🔗](https://huggingface.co/datasets/mirajbhandari/llama2_finetune_dataset) Example of Llama accepting template data<br><br>[🔗](https://github.com/mirajdeepbhandari/GenAI_Reference/blob/main/llm%20finetuning/llma%202%20chat%20model/Dataset_formation_for_llama.ipynb) Code for formation of llama accepting CSV |
| 3) Upload the Llama Accepting Csv file into Hugging Face dataset repo | Share the dataset in Hugging Face repo to use it in training directly  | -                                                                                     |
| 4) Run the Jupyter Code for Tuning the Llama 2 with just prepared dataset | Execute the code to fine-tune Llama 2 with the prepared dataset | [🔗](https://github.com/mirajdeepbhandari/GenAI_Reference/blob/main/llm%20finetuning/llma%202%20chat%20model/llma2chatfinetuning.ipynb) Train Code                                                                 |
| 5) Test the Tuned model                                      | Evaluate the performance of the fine-tuned model          | [🔗](https://github.com/mirajdeepbhandari/GenAI_Reference/blob/main/llm%20finetuning/llma%202%20chat%20model/testing%20the%20fine%20tuned%20llma2%20chat%20model/testing_llma2_after_fine_tuned.ipynb) Test Code |

<br><br>
<a id="fine-tuning-gemma-steps"></a>
### b) SFT Fine Tuning on Gemma Steps:

| Steps                                                        | Description                                               | Resources                                                                             |
| ----------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| 1) Prepare the txt file containing questions and answers    | Collect and organize questions and corresponding answers  | [🔗](https://github.com/mirajdeepbhandari/GenAI_Reference/blob/main/llm%20finetuning/gemma%202b-it%20model/yungridataset.txt) Example of dataset                                                            |
| 2) Format the txt file into Gemma Accepting Template CSV        | Convert the data into a format compatible with Gemma    | [🔗](https://huggingface.co/datasets/mirajbhandari/gemma_2b_it_dataset) Example of Gemma accepting template data<br><br>[🔗](https://github.com/mirajdeepbhandari/GenAI_Reference/blob/main/llm%20finetuning/gemma%202b-it%20model/Dataset_formation_for_gemma.ipynb) Code for formation of Gemma accepting CSV |
| 3) Upload the Gemma Accepting Csv file into Hugging Face dataset repo | Share the dataset in Hugging Face repo to use it in training directly  | -                                                                                     |
| 4) Run the Jupyter Code for Tuning Gemma with just prepared dataset | Execute the code to fine-tune Gemma with the prepared dataset | [🔗](https://github.com/mirajdeepbhandari/GenAI_Reference/blob/main/llm%20finetuning/gemma%202b-it%20model/gemma_2b_it_finetune.ipynb) Train Code                                                                 |
| 5) Test the Tuned model                                      | Evaluate the performance of the fine-tuned model          | [🔗](https://github.com/mirajdeepbhandari/GenAI_Reference/blob/main/llm%20finetuning/gemma%202b-it%20model/testing%20the%20fine%20tuned%20gemma%20chat%20model/Testing_gemma_fine_Tuning_model.ipynb) Test Code    |

<br><br>
<a id="fine-tuning-Mistral-steps"></a>
### c) SFT Fine Tuning on Mistral 7 billion parameters model on colab free GPU with Inference Steps:

| Steps                                                        | Description                                               | Resources                                                                             |
| ----------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| 1) Prepare the txt file containing questions and answers    | Collect and organize questions and corresponding answers  | [🔗](https://github.com/mirajdeepbhandari/GenAI_Reference/blob/main/llm%20finetuning/Mistral%207b%20Instruct%20v1%20model/TechVibedata.txt) Example of dataset                                                            |
| 2) Format the txt file into Mistral Accepting Template CSV  | Convert the data into a format compatible with Mistral   | [🔗](https://huggingface.co/datasets/mirajbhandari/mistral_dataset_for_tuning) Example of Mistral accepting template data<br><br>[🔗](https://github.com/mirajdeepbhandari/GenAI_Reference/blob/main/llm%20finetuning/Mistral%207b%20Instruct%20v1%20model/Dataset_formation_for_Mistral_7B.ipynb) Code for formation of mistral accepting CSV |
| 3) Upload the Mistral Accepting Csv file into Hugging Face dataset repo | Share the dataset in Hugging Face repo to use it in training directly  | -                                                                                     |
| 4) Run the Jupyter Code for Tuning the Mistral  with just prepared dataset and upload adapters containing files to hugging face models  | Execute the code to fine-tune Mistral  with the prepared dataset | [🔗](https://github.com/mirajdeepbhandari/GenAI_Reference/blob/main/llm%20finetuning/Mistral%207b%20Instruct%20v1%20model/Fine_Tuning_Mistral_7b_Instruct.ipynb) Train Code                                                                 |
| 5) Test the Tuned model by using PeftModel(Hugging Face) and Unsloth (useful for adapters only)                                      | Evaluate the performance of the fine-tuned model          | [🔗](https://github.com/mirajdeepbhandari/GenAI_Reference/tree/main/llm%20finetuning/Mistral%207b%20Instruct%20v1%20model/testing%20the%20fine%20tuned%20Mistral%207b%20Instruct%20chat%20model) Test Code |

<br><br>
<a id="fine-tuning-unsloth"></a>
### d) LLM Fine Tuning using Unsloth (Train and Test Codes)

| Steps                                                         | Resources                                                                            |
| -----------------------------------------------------------  |------------------------------------------------------------------------------------- |
| 1) Fine Tuning Train Code (Unsloth)    | [🔗](https://github.com/mirajdeepbhandari/GenAI_Reference/blob/main/llm%20finetuning/Unsloth%20Finetuning/unsloth_mistral_finetuning.ipynb) Train Code|   
| 2) Fine Tuning Test Code using Huggingface Transformers (merged model)    | [🔗](https://github.com/mirajdeepbhandari/GenAI_Reference/blob/main/llm%20finetuning/Unsloth%20Finetuning/testing_usloth_tuning_model_from_hugging_face.ipynb) Test Code|

<br><br>
# LLM Fine Tuning Theory and notes (coming nearly soon)

| Theory Topics                                                                                                                | Notes |
| ---------------------------------------------------------------------------------------------------------------------------- | :-------: |
| Quantization in llm                                                                                                          | [🔗](https://github.com/mirajdeepbhandari/GenAI_Reference/blob/main/llm%20finetuning/quantazationllmsnotes.pdf)  |
| LoRA: Low-Rank Adaptation && QLoRA: Quantized Low-Rank Adaptation                                                            | [🔗](#)  |
| Supervised fine-tuning (SFT)                                                                                                 | [🔗](#)  |
| Direct Preference Optimization (DPO)                                                                                         | [🔗](#)  |


<br><br>

# Contributing

We welcome contributions! If you'd like to contribute to this project, whether it's by suggesting improvements, opening issues, or submitting pull requests, please feel free to do so. Your input is valuable in making this resource even better.



### Created by Miraj Deep Bhandari 😍
