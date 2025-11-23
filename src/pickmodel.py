import wrapper.ollw as ollama
import utils
from prompt_toolkit import PromptSession


session = PromptSession()


def pick_model():
    client = ollama.Client()
    models = client.list_ollama_models()
    print(utils.format_list(models))
    try:
        text = session.prompt('(Space for Tinyllama) > ')

        if text.lower() == 'exit':
            print("Quitting..")
            exit(0)

        if text.lower() == "" or text.lower() == " ":
            return "tinyllama:latest"
        
        try:
            return models[models.index(text.lower())]
        except:
            print("[X] Invalid model name")
            return ""
            
        


    except EOFError:  # Ctrl+D
        print("Quitting..")
        exit(0)
    except KeyboardInterrupt:  # Ctrl+C
        pass

