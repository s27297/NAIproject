# NAIproject



```
Opis projektu
Projekt ma na celu stworzenie systemu moderacji komentarzy z wykorzystaniem dwóch wzajemnie uzupełniających się modeli sztucznej inteligencji. Modele te są rozwijane przez dwóch członków zespołu i współpracują, aby poprawić jakość komunikacji w komentarzach oraz pomóc użytkownikom w formułowaniu bardziej konstruktywnych wypowiedzi.
Tematyka projektu
Główne aspekty projektu:
	1	Sztuczna inteligencja i przetwarzanie języka naturalnego: opracowanie dwóch niezależnych modeli, które mogą ze sobą współdziałać.
	2	Moderacja treści online: stworzenie skutecznego narzędzia do zarządzania komentarzami.
	3	Edukacja użytkowników: poprawa umiejętności konstruktywnej komunikacji poprzez interakcję z systemem.
Zespół projektu
Artem Stakhovski s27297, Savely Zalessky s27146
Zespół składa się z dwóch członków:
	•	Pierwszy członek opracowuje model oceniający komentarze pod kątem tonu i treści (np. toksyczność, uprzejmość, konstruktywność).
	•	Drugi członek tworzy model, który proponuje ulepszenia komentarzy (np. łagodniejszy ton lub bardziej konstruktywne sformułowania).
Funkcjonalności (MoSC)
Must (funkcje konieczne):
	•	Model 1: Ocena komentarza według określonych kryteriów (toksyczność, konstruktywność itp.).
	•	Model 2: Generowanie propozycji ulepszeń komentarza na podstawie analizy pierwszego modelu.
	•	Współdziałanie modeli dla synchronicznej pracy.
Should (funkcje zalecane):
	•	Obsługa wielu języków.
	•	Panel administratora do konfiguracji kryteriów oceny i ulepszeń.
Could (funkcje opcjonalne):
	•	Wyświetlanie użytkownikowi wyjaśnień, dlaczego zaproponowano dane zmiany.
	•	Integracja z popularnymi platformami blogowymi.
Projekt ten ma na celu dostarczenie użytkownikom wygodnego narzędzia do poprawy komentarzy oraz pokazanie, jak dwa modele AI mogą skutecznie współpracować w rozwiązywaniu jednego zadania.

```












to connect to application you should run two projects in webstorm which can be found by links 
https://github.com/s27297/projektTFN
https://github.com/s27297/projektTBK
 and start database on mongodb on Port 27017:27017 but this canspend a lot of time
 also you need to run script,py in this repositorium

if you want to test only algoritm you can download project and run script1.py
# To run python code you need to install 5 libriaries
# scikit-learn,nltk,pandas,flask,flask-cors
# !pip install scikit-learn
# !pip install nltk
# !pip install pandas
# !pip install flask
# !pip install flask-cors


# models to classify:
# TdIfVector:
precision= 0.7295081967213115
recall= 0.664179104477612
accuracy= 0.74

# word2Vec:
precision= 0.5
recall= 0.3829787234042553
accuracy= 0.53

# BagOfWords:
precision= 0.6759259259259259
recall= 0.5140845070422535
accuracy= 0.6533333333333333

# Comment Rewriter

This is a simple script that interacts with the Ollama API to rewrite comments in a more polite way using the Mistral 7B model.

## Requirements

- Python 3.7+
- Ollama installed and running locally
- Internet connection (for downloading the Mistral model)

## Installation

### 1. Download and Install Ollama

Ollama is required to run the Mistral model locally. You can download it from:

- [Ollama official website](https://ollama.ai)

After downloading, follow the installation instructions for your operating system.

### 2. Run Ollama and Download the Model

Once Ollama is installed, open a terminal and run:

```sh
ollama pull mistral
```

This command will download the Mistral model, which is required for processing the text.

### 3. Install Python Dependencies

Ensure you have Python installed. Then, install the required dependencies:

```sh
pip install requests
```

### 4. Start the Ollama Server

Run Ollama in the background to handle API requests:

```sh
ollama serve
```

### 5. Run the Script

Now you can run the script:

```sh
python mistral.py
```

## Usage

- The script will prompt you to enter a comment.
- It will then send the comment to the Ollama API and return a more polite rewording.
- Type `exit` to quit the program.

## Troubleshooting

- If you encounter connection errors, ensure Ollama is running by checking:
  ```sh
  ps aux | grep ollama
  ```
- If the Mistral model is not found, try re-downloading it:
  ```sh
  ollama pull mistral
  ```
- Ensure your API server is accessible at `http://localhost:11434`.

## License

This project is open-source and free to use.



