import requests
from CompanyApi import CompanyApi

api = CompanyApi("https://x-clients-be.onrender.com")

#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager

# Указываем название и описание компании для добавление в список
name = "Test Company"
descr ="Test Description"

# Поля, необходимые для добавления нового сотрудника
id = 0
first_name = "Ginevra"
last_name = "Weasley"
middle_name = "Molly "
email = "g_weasley@hogwarts.com"
url = "gryffindor.net"
phone = "1234567890"
birthdate = "1981-08-11"
isActive = True

# [GET] /employee
# Проверка получения списка работников компании
def test_get_employee_list():
    # Создаем новую компанию
    new_company = api.post_company(name, descr)
    company_id = new_company["id"]

    # Считаем длину списка работников в новой компании  
    body = api.get_employee(company_id)  
    len_before = len(body)

    # Добавляем работника
    api.add_employee(id, first_name, last_name, middle_name, company_id, email, url, phone, birthdate, isActive)
    
    # Снова считаем длину списка работников в новой компании после добавления работника
    body = api.get_employee(company_id)
    len_after = len(body)

    # Проверяем, что длина списка изменилась
    assert len_after - len_before == 1

# [POST] /employee
# Проверка добавления работника в компанию
def test_add_employee():
    # Создаем новую компанию
    new_company = api.post_company(name, descr)
    company_id = new_company["id"]
    
    # Считаем длину списка работников в новой компании      
    body = api.get_employee(company_id)  
    len_before = len(body)

    # Добавляем работника в новую компанию
    api.add_employee(id, first_name, last_name, middle_name, company_id, email, url, phone, birthdate, isActive)

    # Считаем длину списка работников в новой компании после добавления работника
    body = api.get_employee(company_id)
    len_after = len(body)

    assert len_after - len_before == 1
    assert body[-1]["firstName"] == first_name
    assert body[-1]["lastName"] == last_name
    assert body[-1]["middleName"] == middle_name
    assert body[-1]["email"] == None
    assert body[-1]["avatar_url"] == url
    assert body[-1]["phone"] == phone
    assert body[-1]["birthdate"] == birthdate

# [GET] /employee/{id}
# Проверка получения информации о работнике по его ID
def test_get_employee_by_id():
    # Создаем новую компанию
    new_company = api.post_company(name, descr)
    company_id = new_company["id"]

    # Добавляем работника в новую компанию
    employee = api.add_employee(id, first_name, last_name, middle_name, company_id, email, url, phone, birthdate, isActive)
    employee_id = employee["id"]
    
    # Получаем сведения о работнике, которого добавили шагом ранее
    response = api.get_employee_info(employee_id)

    # Проверяем, что сведения о работнике, которые мы отправляли на сервер, 
    # соответствуют сведениям, что пришли в ответ на запрос данных о работнике по его ID
    assert response["id"] == employee_id
    assert response["firstName"] == first_name
    assert response["lastName"] == last_name
    assert response["middleName"] == middle_name
    assert response["phone"] == phone
    # Сервер не сохраняет email, который ему передается
    # В сваггере и postman происходит аналогичная ситуация
    assert response["email"] == email  
    assert response["birthdate"] == birthdate
    assert response["avatar_url"] == url
    assert response["companyId"] == company_id

# [PATCH] /employee/{id}
# Проверка обновления информации о работнике
def test_patch_employee_info():
    # Создаем новую компанию
    new_company = api.post_company(name, descr)
    company_id = new_company["id"]

    # Добавляем работника в новую компанию
    employee = api.add_employee(id, first_name, last_name, middle_name, company_id, email, url, phone, birthdate, isActive)

    employee_id = employee["id"]

    # Перечень полей и их значения, которые будут изменяться у работника
    updated_last_name = "Potter"
    updated_email = "g_potter@hogwarts.com"
    updated_url = "hogwarts.net"
    updated_phone = "updated phone"
    updated_isActive = False

    # Передаем запрос на изменение сведений о работнике
    api.patch_employee_info(
        employee_id,
        last_name=updated_last_name, 
        email=updated_email, 
        url=updated_url,
        phone=updated_phone, 
        isActive=updated_isActive,
    )

    # Получаем сведения о работнике
    response = api.get_employee_info(employee_id)

    # Проверяем, что нужные сведения изменились
    assert response["lastName"] == updated_last_name
    assert response["email"] == updated_email
    assert response["avatar_url"] == updated_url
    assert response["phone"] == updated_phone
    assert response["isActive"] == updated_isActive

# Проверка обязательности поля 'id' для метода [POST] /employee
def test_add_employee_without_id():
    # Создаем новую компанию
    new_company = api.post_company(name, descr)
    company_id = new_company["id"]

    # Задаем словарь с данными без обязательного поля 
    data = {
            #"id": id,
            "firstName": "Test name",
            "lastName": "Test last name",
            "middleName": "Test middle name",
            "companyId": company_id,
            "email": "test@email.com",
            "url": "test url",
            "phone": "test phone",
            "birthdate": "1981-08-11",
            "isActive": True
        }

    # Добавляем работника в новую компанию через соответствующую функцию
    response = api.add_employee_without_fields(data)

    assert response.status_code == 500

# Проверка обязательности поля 'firstName' для метода [POST] /employee
def test_add_employee_without_firstName():
    # Создаем новую компанию
    new_company = api.post_company(name, descr)
    company_id = new_company["id"]

    # Задаем словарь с данными без обязательного поля 
    data = {
            "id": 0,
            #"firstName": "Test name",
            "lastName": "Test last name",
            "middleName": "Test middle name",
            "companyId": company_id,
            "email": "test@email.com",
            "url": "test url",
            "phone": "test phone",
            "birthdate": "1981-08-11",
            "isActive": True
        }

    # Добавляем работника в новую компанию через соответствующую функцию
    response = api.add_employee_without_fields(data)

    assert response.status_code == 500

# Проверка обязательности поля 'lastName' для метода [POST] /employee
def test_add_employee_without_lastName():
    # Создаем новую компанию
    new_company = api.post_company(name, descr)
    company_id = new_company["id"]

    # Задаем словарь с данными без обязательного поля 
    data = {
            "id": 0,
            "firstName": "Test name",
            #"lastName": "Test last name",
            "middleName": "Test middle name",
            "companyId": company_id,
            "email": "test@email.com",
            "url": "test url",
            "phone": "test phone",
            "birthdate": "1981-08-11",
            "isActive": True
        }

    # Добавляем работника в новую компанию через соответствующую функцию
    response = api.add_employee_without_fields(data)

    assert response.status_code == 500

# Проверка обязательности поля 'companyId' для метода [POST] /employee
def test_add_employee_without_companyId():
    # Создаем новую компанию
    new_company = api.post_company(name, descr)
    company_id = new_company["id"]

    # Задаем словарь с данными без обязательного поля 
    data = {
            "id": 0,
            "firstName": "Test name",
            "lastName": "Test last name",
            "middleName": "Test middle name",
            #"companyId": company_id,
            "email": "test@email.com",
            "url": "test url",
            "phone": "test phone",
            "birthdate": "1981-08-11",
            "isActive": True
        }

    # Добавляем работника в новую компанию через соответствующую функцию
    response = api.add_employee_without_fields(data)

    assert response.status_code == 500

# Проверка обязательности поля 'isActive' для метода [POST] /employee
def test_add_employee_without_isActive():
    # Создаем новую компанию
    new_company = api.post_company(name, descr)
    company_id = new_company["id"]

    # Задаем словарь с данными без обязательного поля 
    data = {
            "id": 0,
            "firstName": "Test name",
            "lastName": "Test last name",
            "middleName": "Test middle name",
            "companyId": company_id,
            "email": "test@email.com",
            "url": "test url",
            "phone": "test phone",
            "birthdate": "1981-08-11",
            #"isActive": True
        }

    # Добавляем работника в новую компанию через соответствующую функцию
    response = api.add_employee_without_fields(data)

    assert response.status_code == 500