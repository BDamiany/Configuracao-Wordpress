from locust import HttpUser, TaskSet, task, between

class UserTasks(TaskSet):

    @task(1)
    def post_imagem_1mb(self):
        self.client.get("/2026/04/28/imagem-1mb/")

    @task(1)
    def post_texto_400kb(self):
        self.client.get("/2026/04/28/texto-400kb/")

    @task(1)
    def post_imagem_300kb(self):
        self.client.get("/2026/04/28/imagem-300kb/")

class WebsiteUser(HttpUser):
    tasks = [UserTasks]
    wait_time = between(1, 3)
