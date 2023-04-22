import os
import openai

#selecting path for api key value
openai.api_key_path = "D:\CHATCORD\OpenAI\key.txt"

# openai.api_key = os.getenv("OPENAI_API_KEY")
while True:
  question = input("\033[34mWhat is your question?\n\033[0m")

  if question.lower() == "exit":
    print("\033[31mGoodbye!\033[0m")
    break
  completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
      {
        "role":"system",
        "content":"You are helpful assistant.Answer the given question."},
      {
        "role":"user",
        "content":question}
    ]
  )
  
  
  print("\033[32m" + completion.choices[0].message.content + "\n")