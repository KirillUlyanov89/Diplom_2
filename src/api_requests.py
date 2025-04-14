import allure
import requests
import src.helpers
import src.urls

@allure.step('Регистрация нового пользователя и получение его данных')
def create_user_and_collect_user_data():
    user_data = src.helpers.generate_user_data()
    response = requests.post(src.urls.CREATE_USER_URL, data=user_data)
    if response.status_code == 200:
        return user_data
    
@allure.step('Удаление пользователя по токену')
def delete_user(token):
    requests.delete(src.urls.DELETE_USER_URL, headers={"Authorization": f'{token}'})