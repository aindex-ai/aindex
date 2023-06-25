import requests
import json
import os

class Aindex:
    def __init__(self):
        self.functions = self._get_functions()

    def _get_functions(self):
        repo_url = "https://api.github.com/repos/aindex-ai/functions/contents/functions"
        response = requests.get(repo_url)
        files = response.json()

        functions = {}
        for file in files:
            if file['name'].endswith(".json"):
                function_name = os.path.splitext(file['name'])[0]
                file_content = requests.get(file['download_url']).json()
                functions[function_name] = file_content

        return functions

    def __getattr__(self, attr):
        if attr in self.functions:
            return self.functions[attr]
        raise AttributeError(f"No such attribute: {attr}")

# Automatic instantiation upon import
aindex = Aindex()