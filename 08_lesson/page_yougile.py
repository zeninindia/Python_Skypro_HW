import requests
from dotenv import load_dotenv
import os


class PageYougile:
    def __init__(self, base_url):
        self.url = base_url
        load_dotenv()

    def sozdanie_project(self, title, user_id):
        url = f"{self.url}projects"
        key = os.getenv("KEY")
        token = f"bearer {key}"
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        data = {
            "title": title,
            "users": {user_id: "admin"}
        }

        response = requests.post(url, headers=headers, json=data)
        status_code = response.status_code
        project = response.json()
        print(status_code)
        print(project)
        return status_code, project

    def poluchenie_project(self, project_id):
        url = f"{self.url}projects/{project_id}"
        key = os.getenv("KEY")
        token = f"bearer {key}"

        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }

        response = requests.get(url, headers=headers)
        status_code = response.status_code
        project_id = response.json()
        print(status_code)
        print(project_id)
        return status_code, project_id

    def izminenie_project(self, project_id, new_title, user_id):
        url = f"{self.url}projects/{project_id}"
        key = os.getenv("KEY")
        token = f"bearer {key}"

        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        data = {
            "title": new_title,
            "users": {user_id: "admin"}
        }

        response = requests.put(url, headers=headers, json=data)
        status_code = response.status_code
        new_project_id = response.json()
        print(status_code)
        print(new_project_id)
        return status_code, new_project_id
