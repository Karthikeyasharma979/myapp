import os 
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain 
from langchain.chains import LLMMathChain

os.environ["GOOGLE_API_KEY"]=""
def plan(age, height, weight, purpose,sugar,bp):
    llm = GoogleGenerativeAI(model="gemini-pro")
    ptemp = PromptTemplate(
        input_variables=['Age', 'Height', 'Weight', 'Purpose','Sugar','Bp'],
        template="""
        Age: {Age}
        Height: {Height}
        Weight: {Weight}
        Purpose: {Purpose}
        sugar:{Sugar}
        bp:{Bp}
        Create a diet plan using the above information for a one-month period.
        """
    )
    
    chain = LLMChain(llm=llm, prompt=ptemp)
    res = chain.run({'Age': age, 'Height': height, 'Weight': weight, 'Purpose': purpose,'Sugar':sugar,'Bp':bp})
    return res
