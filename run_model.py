from langchain import PromptTemplate
from langchain import LLMChain
from langchain.llms import LlamaCpp


# B is for beginning and E is for Ending , INST is for instrction and SYS is for System

B_INST, E_INST = "[INST]", "[/INST]"
B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"

DEFAULT_SYSTEM_PROMPT = """"
You are a helpful, respectful and honest assistant. Always answer as helpful as possible, while being safe.
Your answer should not include any harmful, unethical, racist, sexist, toxic, dangerous or illegal content.
Please ensure that your responses are socially unbiased and positive in nature.
If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct.
If you dont know the answer to a question, please dont share false information.
"""


instruction = "Convert the following from English to Hindi: \n\n {text}"


SYSTEM_PROMPT = B_SYS + DEFAULT_SYSTEM_PROMPT + E_SYS

template = B_INST + SYSTEM_PROMPT + instruction + E_INST
#print(template)

prompt = PromptTemplate(template = template, input_variables=["text"])

#load the model

llm = LlamaCpp(
    model_path = "model/llama-2-7b-chat.Q4_0.gguf",
    max_tokens = 50,
    temperature = 0.01,
    n_ctx=1024,
    n_batch = 8
    
)


llm_chain = LLMChain(prompt=prompt, llm=llm)

response = llm_chain.run("How are you?")
print(response)