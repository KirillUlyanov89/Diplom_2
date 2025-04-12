import allure
import requests
import src.data
import src.urls

class TestCreateOrder:
    
    @allure.title('Проверка создания заказа с авторизацией')
    def test_create_order_with_auth_and_ingredients_order_created(self, get_user_token):
        token = get_user_token
        burger_ingredients = [src.data.CRATER_BUN_ID, src.data.CHEESE_MAIN_ID, src.data.FILLET_MAIN_ID, src.data.SPICY_SAUCE_ID]
        burger = {
            'ingredients': burger_ingredients
        }
        response = requests.post(src.urls.CREATE_ORDER_URL, headers={"Authorization": f'{token}'}, data=burger)
        
        assert response.status_code == 200
        assert src.data.ORDER_CREATED_MESSAGE in response.text
        
    @allure.title('Проверка создания заказа без авторизации')
    def test_create_order_without_auth_and_with_ingredients_order_created(self):
        burger_ingredients = [src.data.CRATER_BUN_ID, src.data.CHEESE_MAIN_ID, src.data.FILLET_MAIN_ID, src.data.SPICY_SAUCE_ID]
        burger = {
            'ingredients': burger_ingredients
        }
        response = requests.post(src.urls.CREATE_ORDER_URL, data=burger)
        
        assert response.status_code == 200
        assert src.data.ORDER_CREATED_MESSAGE in response.text
        
    @allure.title('Проверка создания заказа без ингридиентов')
    def test_create_order_without_ingredients_order_not_created(self):
        burger_ingredients = []
        burger = {
            'ingredients': burger_ingredients
        }
        response = requests.post(src.urls.CREATE_ORDER_URL, data=burger)
        
        assert response.status_code == 400
        assert src.data.ORDER_CREATE_WITHOUT_INGREDIENTS_MESSAGE in response.text
        
    @allure.title('Проверка создания заказа с неверным ID ингридиентов')
    def test_create_order_with_invalid_ingredients_leads_to_server_error(self):
        burger_ingredients = ['invalid_ingredient_id']
        burger = {
            'ingredients': burger_ingredients
        }
        response = requests.post(src.urls.CREATE_ORDER_URL, data=burger)
        
        assert response.status_code == 500
        assert src.data.ORDER_CREATE_WITH_INCORRECT_INGREDIENTS_MESSAGE in response.text