from importlib.metadata import requires
from auth.auth import AuthHandler
from starlette.responses import JSONResponse
from typing import List, Any
from fastapi import Depends, Form, File, UploadFile
from config.config_db import app, cursor, auth_handler, conp
from re import match
from .department import department_name
import uuid
from werkzeug.security import generate_password_hash
from .position import position_name
from .session import session_name
from .province import province_name
import os
from werkzeug.utils import secure_filename
from pydantic import BaseModel
from typing import Optional
import aiofiles
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.get('/myproject1/employee', tags=['ພະນັກງານ'])
async def employee(public_id=Depends(auth_handler.auth_wrapper)):
    try:
        cursor.execute("SELECT d1.emp_ID, d1.gender, d1.emp_name, d1.emp_surname,\
             d1.emp_tel, d1.village, d1.district, d1.profilepic, d4.province, d3.dep_name, d2.pos_name\
              from employee as d1 inner join position as d2 on (d1.pos_ID=d2.pos_ID)\
                inner join department as d3 on(d1.dep_ID=d3.dep_ID) \
                inner join province as d4 on(d1.prov_ID=d4.prov_ID) WHERE d1.status = 2")
        empRows = cursor.fetchall()
        return JSONResponse(status_code=200, content={"employee": empRows})

    except Exception as e:
        return print(e)


@app.post('/myproject1/employee', tags=['ພະນັກງານ'])
async def create_employee(emp_ID: str = Form(...),
                          emp_name: str = Form(...),
                          emp_surname: str = Form(...),
                          gender: str = Form(...),
                          emp_tel: str = Form(...),
                          village: str = Form(...),
                          district: str = Form(...),
                          prov_name: str = Form(...),
                          dep_name: str = Form(...),
                          pos_name: str = Form(...),
                          sessions_name: str = Form(...),
                          files: UploadFile = File(...),
                          public_id=Depends(auth_handler.auth_wrapper)

):
    # try:
    cursor.execute(
        'SELECT emp_ID FROM employee WHERE emp_ID = %s', (emp_ID))
    if empid := cursor.fetchone():
        respone = JSONResponse(status_code=405, content={
                               'message': 'ມີລະຫັດນີ້ແລ້ວ'})
    elif not match(r'[A-Z]+[0-9]+', emp_ID):
        respone = JSONResponse(status_code=403, content={
                               'message': 'ຮູບແບບລະຫັດບໍ່ຖືກຕ້ອງ'})
    elif files and (not allowed_file(files.filename)):
        respone = JSONResponse(status_code=403, content={
                               'message': 'ຮູບບໍ່ຖືກຕ້ອງ'})
    else:
        _dep = department_name(dep_name)
        _pos = position_name(pos_name)
        _ses = session_name(sessions_name)
        _prov = province_name(prov_name)
        filename = files.filename
        secure_filename = str(uuid.uuid1())
        filesave = os.path.join("/app/config/static/uploads", str(f"{secure_filename}_{filename}"))
        print(filesave)
        async with aiofiles.open(filesave, 'wb') as fh:
            while True:
                chunk = await files.read(2048)
                if not chunk:
                    break
                await fh.write(chunk)
        print(_dep)
        sqlQuery = "INSERT INTO employee(emp_ID, emp_name, emp_surname, \
                gender, emp_tel, village, district, pos_ID, dep_ID, prov_ID, session_ID, status, profilepic) \
                    VALUES(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        bindData = emp_ID, emp_name, emp_surname, gender, emp_tel, village, district, _pos, _dep, _prov, _ses, "ຍັງບໍ່ອອກ", f"http://47.250.49.41/display/{secure_filename}_{filename}"
        cursor.execute(sqlQuery, bindData)
        conp.commit()
        password = 'password'
        username = emp_ID
        passhash = generate_password_hash(password)
        public_id = (uuid.uuid4())
        sql = "INSERT INTO useraccount (username, password, public_id) VALUES (%s, %s, %s)"
        sql_where = (username, passhash, public_id)
        cursor.execute(sql, sql_where)
        conp.commit()
        respone = JSONResponse(
            status_code=201,
            content={
                'message': 'ເພີ່ມຂໍ້ມູນສຳເລັດ', 'status': 'ok'}
        )
        return respone
    # except Exception as e:
    #     return e


@app.put('/myproject1/employee', tags=['ພະນັກງານ'])
async def update_employee(emp_ID: str = Form(...),
                          emp_name: str = Form(...),
                          emp_surname: str = Form(...),
                          gender: str = Form(...),
                          emp_tel: str = Form(...),
                          village: str = Form(...),
                          district: str = Form(...),
                          prov_name: str = Form(...),
                          dep_name: str = Form(...),
                          pos_name: str = Form(...),
                          sessions_name: str = Form(...),
                          files: UploadFile = File(None),
                          public_id=Depends(auth_handler.auth_wrapper)
):
    try:
        cursor.execute(
            'SELECT emp_ID FROM employee WHERE emp_ID = %s', (emp_ID))
        if empid := cursor.fetchone():
            if not files:
                _dep = department_name(dep_name)
                _pos = position_name(pos_name)
                _ses = session_name(sessions_name)
                _prov = province_name(prov_name)
                sqlQuery = "UPDATE employee  SET emp_name = %s, emp_surname = %s, gender = %s, \
                    emp_tel = %s, village = %s, district = %s, pos_ID = %s, session_ID = %s, dep_ID = %s, \
                            prov_ID = %s, status = 2  WHERE (emp_ID = %s)"
                bindData = (emp_name, emp_surname, gender, emp_tel, village,
                            district, _pos, _ses, _dep, _prov, emp_ID)
            else:
                _dep = department_name(dep_name)
                _pos = position_name(pos_name)
                _ses = session_name(sessions_name)
                _prov = province_name(prov_name)
                print(files.filename)
                filename = files.filename
                secure_filename = str(uuid.uuid1())
                filesave = os.path.join(
                    "/app/config/static/uploads", str(filename))
                print(filesave)
                async with aiofiles.open(filesave, 'wb') as fh:
                    while True:
                        chunk = await files.read(2048)
                        if not chunk:
                            break
                        await fh.write(chunk)
                print(_dep)
                sqlQuery = "UPDATE employee SET emp_name = %s, emp_surname = %s, gender = %s, \
                    emp_tel = %s, village = %s, district = %s, pos_ID = %s, session_ID = %s, dep_ID = %s, \
                            prov_ID = %s, status = 2, profilepic = %s  WHERE (emp_ID = %s)"
                bindData = emp_name, emp_surname, gender, emp_tel, village, district, _pos, _ses, _dep, _prov, f"http://47.250.49.41/display/{secure_filename}_{filename}", emp_ID
            cursor.execute(sqlQuery, bindData)
            conp.commit()
            respone = JSONResponse(
                status_code=201,
                content={
                    'message': 'ແກ້ໄຂຂໍ້ມູນສຳເລັດ', 'status': 'ok'}
            )
        return respone
    except Exception as e:
        return e

@app.delete('/myproject1/employee', tags=['ພະນັກງານ'])
async def delete_employee(emp_ID: str, public_id=Depends(
    auth_handler.auth_wrapper
)
):
    try:
        cursor.execute(
            'SELECT emp_ID FROM employee WHERE emp_ID = %s', (emp_ID))
        if not (empid := cursor.fetchone()):
            return JSONResponse(status_code=405, content={'message': 'ບໍ່ມີລະຫັດນີ້ແລ້ວ'})

        cursor.execute("UPDATE employee SET status = 1 WHERE (emp_ID = %s)", emp_ID)
        conp.commit()
        return JSONResponse(status_code=201, content={'message': 'ລົບຂໍ້ມູນສຳເລັດ', 'status': 'ok'})

    except Exception as e:
        return e


@app.get('/myproject1/employees', tags=['ພະນັກງານ'])
async def employee_only_10(page: int, public_id=Depends(auth_handler.auth_wrapper)):
    try:
        if page == 1:
            d = 0
        else:
            d = 5 * page
            print(d)
        cursor.execute("SELECT d1.emp_ID, d1.gender, d1.emp_name, d1.emp_surname,\
                d1.emp_tel, d1.village, d1.district, d1.profilepic, d4.province, d3.dep_name, d2.pos_name\
                from employee as d1 inner join position as d2 on (d1.pos_ID=d2.pos_ID)\
                inner join department as d3 on(d1.dep_ID=d3.dep_ID) \
                inner join province as d4 on(d1.prov_ID=d4.prov_ID) WHERE d1.status = 2 limit 10 offset %s", d)
        empRows = cursor.fetchall()
        return JSONResponse(status_code=200, content={"employee": empRows})

    except Exception as e:
        return print(e)