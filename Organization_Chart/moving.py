# from auth.auth import AuthHandler
# from starlette.responses import JSONResponse
# from fastapi import Depends
# from config.config_db import app, cursor, auth_handler, conp
# from typing import List
# from model.model import Post_moving
# from CRUD.department import department_name
# from CRUD.position import position_name
# from CRUD.session import session_name

# @app.get('/myproject1/moving', tags=['ອົງກອນ'])
# async def view_moving(public_id=Depends(auth_handler.auth_wrapper)):
#     try:
#         cursor.execute("SELECT  d1.emp_ID, d2.emp_name, d2.emp_surname, d3.dep_name,\
#              d4.session_name, d5.pos_name, d1.description, DATE_FORMAT(d1.moving_date, '%Y-%m-%d') as moving_date, d6.dep_name, d7.session_name, d8.pos_name \
#             FROM moving as d1 inner join employee as d2 on (d1.emp_ID = d2.emp_ID) \
#                 inner join department as d3 on (d1.dep_ID = d3.dep_ID) \
#                     inner join session as d4 on (d1.session_ID = d4.session_ID) \
#                         inner join position as d5 on (d1.pos_ID = d5.pos_ID) \
#                             inner join department as d6 on (d2.dep_ID = d6.dep_ID) \
#                                 inner join session as d7 on (d2.session_ID = d7.session_ID) \
#                                     inner join position as d8 on (d2.pos_ID = d8.pos_ID) WHERE d2.status = 2")
#         sql_where = cursor.fetchall()
#         return JSONResponse(status_code=200, content={"moving": sql_where})

#     except Exception as e:
#         return print(e)

# @app.post('/myproject1/moving', tags=['ອົງກອນ'])
# async def create_moving(info: Post_moving, public_id=Depends(auth_handler.auth_wrapper)):
#     try:
#         _dep = department_name(info.dep_name)
#         print(type(_dep))
#         _pos = position_name(info.pos_name)
#         print(_pos)
#         _ses = session_name(info.session_name)
#         print(type(_ses))
#         sql = "SELECT emp_ID, pos_ID, dep_ID, session_ID FROM employee WHERE emp_ID = %s"
#         sql_where = (info.emp_ID)
#         print(type(sql_where))
#         cursor.execute(sql, sql_where)
#         row = cursor.fetchone()
#         depid = row['dep_ID']
#         print(depid)
#         sessionid = row['session_ID']
#         print(sessionid)
#         posid = row['pos_ID']
#         print(posid)
#         sql = "INSERT INTO moving (dep_ID, session_ID, pos_ID, emp_ID) \
#             VALUES (%s, %s, %s, %s)"
#         sql_where = (depid, sessionid, posid, info.emp_ID)
#         print(sql_where)
#         cursor.execute(sql, sql_where)
#         sql = "UPDATE employee  SET pos_ID = %s, session_ID = %s, dep_ID = %s, \
#                         status = 2 WHERE (emp_ID = %s)"
#         sql_where = (_pos, _ses, _dep, info.emp_ID)
#         print(sql_where)
#         cursor.execute(sql, sql_where)
#         conp.commit()
#         return JSONResponse(
#             status_code=201,
#             content={"message": 'ຍ້າຍຂໍ້ມູນສຳເລັດ', 'status': 'ok'}
#         )
#     except Exception as e:
#         return print(e)