import openai
import pandas as pd
import datetime
from utils import GPT_API_KEY

now = datetime.datetime.now()
openai.api_key = GPT_API_KEY
gpt = []
inp = []

while True:
        uinp = input('\nI am GPT ask me anything!\nType quit, if you want to quit the program.\n\n\n')
        df = pd.DataFrame(list(zip(inp, gpt)), columns=['input', 'response'])
        if uinp == 'quit':
            print('Thanks for using GPT')
            df.to_csv(f"chat{now.date()}GPTresult.csv")
            break
        
        def chatbot_response(user_input):
            response = openai.Completion.create(engine="text-davinci-003", prompt=user_input, max_tokens=1000, temperature=1)
            inp.append(user_input)
            gpt.append(response['choices'][0]['text'])
            return response['choices'][0]['text']
        print(chatbot_response(uinp))
        
