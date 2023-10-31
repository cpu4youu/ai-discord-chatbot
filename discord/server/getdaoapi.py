# Helpers
import os
import json
import argparse

# Dependencies
from langchain.llms import OpenAI

# Tool imports
from langchain.chains import APIChain

# Other
from langchain.globals import set_debug
from apidoc import apidoc

set_debug(False)

def getdaoapi(message):

  template = """
  To answer the following question, try to use the tool Alienworld API endpoints.

  There are 6 planets in Alien Worlds and they are: Neri, Kavian, Veles, Naron, Magor, and Eyeke. 

  Try to only give information about alien worlds. If the question is not about alien worlds, then 
  let the user know you cannot answer.

  {}
  """.format(message)

  api_docs = apidoc
  openai_api_key= os.getenv('OPENAI_API_KEY', 'sk-111111111111111111111111111111111111111111111111')
  os.environ["SERPAPI_API_KEY"] = "serpapi key"

  os.environ["OPENAI_API_BASE"] = "http://localhost/v1"
  llm = OpenAI(temperature=0, model_name='text-davinci-003', openai_api_key=openai_api_key)

  api_chain = APIChain.from_llm_and_api_docs(llm, api_docs, verbose=False)

  res = api_chain.run("{}".format(template))
  return res


def main():
    parser = argparse.ArgumentParser(description='Your program description here')
    parser.add_argument('message', help='The message for LLM processing')
    
    args = parser.parse_args()
    response = getdaoapi(args.message)
    #print("LLM Response:")
    print(response)

if __name__ == '__main__':
    main()
