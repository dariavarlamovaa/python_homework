import requests
import socket
import threading

api_key = '2613bebc4b7afe87664e9807fbf89c37'
baseURL = 'https://api.openweathermap.org/data/2.5/'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 4321

server_socket.bind((host, port))
print(f'Сервер запущен по адресу {host}, порту {port}')

server_socket.listen(5)

welcome_message = 'Добро пожаловать! Вы подключены к серверу о погоде.\n' \
                  'Введите сообщение в виде - Город, Страна: '


def handle_client(client_socket, client_address):
    print(f'Подключился клиент: {client_address}')
    client_socket.send(welcome_message.encode())

    while True:
        client_message = client_socket.recv(4096).decode()

        if not client_message:
            print('Клиент отключился: ', client_address)
            break

        def weather(q: str = 'Petrozavodsk, RU', appid: str = api_key,
                    units: str = 'metric'):
            response = requests.get(baseURL + 'forecast', params={'q': q, 'appid': appid, 'units': units}).json()
            answer = ''
            if response['cod'] == '200':
                for i in range(7):
                    day = response['list'][i]
                    avg_temperature = round((day['main']['temp_min'] + day['main']['temp_max']) / 2)
                    description = day['weather'][0]['description']
                    speed = day['wind']['speed']
                    humidity = day['main']['humidity']
                    date = day['dt_txt']
                    answer += f'Date: {date}\n' \
                              f'Weather: {description.capitalize()}\n' \
                              f'Average temperature: {avg_temperature}°C\n' \
                              f'Speed of wind: {speed} m/s\n' \
                              f'Humidity: {humidity} %\n' \
                              f'==========================================\n'
                client_socket.send(answer.encode())
            else:
                answer = 'Город не найден. Попробуйте еще раз.'
                client_socket.send(answer.encode())

        weather(client_message.strip())
    client_socket.close()


while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
