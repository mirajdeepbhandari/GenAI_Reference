
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate,PromptTemplate
from dotenv import load_dotenv
import os

# setting the api key from environment variable
load_dotenv()  # loading environment variable
api_key = os.getenv("GOOGLE_API_KEY")


def doc_words_join(inp):
   loader = PyPDFLoader(inp)
   pages = loader.load_and_split()
   # print(len(pages)) #no of pages in the documents
   whole_doc_text = ''
   for i in range(len(pages)):
       whole_doc_text+=pages[i].page_content
   return whole_doc_text




# propts setup for each chunks

chunks_prompt="""
Please summarize the below Document. The summary must be very clear with proper phrases and easy words:
Document:`{text}'
Summary:
"""
map_prompt_template=PromptTemplate(input_variables=['text'], template=chunks_prompt)



# propts setup for final summary

system = """You are a document summarizer chatbot. You are very experienced and can provide the summary in a very good way.
The documents may contain very complex words, which may be difficult to understand, so you have to use easy words while
summarizing the documents. If the document is not a textual document or you did not get any text,
display output="Sir, would you please provide a textual PDF?" and don't give random outputs.

Note: If the document has numerical values such as cost, price, rate, profit, loss, or anything, try to represent that also in the summary.

You have to follow this template while giving the summary. You have to give the summary from the user input only; don't give your opinion or content
which is not given by the user document or text.

Document: Title which may be suitable for the document (it should be at the center of the document)

Summary: Summary of the document must be at least 15 lines. Tell what the document is about.

Key Points:

a.
b.
c.
d.
e.
......... other key points.........
"""


human="{text}" # yo ra mathi ko chunk prompt ma same hunparxa input field ko name

final_combine_prompt=ChatPromptTemplate.from_messages([SystemMessagePromptTemplate.from_template(system),
                                                 HumanMessagePromptTemplate.from_template(human)])



def summarize(inp):

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    text_chunks = text_splitter.create_documents([inp])

    llm_model = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key) 

    summary_chain = load_summarize_chain( llm=llm_model, chain_type='map_reduce', map_prompt=map_prompt_template, combine_prompt=final_combine_prompt,
                                         verbose=False)
    
    output = summary_chain.invoke(text_chunks)  

    return output




    
 
