import allure
import requests
import src.api_requests
import src.data
import src.helpers
import src.urls

class TestLoginUser:
    
    @allure.title('Проверка логина существующего пользователя')
    def test_login_user_with_correct_credentials_user_loged_in(self):
        user_data = src.api_requests.create_user_and_collect_user_data()
        response = requests.post(src.urls.LOGIN_USER_URL, data=user_data)
        
        assert response.status_code == 200
        assert src.data.USER_CREATED_MESSAGE in response.text
        
    @allure.title('Проверка невозможности логина пользователя с неверным Email')
    def test_login_user_with_wrong_email_user_not_loged_in(self):
        user_data = src.api_requests.create_user_and_collect_user_data()
        wrong_email = src.helpers.fake.email()
        password = user_data['password']
        corrupt_user_data = {
            'email': wrong_email,
            'password': password
        }
        response = requests.post(src.urls.LOGIN_USER_URL, data=corrupt_user_data)
        
        assert response.status_code == 401
        assert src.data.USER_NOT_FOUND_MESSAGE in response.text
        
    @allure.title('Проверка невозможности логина пользователя с неверным паролем')
    def test_login_user_with_wrong_password_user_not_loged_in(self):
        user_data = src.api_requests.create_user_and_collect_user_data()
        email = user_data['email']
        wrong_password = src.helpers.generate_random_string(12)
        corrupt_user_data = {
            'email': email,
            'password': wrong_password
        }
        response = requests.post(src.urls.LOGIN_USER_URL, data=corrupt_user_data)
        
        assert response.status_code == 401
        assert src.data.USER_NOT_FOUND_MESSAGE in response.text