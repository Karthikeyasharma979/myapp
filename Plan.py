import os 
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain 
from langchain.chains import LLMMathChain

os.environ["GOOGLE_API_KEY"]=" AIzaSyDmZRXIkfaxY5c0BzBPO-1RtNhA9kEInNQ"
def plan(age, height, weight, purpose):
    llm = GoogleGenerativeAI(model="gemini-pro")
    ptemp = PromptTemplate(
        input_variables=['Age', 'Height', 'Weight', 'Purpose'],
        template="""
        Age: {Age}
        Height: {Height}
        Weight: {Weight}
        Purpose: {Purpose}
        Create a diet plan using the above information for a one-month period.
        """
    )
    
    chain = LLMChain(llm=llm, prompt=ptemp)
    res = chain.run({'Age': age, 'Height': height, 'Weight': weight, 'Purpose': purpose})
    return res['text']



def call(age,height,weight):
    llm  = GoogleGenerativeAI(model="gemini-pro")
    chain = LLMMathChain(llm=llm,verbose=True)
    res = chain.run("What is height after 10 years")
    return res
    

# print(cal("18","6feet","80","to loss the  weight"))
