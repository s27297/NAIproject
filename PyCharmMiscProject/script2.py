from tdIf import classiffy_sentence
from mistral import ask_ollama
text=input("Enter a sentence: ")
classification = classiffy_sentence(text)
print (classification)
if classification=="True":
    print(ask_ollama(text))
else:
    print(text)
