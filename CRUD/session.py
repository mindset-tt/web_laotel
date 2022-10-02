from auth.auth import AuthHandler
from starlette.responses import JSONResponse
from fastapi import Depends
from model.model import Delete_session, Update_session, Create_session
from config.config_db import app, cursor, auth_handler, conp
import os

@app.get('/myproject1/session', tags=['ພາກສ່ວນ'])
async def get_session(public_id=Depends(auth_handler.auth_wrapper)):
    try:
        cursor.execute("SELECT session_ID, session_name,\
            DATE_FORMAT(session_create_date, '%Y-%m-%d') \
                as session_create_date FROM session")
        userRows = cursor.fetchall()
        return JSONResponse(status_code=200, content={"session": userRows})
    except Exception as e:
        return print(e)

@app.post('/myproject1/session', tags=['ພາກສ່ວນ'])
async def post_session(info: Create_session,public_id=Depends(auth_handler.auth_wrapper)):
    try:
        sql = "SELECT session_name FROM session WHERE session_name = %s"
        sql_where = (info.session_name)
        cursor.execute(sql, sql_where)
        if row := cursor.fetchone():
            return JSONResponse(
                status_code=405,
                content={"message": 'ມີຂໍ້ມູນແລ້ວ'}
            )
        sql = "INSERT INTO session (session_name) VALUES(%s)"
        sql_where = (info.session_name)
        cursor.execute(sql, sql_where)
        conp.commit()
        return JSONResponse(
            status_code=201,
            content={"message": 'ເພີ່ມຂໍ້ມູນສຳເລັດ', 'status':'ok'}
        )
    except Exception as e:
        return print(e)

@app.put('/myproject1/session', tags=['ພາກສ່ວນ'])
async def put_session(info: Update_session,public_id=Depends(auth_handler.auth_wrapper)):
    try:
        sql = "UPDATE session SET session_name = %s WHERE session_ID = %s"
        sql_where = (info.session_name, info.session_ID)
        cursor.execute(sql, sql_where)
        conp.commit()
        return JSONResponse(
            status_code=201,
            content={"message": 'ອັດເດດຂໍ້ມູນສຳເລັດ', 'status':'ok'}
        )
    except Exception as e:
        return print(e)

@app.delete('/myproject1/session', tags=['ພາກສ່ວນ'])
async def delete_session(info: Delete_session,public_id=Depends(auth_handler.auth_wrapper)):
    try:
        sql = "DELETE FROM session WHERE session_name =%s"
        sql_where = (info.session_name)
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

def session_name(data):
    cursor.execute('SELECT session_ID FROM session \
        WHERE session_name = %s', (data, ))
    ses = cursor.fetchone()
    return ses['session_ID']