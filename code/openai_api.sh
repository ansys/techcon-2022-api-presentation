curl https://api.openai.com/v1/completions \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
  "model": "text-davinci-002",
  "prompt": "Say this is a test",
  "max_tokens": 6,
}'
