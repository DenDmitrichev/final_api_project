import allure


class EndPoint:
    url = 'http://memesapi.course.qa-practice.com/meme'
    response = None
    json = None

    def __init__(self, headers=None):
        self.headers = headers or {'Content-Type': 'application/json'}

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200, "Код ответа не 200"

    @allure.step('Check that response is 404')
    def check_that_status_is_404(self):
        assert self.response.status_code == 404, "Код ответа не 404"

    @allure.step('Check that response is 405')
    def check_that_status_is_405(self):
        assert self.response.status_code == 405, "Код ответа не 405"

    @allure.step('Check that response is 400')
    def check_that_status_is_400(self):
        assert self.response.status_code == 400, "Код ответа не 400"
