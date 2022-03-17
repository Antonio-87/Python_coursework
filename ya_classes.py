import json

import requests

from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
    
    def upload_photo(self, disk_file_path, url):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "url": url}
        response = requests.post(upload_url, headers=headers, params=params)
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

    def create_file(self, file):
        with open('File_backup.json', 'w', encoding='utf-8') as new_file:
            json.dump(file,new_file)
