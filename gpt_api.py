import requests


class GptApi:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url
        self.messages = [
            {
                "role": "system",
                "content": "You are ChatGPT, a large language model trained by OpenAI.",
            }
        ]

    def send_message(self, message):
        self.messages.append({"role": "user", "content": message})
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"model": "gpt-4", "messages": self.messages}
        response = requests.post(
            self.api_url,
            json=data,
            headers=headers,
        )
        data = response.json()

        self.messages.append(
            {"role": "system", "content": data["choices"][0]["message"]["content"]}
        )

        return data["choices"][0]["message"]["content"]
