import openai 

openai.api_key = "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"
def chat_with_gpt(prompt):
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
  ) 

  return response.choice[0].message.content.strip()

if __name__ == "__main__":
  while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
      break

    response = chat_with_gpt(user_input)
    print("Chatbot: ", response)
