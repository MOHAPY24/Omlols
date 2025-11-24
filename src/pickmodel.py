import wrapper.ollw as ollama
import utils
from prompt_toolkit import PromptSession
import config


session = PromptSession()


def pick_model():
    client = ollama.Client()
    models = client.list_ollama_models()
    print(utils.format_list(models))
    try:
        if config.get_config()["default_model"] != None and config.get_config()["default_model"] != "":
            stock = input("Would you like to use your stock model from your config? (Y/n) > ")
            if stock == "" or stock.lower() == "y":
                try:
                    return models[models.index(config.get_config()["default_model"])]
                except:
                    print("[X] Invalid model name")
                    return ""
            else:
                pass

        text = session.prompt('(Space for Tinyllama) > ')

        if text.lower() == 'exit':
            print("Quitting..")
            return ""

        if text.lower() == "" or text.lower() == " ":
            return "tinyllama:latest"
        
        try:
            return models[models.index(text.lower())]
        except:
            print("[X] Invalid model name")
            return ""
            
        


    except EOFError:  # Ctrl+D
        print("Quitting..")
        return ""
    except KeyboardInterrupt:  # Ctrl+C
        pass

