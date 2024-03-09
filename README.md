# Fine-Tuning Large Language Models (LLMs)

**Welcome! Here, you'll discover how to fine-tune any LLM for your specific needs using your own dataset. Whether it's for your shop, office, school, or any other business, you can create a custom Q&A chatbot tailored to your requirements. Let's dive into how you can structure a chat template and fine-tune an LLM model using Hugging Face Transformers.**



## Fine-Tuning Models (Train on Custom DataSet Code)

| Content                                       | Resources |
| ------------------------------------------- | :-------: |
| 1) Fine Tune Llama 2 Chat Model (Code)      | [🔗](#)  |
| 2) Fine Tune Gemma 2b-it Chat Model (Code)  | [🔗](#)  |



### Fine Tuning Llama 2 Steps:

| Steps                                                        | Description                                               | Resources                                                                             |
| ----------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| 1) Prepare the txt file containing questions and answers    | Collect and organize questions and corresponding answers  | [🔗](#) Example of dataset                                                            |
| 2) Format the txt file into Llama Accepting Template CSV        | Convert the data into a format compatible with Llama 2    | [🔗](#) Example of Llama accepting template data<br><br>[🔗](#) Code for formation of llama accepting CSV |
| 3) Upload the Llama Accepting Csv file into Hugging Face dataset repo | Share the dataset in hugging face repo to use it in training directly  | -                                                                                     |
| 4) Run the Jupyter Code for Tuning the Llama 2 with just prepared dataset | Execute the code to fine-tune Llama 2 with the prepared dataset | [🔗](#) Train Code                                                                 |
| 5) Test the Tuned model                                      | Evaluate the performance of the fine-tuned model          | [🔗](#) Test Code                                                                    |

### Fine Tuning Gemma Steps:

| Steps                                                        | Description                                               | Resources                                                                             |
| ----------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| 1) Prepare the txt file containing questions and answers    | Collect and organize questions and corresponding answers  | [🔗](https://github.com/mirajdeepbhandari/GenAI_Reference/blob/main/llm%20finetuning/gemma%202b-it%20model/yungridataset.txt) Example of dataset                                                            |
| 2) Format the txt file into Gemma Accepting Template CSV        | Convert the data into a format compatible with Gemma    | [🔗](https://huggingface.co/datasets/mirajbhandari/gemma_2b_it_dataset) Example of Gemma accepting template data<br><br>[🔗](https://github.com/mirajdeepbhandari/GenAI_Reference/blob/main/llm%20finetuning/gemma%202b-it%20model/Dataset_formation_for_gemma.ipynb) Code for formation of Gemma accepting CSV |
| 3) Upload the Gemma Accepting Csv file into Hugging Face dataset repo | Share the dataset in Hugging Face repo to use it in training directly  | -                                                                                     |
| 4) Run the Jupyter Code for Tuning Gemma with just prepared dataset | Execute the code to fine-tune Gemma with the prepared dataset | [🔗](https://github.com/mirajdeepbhandari/GenAI_Reference/blob/main/llm%20finetuning/gemma%202b-it%20model/gemma_2b_it_finetune.ipynb) Train Code                                                                 |
| 5) Test the Tuned model                                      | Evaluate the performance of the fine-tuned model          | [🔗](https://github.com/mirajdeepbhandari/GenAI_Reference/blob/main/llm%20finetuning/gemma%202b-it%20model/testing%20the%20fine%20tuned%20gemma%20chat%20model/Testing_gemma_fine_Tuning_model.ipynb) Test Code    |


# Contributing
We welcome contributions! If you'd like to contribute to this project, whether it's by suggesting improvements, opening issues, or submitting pull requests, please feel free to do so. Your input is valuable in making this resource even better.
