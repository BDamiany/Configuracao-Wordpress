from locust import HttpUser, task, between

class WordPressUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def index(self):
        self.client.get("/")

    @task(1)
    def wp_admin(self):
        self.client.get("/wp-admin/")

    @task(2)
    def wp_login(self):
        self.client.get("/wp-login.php")

    @task(1)
    def wp_api(self):
        self.client.get("/wp-json/wp/v2/posts")