import configuration
import requests
import data

# Создаётся новый заказ
def post_new_order(order_body):

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,  # подставялем полный url
                         json=order_body)  # тут тело в data.py

order_response = post_new_order(data.order_body) # переменная ответа

# Проверяем заказ по номеру заказа в ответе
def get_order_info(track):

    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + str(track))
    # В запрос ставим номер из созданного заказа, преобразуя в строку
track_number = order_response.json()['track']  # присваивается переменной полученное значение track

# тест: информация о заказе по номеру заказа
def test_order_info_by_order_number_get_success_response():

    order_info_response = get_order_info(track_number) # запускаем функцию с новой переменной

    assert order_info_response.status_code == 200 # сравниваем статус кода на выходе

