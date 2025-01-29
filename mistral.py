import requests
import json

def ask_ollama(prompt, model="mistral"):
    url = "http://localhost:11434/api/chat"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": "Rephrase it in a more polite way and give me only new comment text: " + prompt}],
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        response_data = []
        for line in response.text.splitlines():
            try:
                response_data.append(json.loads(line))
            except json.JSONDecodeError:
                continue

        content = []
        for msg in response_data:
            if msg.get("done_reason") == "stop":
                content.append(msg["message"]["content"])
                break
            content.append(msg["message"]["content"])

        combined_content = "".join(content)

        return combined_content

    except requests.exceptions.RequestException as e:
        return f"Error while contacting Ollama: {e}"
    except ValueError as e:
        return f"Error processing JSON response: {e}"

if __name__ == "__main__":
    print("Welcome to the Mistral 7B console-based QA bot!")
    print("Enter 'exit' to quit.")

    while True:
        user_input = input("Your question: ")
        if user_input.lower() in ["exit"]:
            print("Goodbye!")
            break

        answer = ask_ollama(user_input)
        print(f"Answer: {answer}")
