import imp
from urllib import response
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.api.common import constant
import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1',
aws_access_key_id=constant.ACCESS_KEY,
aws_secret_access_key=constant.SECRET_KEY)

table = dynamodb.Table(constant.DYNAMO_DB_TABLENAME)

router= APIRouter()
class Employee(BaseModel):
    emp_id: str
    department: str
    emp_name: str
    designation: str
    emp_email: str
    emp_contact: str
    
       
def get_employee_by_id(emp_id: str):
    try:
        response = table.get_item(
        Key={
        'emp_id': emp_id
    })
        item = response['Item']
        return item
    except Exception as e:
        raise HTTPException(
            status_code=constant.STATUS_CODE_NOT_FOUND, detail=str(e)
        )

    
@router.get("/")
async def get_employee(emp_id: str):
    response=get_employee_by_id(emp_id)
    return response
    
    


@router.post("")
async def add_employee(req_body: Employee):
    req_body_dict= req_body.dict()
    table.put_item(
    Item={
        'emp_id': req_body_dict['emp_id'],
        'department': req_body_dict['department'],
        'emp_name': req_body_dict['emp_name'],
        'designation': req_body_dict['designation'],
        'emp_email': req_body_dict['emp_email'],
        'emp_contact': req_body_dict['emp_contact'],
    }
)
    response= get_employee_by_id(req_body_dict['emp_id'])
    return response

@router.delete("")
async def delete_employee(emp_id: str):
    try:
        table.delete_item(
        Key={
        'emp_id': emp_id
    })
        
        return {"message":"Item deleted"}
    except Exception as e:
        raise HTTPException(
            status_code=constant.STATUS_CODE_NOT_FOUND, detail=str(e)
        )



@router.put("")
async def update_employee(emp_id, department, emp_name, emp_email, emp_contact):
    table.update_item(
    Key={
        'emp_id': emp_id
    },
    UpdateExpression='set department=:val1, emp_name=:val2, emp_email=:val3, emp_contact=:val4',
    ExpressionAttributeValues={
        ':val1': department,
        ':val2': emp_name,
        ':val3': emp_email,
        ':val4' : emp_contact
    }
    )
    response= get_employee_by_id(emp_id)
    return response



