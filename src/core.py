import wrapper.ollw as ollama
import utils, pickmodel
import readplugins as rp
from prompt_toolkit import PromptSession
import os, time, sources


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


model = pickmodel.pick_model()
if model == "":
    quit(1)
os.system("clear")
client = ollama.Client(model)
directory_to_scan = 'src/plugins/'
plugins = rp.process_files_in_directory(directory_to_scan)
directory_to_scan = 'src/memory/sources'
sourcesr = rp.process_sources(directory_to_scan)
time.sleep(2)
os.system("clear")
try:
    text = session.prompt(f"Ask '{model}' >> ")
    prompt_with_sources = f"""
You are an AI system receiving the following structured inputs. Follow all rules carefully.

PLUGINS:
{plugins}

CHAT MEMORY (optional):
{memory}

EXTERNAL SOURCES (user explicitly mentioned one or more sources, so you may reference only those included):
{sourcesr}

IMPORTANT RULES:
• Only use the sources included above. 
• You must NOT invent or reference sources outside this list.
• When using these sources, clearly state which one you are referencing.

USER REQUEST:
{text}

Now respond using the user-requested sources when relevant.
"""
    prompt_without_sources = f"""
You are an AI system receiving the following structured inputs. Follow all rules carefully.

PLUGINS:
{plugins}

CHAT MEMORY (optional):
{memory}

IMPORTANT RULES:
• The user has not requested any external sources.
• You must NOT reference, mention, summarize, or use ANY external text sources.
• Ignore the existence of any external sources entirely.
• Do not cite anything unless it comes directly from the conversation or user.

USER REQUEST:
{text}

Now respond using only general knowledge and the conversation context.
"""

    if sources.user_mentions_source(text, sourcesr):
        response = client.prompt(prompt_with_sources)
    else:
        response = client.prompt(prompt_without_sources)


    if response.status_code == 200:
        response_data = response.json()
        memory.append(response.json()["response"])
        f.write(str(memory))
        print(response_data["response"])
    else:
        print(f"Error: {response.status_code} - {response.text}")
except KeyboardInterrupt:
    print("Quitting..")
    f.close()
    exit(0)
f.close()