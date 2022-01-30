# FastAPI

## Features:
This project on FAST API contains 4 endpoints to perform CRUD operations on DynamoDB.
__________________________________________
    Name of DynamoDB Table= Employee
    Table consists of following fields:

            emp_id: str
            department: str
            emp_name: str
            designation: str
            emp_email: str
            emp_contact: str
__________________________________________

## Endpoints:
1. GET: /api/v1/employee/{emp_id} [Get Employee]
2. POST: /api/v1/employee/{emp_id} [Add Employee]
3. PUT: /api/v1/employee/{emp_id} [Delete Employee]
4. DELETE: /api/v1/employee/{emp_id} [Update Employee]

## Setup:
1. Clone master branch of the repository.
2. Setup Virtual env in the local. Refer this link:
    -[https://programwithus.com/learn/python/pip-virtualenv-windows]
3. Activate the  Virtualenv.
4. pip install from requirements.txt using command(inside env):
    - pip install -r requirements.txt
5. If requirements.txt is not present, then run the following command:
    - pip install fastapi uvicorn requests boto3 botocore Mangum
6. In order to run the code, execute following command:
    - uvicorn app.main:app --reload