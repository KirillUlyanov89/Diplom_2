import allure
import requests
import src.api_requests
import src.data
import src.helpers
import src.urls

class TestUpdateUser:
    
    @allure.title('Проверка изменения почты авторизованного пользователя')
    def test_update_user_email_with_auth_user_email_changed(self, get_user_token):
        token = get_user_token
        new_email = src.helpers.fake.email()
        new_user_data = {
            'email': new_email
        }
        response = requests.patch(src.urls.UPDATE_USER_DATA_URL, headers={"Authorization": f'{token}'}, data=new_user_data)
        
        assert response.status_code == 200
        assert src.data.USER_DATA_UPDATED_MESSAGE in response.text
        
    @allure.title('Проверка изменения пароля авторизованного пользователя')
    def test_update_user_password_with_auth_user_password_changed(self, get_user_token):
        token = get_user_token
        new_password = src.helpers.generate_random_string(12)
        new_user_data = {
            'password': new_password
        }
        response = requests.patch(src.urls.UPDATE_USER_DATA_URL, headers={"Authorization": f'{token}'}, data=new_user_data)
        
        assert response.status_code == 200
        assert src.data.USER_DATA_UPDATED_MESSAGE in response.text
        
    @allure.title('Проверка изменения имени авторизованного пользователя')
    def test_update_user_name_with_auth_user_name_changed(self, get_user_token):
        token = get_user_token
        new_name = src.helpers.fake.name()
        new_user_data = {
            'name': new_name
        }
        response = requests.patch(src.urls.UPDATE_USER_DATA_URL, headers={"Authorization": f'{token}'}, data=new_user_data)
        
        assert response.status_code == 200
        assert src.data.USER_DATA_UPDATED_MESSAGE in response.text
        
    @allure.title('Проверка изменений данных пользователя без авторизации')
    def test_update_user_data_without_auth_data_not_changed(self):
        new_email = src.helpers.fake.email()
        new_password = src.helpers.generate_random_string(12)
        new_name = src.helpers.fake.name()
        new_user_data = {
            'email': new_email,
            'password': new_password,
            'name': new_name
        }
        response = requests.patch(src.urls.UPDATE_USER_DATA_URL, data=new_user_data)
        
        assert response.status_code == 401
        assert src.data.USER_DATA_NOT_UPDATED_DUE_LOGIN_MESSAGE in response.text
        
    @allure.title('Проверка изменения почты авторизованного пользователя на уже привязанную почту')
    def test_update_user_email_with_existing_email_user_email_not_changed(self, get_user_token):
        token = get_user_token
        user_data = src.api_requests.create_user_and_collect_user_data()
        user_email = user_data['email']
        new_user_data = {
            'email': user_email
        }
        response = requests.patch(src.urls.UPDATE_USER_DATA_URL, headers={"Authorization": f'{token}'}, data=new_user_data)
        
        assert response.status_code == 403
        assert src.data.USER_DATA_NOT_UPDATED_DUE_EMAIL_MESSAGE in response.text