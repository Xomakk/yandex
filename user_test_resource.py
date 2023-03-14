import requests

print(requests.get('http://127.0.0.1:5000/api/v2/users/2').json())
print(requests.get('http://127.0.0.1:5000/api/v2/users/123').json())

print(requests.get('http://127.0.0.1:5000/api/v2/users').json())


# user = {
#     'name': 'Maksim',
#     'about': 'Крутой рудокоп',
#     'email': 'maksimka007@mail.ru'
# }
# print(requests.post('http://127.0.0.1:5000/api/v2/users',
#                     json=user).json())

user = {
    'about': 'Крутой рудокоп',
    'email': 'maksimka007@mail.ru'
}
print(requests.post('http://127.0.0.1:5000/api/v2/users',
                    json=user).json())
print(requests.post('http://127.0.0.1:5000/api/v2/users').json())


print(requests.delete('http://127.0.0.1:5000/api/v2/users/3').json())
print(requests.delete('http://127.0.0.1:5000/api/v2/users/123').json())

