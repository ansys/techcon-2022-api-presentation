>>> import os
>>> import openai
>>> openai.api_key = os.getenv("OPENAI_API_KEY")
>>> response = openai.Completion.create(
...     model="text-davinci-002",
...     prompt="What is the answer to life the universe and everything?",
...     max_tokens=6,
...     temperature=1.0,
... )
>>> response['choices'][0]['text'].strip()
'42'
