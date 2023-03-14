from datetime import datetime

from requests import get, post

print(get('http://127.0.0.1:5000/api/jobs').json())

print(get('http://127.0.0.1:5000/api/jobs/1').json())
print(get('http://127.0.0.1:5000/api/jobs/123').json())
print(get('http://127.0.0.1:5000/api/jobs/stroke').json())

# правильный
job = {
    'team_leader_id': 2,
    'job': 'New job 2',
    'work_size': 45,
    'collaborators': '5, 6',
    'is_finished': False
}
print(post('http://127.0.0.1:5000/api/jobs', json=job).json())

# пустой запрос
print(post('http://127.0.0.1:5000/api/jobs', json={}).json())

# id уже существует
job = {
    'id': 2,
    'team_leader_id': 2,
    'job': 'New job 2',
    'work_size': 45,
    'collaborators': '5, 6',
    'is_finished': False
}
print(post('http://127.0.0.1:5000/api/jobs', json=job).json())

# нехватает данных
job = {
    'id': 2,
    'team_leader_id': 2,
}
print(post('http://127.0.0.1:5000/api/jobs', json=job).json())
