# This file will be the Open AI playground file.
# Docs: https://developers.openai.com/
#       https://developers.openai.com/api/reference/overview

from openai import OpenAI

client = OpenAI()

def gen_answer(question):
  response = client.responses.create(
      model = "gpt-5.4-mini",
      input =  question
  )
  # print(response.output_text)
  # print(response.usage)
  return response.output_text

# This is basically the code but it won't work unless you have the API key from OpenAI
# and to run it you will need to create an account on OpenAI services and create your open API key. 
# You will also need to import the api data on the project. 


while True:
  question = input("What do you wanna know ?")
  if (question == "sair"):
    break
  answer = gen_answer(question)
  #print(response.output_text)