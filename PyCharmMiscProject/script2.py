from tdIf import classiffy_sentence
from mistral import ask_ollama
text="This comment seems offensive and should be banned"
classification = classiffy_sentence(text)
if classification=="True":
    ask_ollama(text)
else:
    print(text)