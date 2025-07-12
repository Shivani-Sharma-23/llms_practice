from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = OpenAI(temperature=0.7)
prompt = PromptTemplate(input_variables=["topic"], template="Explain {topic} in simple terms.")
chain = LLMChain(llm=llm, prompt=prompt)

response = chain.run("computing")

