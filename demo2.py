
import openai

API_KEY = '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'

openai.api_key = API_KEY

prompt = "The quick brown fox"
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

generated_text = response.choices[0].text.strip()
print(generated_text)
