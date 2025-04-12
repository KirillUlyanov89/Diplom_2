import allure
import requests
import src.data
import src.helpers
import src.urls
import src.api_requests

class TestCreateUser:
    
    @allure.title('Проверка создания пользователя')
    def test_create_user_with_all_fields_user_created(self):
        user_data = src.helpers.generate_user_data()
        response = requests.post(src.urls.CREATE_USER_URL, data=user_data)
        
        assert response.status_code == 200
        assert src.data.USER_CREATED_MESSAGE in response.text
        
    @allure.title('Проверка невозможности создания пользователя, который уже зарегистрирован')
    def test_create_user_which_already_created_user_not_created(self):
        user_data = src.api_requests.create_user_and_collect_user_data()
        response = requests.post(src.urls.CREATE_USER_URL, data=user_data)
        
        assert response.status_code == 403
        assert src.data.USER_EXISTS_MESSAGE in response.text
        
    @allure.title('Проверка создания пользователя без заполненного поля Имя')
    def test_create_user_without_name_user_not_created(self):
        user_data = src.helpers.generate_user_data()
        email = user_data['email']
        password = user_data['password']
        corrupt_user_data = {
            'email': email,
            'password': password
        }
        response = requests.post(src.urls.CREATE_USER_URL, data=corrupt_user_data)
        
        assert response.status_code == 403
        assert src.data.MISSING_FIELDS_IN_USER_FORM_MESSAGE in response.text
        
    @allure.title('Проверка создания пользователя без заполненного поля Email')
    def test_create_user_without_email_user_not_created(self):
        user_data = src.helpers.generate_user_data()
        password = user_data['password']
        name = user_data['name']
        corrupt_user_data = {
            'password': password,
            'name': name
        }
        response = requests.post(src.urls.CREATE_USER_URL, data=corrupt_user_data)
        
        assert response.status_code == 403
        assert src.data.MISSING_FIELDS_IN_USER_FORM_MESSAGE in response.text
        
    @allure.title('Проверка создания пользователя без заполненного поля пароля')
    def test_create_user_without_password_user_not_created(self):
        user_data = src.helpers.generate_user_data()
        email = user_data['email']
        name = user_data['name']
        corrupt_user_data = {
            'email': email,
            'name': name
        }
        response = requests.post(src.urls.CREATE_USER_URL, data=corrupt_user_data)
        
        assert response.status_code == 403
        assert src.data.MISSING_FIELDS_IN_USER_FORM_MESSAGE in response.text