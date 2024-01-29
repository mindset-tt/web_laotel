# from pickle import TRUE
# from warnings import catch_warnings
# from config.config_db import app, cursor, SECRET_KEY, conp, auth_handler
# from re import match
# from model.model import forgot_password, login
# from starlette.responses import JSONResponse
# from werkzeug.security import check_password_hash
# from jose import jwt
# from datetime import datetime, timezone, timedelta
# from werkzeug.security import generate_password_hash
# from fastapi import Depends
# @app.post('/myproject1/login', tags=['ເຂົ້າສູ່ລະບົບ'])
# async def Login(info: login):
#     try:
#         sql = "SELECT d1.username, d1.password, d1.public_id, d2.status FROM useraccount as d1\
#                     inner join employee as d2 on (d1.username=d2.emp_ID) WHERE d1.username=%s and d2.status = 2"
#         sql_where = (info.username)
#         cursor.execute(sql, sql_where)
#         if row := cursor.fetchone():
#             public_id = row['public_id']
#             password = row['password']
#             if not match(r'[A-Z0-9]+', info.username):
#                 return JSONResponse(
#                     status_code=401,
#                     content={'message': 'username ບໍ່ຖືກຕ້ອງ'}
#                 )
#             if check_password_hash(password, info.password) == True:
#                 token = jwt.encode({'public_id': public_id, 'exp': datetime.now(timezone.utc) + timedelta(days=0, hours=12), 'iat': datetime.now(timezone.utc)}, SECRET_KEY, algorithm='HS256')
#                 cursor.execute("SELECT d1.emp_ID, d5.password, d1.gender, d1.emp_name, d1.emp_surname,\
#                                 d1.emp_tel, d1.village, d1.district, d1.profilepic, d4.province, d3.dep_name, d2.pos_name\
#                                 from employee as d1 inner join position as d2 on (d1.pos_ID=d2.pos_ID)\
#                                 inner join department as d3 on(d1.dep_ID=d3.dep_ID) \
#                                 inner join province as d4 on(d1.prov_ID=d4.prov_ID)\
#                                 inner join useraccount as d5 on(d1.emp_ID=d5.username) WHERE d1.emp_ID = %s and d1.status = 2", info.username)
#                 userRows = cursor.fetchone()
#                 return JSONResponse(
#                     status_code=200,
#                     content={
#                         "status": "ok",
#                         "message": 'ເຂົ້າສູ່ລະບົບສຳເລັດ',
#                         'token': token,
#                         'user': userRows}
#                 )
#             else:
#                 respone = JSONResponse(
#                     status_code=401,
#                     content={'message': 'password ບໍ່ຖືກຕ້ອງ'}
#                 )
#                 return respone
#         else:
#             respone = JSONResponse(
#                 status_code=401,
#                 content={'message': 'ບໍ່ມີຜູ້ໃຊ້ນີ້'}
#             )
#             return respone
#     except Exception as e:
#         return e



# @app.post('/myproject1/forgotpassword', tags=['ລືມລະຫັດຜ່ານ'])
# async def ForgotPassword(info: forgot_password):
#     try:
#         sql = "SELECT d1.username, d2.status, d2.emp_tel FROM useraccount as d1\
#                     inner join employee as d2 on (d1.username=d2.emp_ID) WHERE d1.username=%s and d2.status = 2 and d2.emp_tel = %s"
#         sql_where = (info.username, info.tel)
#         cursor.execute(sql, sql_where)
#         if not (row := cursor.fetchone()):
#             return JSONResponse(
#                 status_code=401,
#                 content={'message': 'ບໍ່ມີຜູ້ໃຊ້ນີ້'}
#             )
#         tel = row['emp_tel']
#         if not match(r'[A-Z0-9]+', info.username):
#             return JSONResponse(
#                 status_code=401,
#                 content={'message': 'username ຫຼື password ບໍ່ຖືກຕ້ອງ'}
#             )
#         if not match(r'[0-9]+', info.tel):
#             return JSONResponse(
#                 status_code=401,
#                 content={'message': 'ເບີໂທບໍ່ຖືກຕ້ອງ'}
#             )
#         if info.tel == tel:
#             passhash = generate_password_hash(info.new_password)
#             cursor.execute(
#                 "UPDATE useraccount SET password = %s WHERE username = %s", (passhash, info.username))
#             conp.commit()
#             return JSONResponse(
#                 status_code=200,
#                 content={
#                     "status": "ok",
#                     "message": 'ປ່ຽນລະຫັດຜ່ານສຳເລັດ'}
#             )
#     except Exception as e:
#         return e
