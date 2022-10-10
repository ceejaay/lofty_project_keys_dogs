from locust import HttpUser, task

class ListAllKeys(HttpUser):
    @task
    def all_keys(self):
        self.client.get("keys/")
