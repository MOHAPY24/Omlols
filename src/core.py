import wrapper.ollw as ollama
import utils, pickmodel
import readplugins as rp
from prompt_toolkit import PromptSession
import os, time, sources, config
#import threading



session = PromptSession()
memory = []
try:
    r = open("src/memory/chatmem.chat", 'r')
except FileNotFoundError:
    f = open("src/memory/chatmem.chat", 'w')
    f.close()
    r = open("src/memory/chatmem.chat", 'r')
memory = [r.read()]
r.close()
f = open("src/memory/chatmem.chat", 'w')
conf = config.get_config()
if conf["verbose"] == True:
    print("VERBOSE: Got chat memory")
model = pickmodel.pick_model()
if model == "":
    quit(1)
os.system("clear")
if conf["verbose"] == True:
    print("VERBOSE: Got model")
client = ollama.Client(model)
if conf["verbose"] == True:
    print("VERBOSE: Created OLLAMA client")
directory_to_scan = 'src/plugins/'
plugins = rp.process_files_in_directory(directory_to_scan)
if conf["verbose"] == True:
    print("VERBOSE: Got plugins")
directory_to_scan = 'src/memory/sources'
sourcesr = rp.process_sources(directory_to_scan)
if conf["verbose"] == True:
    print("VERBOSE: Got sources")
time.sleep(2)
os.system("clear")
while True:
    try:
        text = session.prompt(f"Ask '{model}' >> ")
        prompt_with_sources = f"""
    You are an AI system receiving the following structured inputs. Follow all rules carefully.

    USERNAME:
    {conf["username"]} (If empty use 'User')

    PLUGINS:
    {plugins}

    CHAT MEMORY (optional):
    {memory}

    EXTERNAL SOURCES (user explicitly mentioned one or more sources, so you may reference only those included):
    {sourcesr}

    IMPORTANT RULES:
    • Only respond to the user, do not add anything else
    • Only use the sources included above. 
    • You must NOT invent or reference sources outside this list.
    • When using these sources, clearly state which one you are referencing.

    USER REQUEST:
    {text}

    Now respond using the user-requested sources when relevant.
    """
        prompt_without_sources = f"""
    You are an AI system receiving the following structured inputs. Follow all rules carefully.

    USERNAME:
    {conf["username"]} (If empty use 'User')

    PLUGINS:
    {plugins}

    CHAT MEMORY (optional):
    {memory}

    IMPORTANT RULES:
    • Only respond to the user, do not add anything else
    • Do not cite anything unless it comes directly from the conversation or user.

    USER REQUEST:
    {text}

    Now respond using only general knowledge and the conversation context.
    """
        #stop_event = threading.Event()
        #def run_spinner():
            #while not stop_event.is_set():
                #utils.loading_spinner()

        #spinner_thread = threading.Thread(target=run_spinner)
        #spinner_thread.start()
        if sources.user_mentions_source(text, sourcesr):
            response = client.prompt(prompt_with_sources)
            if conf["verbose"] == True:
                print("VERBOSE: Checked if source is needed, needed, sent prompt")
        else:
            response = client.prompt(prompt_without_sources)
            if conf["verbose"] == True:
                print("VERBOSE: Checked if source is needed, not needed, sent prompt")


        if response.status_code == 200:
            #stop_event.set()
            #spinner_thread.join()
            if conf["verbose"] == True:
                print("VERBOSE: recived response")
            response_data = response.json()
            memory.append(response.json()["response"])
            f.write(str(memory))
            utils.printdy(response_data["response"])
        else:
            #stop_event.set()
            #spinner_thread.join()
            print(f"Error: {response.status_code} - {response.text}")
    except KeyboardInterrupt:
        print("Quitting..")
        #stop_event.set()
        #spinner_thread.join()
        f.close()
        exit(0)
f.close()