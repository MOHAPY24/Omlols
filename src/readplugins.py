import os


def process_files_in_directory(directory_path):
    plugins = []
    print("//////////////////////////")
    try:
        for entry_name in os.listdir(directory_path):
            full_path = os.path.join(directory_path, entry_name)

            if os.path.isfile(full_path):
                print(f"Processing file: {entry_name}")
                try:
                    with open(full_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        plugins.append(content)
                except Exception as e:
                    print(f"Error plugin: reading file {entry_name}: {e}")
                print(f"Processed file: {entry_name}")
            else:
                print(f"Skipping directory: {entry_name}")
        return plugins

    except FileNotFoundError:
        print(f"Error: Directory not found at {directory_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def process_sources(directory_path):
    sources = []
    print("////////////SOURCES//////////////")

    try:
        for entry_name in os.listdir(directory_path):
            full_path = os.path.join(directory_path, entry_name)

            if os.path.isfile(full_path):
                print(f"Processing file: {entry_name}")
                try:
                    with open(full_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        sources.append({
                            "name": entry_name.replace(".txt", ""),
                            "content": content
                        })
                except Exception as e:
                    print(f"Error reading file {entry_name}: {e}")

                print(f"Processed file: {entry_name}")

            else:
                print(f"Skipping directory: {entry_name}")

        return sources

    except FileNotFoundError:
        print(f"Error: Directory not found at {directory_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
