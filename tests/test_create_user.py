import allure
import requests
import pytest
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

    @pytest.mark.parametrize("missing_field, expected_status, expected_message", [
        ('name', 403, src.data.MISSING_FIELDS_IN_USER_FORM_MESSAGE),
        ('email', 403, src.data.MISSING_FIELDS_IN_USER_FORM_MESSAGE),
        ('password', 403, src.data.MISSING_FIELDS_IN_USER_FORM_MESSAGE),
    ])
    @allure.title('Проверка создания пользователя без заполненного поля {missing_field}')
    def test_create_user_with_missing_fields(self, missing_field, expected_status, expected_message):
        user_data = src.helpers.generate_user_data()

        # Удаляем поле из данных пользователя в зависимости от параметра
        if missing_field == 'name':
            del user_data['name']
        elif missing_field == 'email':
            del user_data['email']
        elif missing_field == 'password':
            del user_data['password']

        response = requests.post(src.urls.CREATE_USER_URL, data=user_data)

        assert response.status_code == expected_status
        assert expected_message in response.text