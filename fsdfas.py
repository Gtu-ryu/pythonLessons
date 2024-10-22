import os

def print_docs(directory):
    if os.path.exists(directory):
        for item in os.listdir(directory):
            path = os.path.join(directory, item)
            print(path)
            if os.path.isdir(path):
                print_docs(path)
    else:
        print(f"Директория {directory} не существует.")

print_docs('gug')
