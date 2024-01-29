# from auth.auth import AuthHandler
# from starlette.responses import JSONResponse
# from fastapi import Depends
# from config.config_db import app, cursor, auth_handler, conp
# from model.model import Post_user, Put_user, Update_position, User_delete, change_password, change_password_while_login
# from werkzeug.security import generate_password_hash, check_password_hash
# import uuid

# @app.get('/myproject1/user', tags=['ຜູ້ໃຊ້'])
# async def view_user(public_id=Depends(auth_handler.auth_wrapper)):
#     try:
#         # cursor.execute("SELECT session_ID, session_name, DATE_FORMAT(session_create_date, '%Y-%m-%d') FROM session")
#         cursor.execute("SELECT d1.username, d2.emp_name, d1.password, d3.pos_name \
#             FROM useraccount as d1 inner join employee as d2 on (d1.username=d2.emp_ID) \
#                 inner join position as d3 on (d2.pos_ID=d3.pos_ID) WHERE d2.status = 2")
#         user = cursor.fetchall()
#         return JSONResponse(status_code=200, content={"user": user})
#     except Exception as e:
#         return print(e)

# @app.post('/myproject1/user', tags=['ຜູ້ໃຊ້'])
# async def create_user(info: Post_user,public_id=Depends(auth_handler.auth_wrapper)):
#     try:
#         passhash = generate_password_hash(info.password)
#         sql = "SELECT username FROM useraccount WHERE username = %s"
#         sql_where = (info.username)
#         cursor.execute(sql, sql_where)
#         if row := cursor.fetchone():
#             return JSONResponse(
#                 status_code=405,
#                 content={"message": 'ມີຜູ້ໃຊ້ນີ້ແລ້ວ'}
#             )
#         public_id = (uuid.uuid4())
#         sql = "INSERT INTO useraccount (username, password, public_id) VALUES (%s, %s, %s)"
#         sql_where = (info.username, passhash, public_id)
#         cursor.execute(sql, sql_where)
#         conp.commit()
#         return JSONResponse(
#             status_code=201,
#             content={"message": 'ເພີ່ມຂໍ້ມູນສຳເລັດ', 'status':'ok'}
#         )
#     except Exception as e:
#         return print(e)

# @app.put('/myproject1/user', tags=['ຜູ້ໃຊ້'])
# async def update_user(info: Put_user,public_id=Depends(auth_handler.auth_wrapper)):
#     try:
#         passhash = generate_password_hash(info.username)
#         sql = "UPDATE useraccount SET password = %s WHERE username = %s"
#         sql_where = (passhash, info.username)
#         cursor.execute(sql, sql_where)
#         conp.commit()
#         return JSONResponse(
#             status_code=201,
#             content={"message": 'ອັດເດດຂໍ້ມູນສຳເລັດ', 'status':'ok'}
#         )
#     except Exception as e:
#         return print(e)

# @app.delete('/myproject1/user', tags=['ຜູ້ໃຊ້'])
# async def delete_user(info: User_delete,public_id=Depends(auth_handler.auth_wrapper)):
#     try:
#         sql = "DELETE FROM useraccount WHERE username =%s"
#         sql_where = (info.username)
#         cursor.execute(sql, sql_where)
#         conp.commit()
#         return JSONResponse(
#             status_code=201,
#             content={"message": 'ລົບຂໍ້ມູນສຳເລັດ', 'status':'ok'}
#         )
#     except Exception as e:
#         return JSONResponse(
#             status_code=403,
#             content={"message": 'ຂໍ້ມູນມີການໃຊ້ງານບໍ່ສາມາດລົບໄດ້'}
#         )

# @app.post('/myproject1/change_password', tags=['ຜູ້ໃຊ້'])
# async def Change_password(info: change_password,public_id=Depends(auth_handler.auth_wrapper)):
#     try:
#         passhash = generate_password_hash(info.new_password)
#         sql = "Select password from useraccount WHERE username = %s"
#         sql_where = (passhash, info.username)
#         cursor.execute(sql, sql_where)
#         if row := cursor.fetchone():
#             password = row['password']
#             if check_password_hash(password, info.old_password) == True:
#                 sql = "UPDATE useraccount SET password = %s WHERE username = %s"
#                 sql_where = (passhash, info.username)
#                 cursor.execute(sql, sql_where)
#                 conp.commit()
#                 return JSONResponse(
#                     status_code=201,
#                     content={"message": 'ອັບເດດລະຫັດຜ່ານສຳເລັດ', 'status':'ok'}
#                 )
#             else:
#                 return JSONResponse(
#                     status_code=403,
#                     content={"message": 'ລະຫັດຜ່ານເກົ່າບໍ່ຖືກຕ້ອງ'}
#                 )
#         else:
#             return JSONResponse(
#                 status_code=403,
#                 content={"message": 'ບໍ່ພົບຜູ້ໃຊ້ນີ້'}
#             )
#     except Exception as e:
#         return print(e)

# @app.post('/myproject1/change_password_while_login', tags=['ຜູ້ໃຊ້'])
# async def Change_password_while_login(info: change_password_while_login,public_id=Depends(auth_handler.auth_wrapper)):
#     try:
#         passhash = generate_password_hash(info.new_password)
#         sql = "Select password from useraccount WHERE username = %s"
#         sql_where = (info.username)
#         cursor.execute(sql, sql_where)
#         if row := cursor.fetchone():
#             password = row['password']
#             if check_password_hash(password, info.frist_password) == True:
#                 sql = "UPDATE useraccount SET password = %s WHERE username = %s"
#                 sql_where = (passhash, info.username)
#                 cursor.execute(sql, sql_where)
#                 conp.commit()
#                 return JSONResponse(
#                     status_code=201,
#                     content={"message": 'ອັບເດດລະຫັດຜ່ານສຳເລັດ', 'status':'ok'}
#                 )
#     except Exception as e:
#         return print(e)