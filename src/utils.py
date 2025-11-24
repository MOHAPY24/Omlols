import time
from colorama import Fore, init, Style
from itertools import cycle
import sys

init(True)
def format_list(listr:list):
    return str(listr).replace(']', '').replace('[', '    \n').replace(',', '\n').replace("'", '').strip()

def printdy(text, colorama1=Fore.WHITE):
  for i in text:
    if i.isdigit():
      print(colorama1 + Style.BRIGHT + i + Style.RESET_ALL, end='', flush=True)
    else:
      print(colorama1 + i + Style.RESET_ALL, end='', flush=True)
    time.sleep(0.034)
  time.sleep(2)
  print("")
  return None

#def loading_spinner(message=""):
#    spinner_frames = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
#    for frame in cycle(spinner_frames):
#        sys.stdout.write(f'\r{message} {frame}')
#        sys.stdout.flush()
#        time.sleep(0.1)