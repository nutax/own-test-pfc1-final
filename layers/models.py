import openai
import time

class ChatGPTModel:
    def __init__(self, openai_api_key, model_name):
        openai.api_key = openai_api_key
        self.model_name = model_name
    
    def complete(self, prompt):
        while True:
            try:
                response = openai.ChatCompletion.create(
                    model=self.model_name,
                    messages=[{"role": "system", "content": "You are a logical entity. You evaluate reasoning problems."}, {"role":"user", "content": prompt}],
                    max_tokens=1024,
                    n=1,
                    stop=None,
                    temperature=0,
                )
                completion = response.choices[0].message.content.strip()
                return completion
            except Exception as e:
                print(f"An error occurred: {e}")
                print("Waiting 5 seconds...")
                time.sleep(5)
                print("Retrying...")


class GPTModel:
    def __init__(self, openai_api_key, model_name):
        openai.api_key = openai_api_key
        self.model_name = model_name
    
    def complete(self, prompt):
        while True:
            try:
                response = response = openai.Completion.create(
                    engine= self.model_name,
                    prompt=f""" System: You are a logical entity. You evaluate reasoning problems.
                    
                    {prompt}""",
                    max_tokens=1024,
                    temperature=0,
                    n=1,
                    stop=None
                )
                completion = response.choices[0].text.strip()
                return completion
            except Exception as e:
                print(f"An error occurred: {e}")
                print("Waiting 5 seconds...")
                time.sleep(5)
                print("Retrying...")