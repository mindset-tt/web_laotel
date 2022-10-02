from auth.auth import AuthHandler
from starlette.responses import JSONResponse
from fastapi import Depends
from config.config_db import app, cursor, auth_handler, conp
from model.model import post_department, Department_delete, put_department

@app.get('/myproject1/department', tags=['ພະແນກ'])
async def department(public_id=Depends(auth_handler.auth_wrapper)):
    try:
        cursor.execute("SELECT dep_ID, dep_name, DATE_FORMAT(dep_create_date, '%Y-%m-%d') as dep_create_date FROM department")
        depRows = cursor.fetchall()
        return JSONResponse(status_code=200, content={"department": depRows})

    except Exception as e:
        return print(e)

@app.post('/myproject1/department', tags=['ພະແນກ'])
async def create_department(info: post_department,public_id=Depends(auth_handler.auth_wrapper)):
    try:
        sql = "SELECT dep_name FROM department WHERE dep_name = %s"
        sql_where = (info.dep_name)
        cursor.execute(sql, sql_where)
        if row := cursor.fetchone():
            return JSONResponse(
                status_code=405,
                content={"message": 'ມີຂໍ້ມູນແລ້ວ'}
            )
        sql = "INSERT INTO department(dep_name) VALUES(%s)"
        sql_where = (info.dep_name)
        cursor.execute(sql, sql_where)
        conp.commit()
        return JSONResponse(
            status_code=201,
            content={"message": 'ເພີ່ມຂໍ້ມູນສຳເລັດ', 'status':'ok'}
        )
    except Exception as e:
        return print(e)

@app.put('/myproject1/department', tags=['ພະແນກ'])
async def update_department(info: put_department,public_id=Depends(auth_handler.auth_wrapper)):
    try:
        sql = "UPDATE department SET dep_name = %s WHERE dep_ID = %s"
        sql_where = (info.dep_name, info.dep_ID)
        cursor.execute(sql, sql_where)
        conp.commit()
        return JSONResponse(
            status_code=201,
            content={"message": 'ອັດເດດຂໍ້ມູນສຳເລັດ', 'status':'ok'}
        )
    except Exception as e:
        return print(e)

@app.delete('/myproject1/department', tags=['ພະແນກ'])
async def delete_department(info: Department_delete,public_id=Depends(auth_handler.auth_wrapper)):
    try:
        sql = "DELETE FROM department WHERE dep_name =%s"
        sql_where = (info.dep_name)
        cursor.execute(sql, sql_where)
        conp.commit()
        return JSONResponse(
            status_code=201,
            content={"message": 'ລົບຂໍ້ມູນສຳເລັດ', 'status':'ok'}
        )
    except Exception as e:
        return JSONResponse(
            status_code=403,
            content={"message": 'ຂໍ້ມູນມີການໃຊ້ງານບໍ່ສາມາດລົບໄດ້'}
        )

def department_name(data):
    cursor.execute('SELECT dep_ID FROM department WHERE dep_name = %s', (data, ))
    dep = cursor.fetchone()
    return dep['dep_ID']