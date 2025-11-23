import requests, json

class Client:
    def __init__(self, model:str="tinyllama"):
        self.model = model
        self.URL = url = "http://localhost:11434"
        self.headers = {"Content-Type": "application/json"}

    def prompt(self, prompt:str):
        self.data = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        response = requests.post(self.URL+"/api/generate", headers=self.headers, data=json.dumps(self.data))
        return response
    


    def list_ollama_models(self):
        try:
            response = requests.get(f"{self.URL}/api/tags")
            response.raise_for_status()  
            models_data = response.json()

            if "models" in models_data:
                models = []
                for model in models_data["models"]:
                    models.append(f"{model['name']}")
                return models
            else:
                return []

        except requests.exceptions.ConnectionError:
            print("Error: Could not connect to Ollama. Is the Ollama server running?")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

            
    

