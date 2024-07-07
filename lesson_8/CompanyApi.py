import requests

class CompanyApi:
    # Инициализация 
    def __init__(self, url) -> None:
        self.url = url
    # Получить список компаний   
    def get_company_list(self, params_to_add=None):
        resp = requests.get(self.url + '/company', params=params_to_add)
        return resp.json()

    # Получить токен авторизации
    def get_token(self, user='raphael', password='cool-but-crude'):
        creds = {
            "username": user,
            "password": password
        } 
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]

    # Создать компанию
    def post_company(self, name, descr):
        data = {
            "name": name,
            "description": descr
        }
        my_headers = {
            "x-client-token": self.get_token()
        }
        response = requests.post(self.url + "/company", json=data, headers=my_headers)
        return response.json()
    

    # Получить список работников в компании
    def get_employee(self, company_id):
        my_params = {
            "company": str(company_id)
        }
        resp = requests.get(self.url + '/employee', params=my_params)
        return resp.json()

    # Добавить работника в компанию    
    def add_employee(self, id, first_name, last_name, middle_name, company_id, email, url, phone, birthdate, isActive):
        new_employee = {
            "id": id,
            "firstName": first_name,
            "lastName": last_name,
            "middleName": middle_name,
            "companyId": company_id,
            "email": email,
            "url": url,
            "phone": phone,
            "birthdate": birthdate,
            "isActive": isActive
        }
        my_headers = {
            "x-client-token": self.get_token()
        }
        resp = requests.post(self.url + '/employee',
                             json=new_employee, headers=my_headers)
        return resp.json()
    
    # Функция, которая испаользуется для тестирования обязательности полей
    # Функция для добавления работника в компанию    
    def add_employee_without_fields(self, data):
        data = {}
        my_headers = {
            "x-client-token": self.get_token()
        }   
        resp = requests.post(self.url + '/employee',
                             json=data, headers=my_headers)
        return resp

    
    # Получить данные работника по его ID
    def get_employee_info(self, employee_id):
        resp = requests.get(self.url + '/employee/' + str(employee_id))
        return resp.json()
    
    # Изменить данные о работнике в компании по его ID   
    def patch_employee_info(self, employee_id, last_name, email, url, phone, isActive):
        new_info = {
            "lastName": last_name,
            "email": email,
            "url": url,
            "phone": phone,
            "isActive": isActive
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(self.url + '/employee/'+ str(employee_id),
            json=new_info, headers=my_headers)
        return resp.json() 