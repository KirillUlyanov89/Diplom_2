import allure
import requests
import src.data
import src.urls

class TestGetOrders:
    
    @allure.title('Проверка получения заказов пользователя с авторизацией')
    def test_get_orders_of_user_with_auth_orders_got(self, get_user_token):
        token = get_user_token
        response = requests.get(src.urls.GET_ORDERS_URL, headers={"Authorization": f'{token}'})
        
        assert response.status_code == 200
        assert src.data.ORDER_GET_SUCCEED_MESSAGE in response.text
        
    @allure.title('Проверка получения заказов пользователя без авторизации')
    def test_get_orders_of_user_without_auth_order_not_got(self):
        response = requests.get(src.urls.GET_ORDERS_URL)
        
        assert response.status_code == 401
        assert src.data.ORDER_DONT_GET_DUE_LOGIN_MESSAGE in response.text    