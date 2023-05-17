import os

def get_files_per_class(directory, class_name):
    files = []
    for file in os.listdir(directory):
        if file.startswith(class_name):
            files.append(f"{directory}/{file}")
    return files


def get_dict_with_files_per_class(directory):
    class_names = ["sunrise", "cloudy", "rain", "shine"]
    class_files = {}
    for i, name in enumerate(class_names):
        class_files[name] = get_files_per_class(directory, name)
    return class_files
