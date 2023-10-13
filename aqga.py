import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = 'my_api_key'

# Define a function to ask questions
def ask_question(question):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        max_tokens=150,
    )
    return response.choices[0].text

while True:
    user_input = input("Ask a question (type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    answer = ask_question(user_input)
    print("Answer:", answer)
