import sys
import requests

path = '/usr/share/dict/words'
country = 'US'

if len(sys.argv) > 1:
  path = sys.argv[1]

if len(sys.argv) > 2:
  country = sys.argv[2]

# Build list of words
with open(path, 'r') as f:
  words = [line.strip() for line in f]

# Test words
for word in words:
  payload = {'term': word, 'country': country}
  r = requests.get('https://tastethefeeling.coca-cola.com/api/profanity', params=payload)
  if len(r.content) != 2:
    print word, " is blocked."
