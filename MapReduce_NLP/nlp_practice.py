import nltk
from nltk import word_tokenize
text = word_tokenize("I enjoy biking on the trails")
# Get Part-of-speech tags for text
output = nltk.pos_tag(text)
print(output)
