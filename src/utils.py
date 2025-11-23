def format_list(listr:list):
    return str(listr).replace(']', '').replace('[', '    \n').replace(',', '\n').replace("'", '').strip()