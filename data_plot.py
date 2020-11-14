import requests
# requests.get('http://127.0.0.1:8000/app/create_db_data')
print(requests.get('http://10.178.229.1:8000/app/get_base_file_data/').content)