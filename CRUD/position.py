# from auth.auth import AuthHandler
# from starlette.responses import JSONResponse
# from fastapi import Depends
# from config.config_db import app, cursor, auth_handler, conp
# from model.model import Create_position, Delete_position, Update_position

# @app.get('/myproject1/position', tags=['ຕຳແໜ່ງ'])
# async def get_position(public_id=Depends(auth_handler.auth_wrapper)):
#     try:
#         cursor.execute("SELECT pos_ID, pos_name FROM position")
#         posRows = cursor.fetchall()
#         return JSONResponse(status_code=200, content={"position": posRows})
#     except Exception as e:
#         return print(e)

# @app.post('/myproject1/position', tags=['ຕຳແໜ່ງ'])
# async def post_position(info: Create_position, public_id=Depends(auth_handler.auth_wrapper)):
#     try:
#         sql = "SELECT pos_name FROM position WHERE pos_name = %s"
#         sql_where = (info.pos_name)
#         cursor.execute(sql, sql_where)
#         if row := cursor.fetchone():
#             return JSONResponse(
#                 status_code=405,
#                 content={"message": 'ມີຂໍ້ມູນແລ້ວ'}
#             )
#         sql = "INSERT INTO position (pos_name) VALUES (%s)"
#         sql_where = (info.pos_name)
#         cursor.execute(sql, sql_where)
#         conp.commit()
#         return JSONResponse(
#             status_code=201,
#             content={"message": 'ເພີ່ມຂໍ້ມູນສຳເລັດ', 'status':'ok'}
#         )
#     except Exception as e:
#         return print(e)

# @app.put('/myproject1/position', tags=['ຕຳແໜ່ງ'])
# async def put_position(info: Update_position, public_id=Depends(auth_handler.auth_wrapper)):
#     try:
#         sql = "UPDATE position SET pos_name = %s WHERE pos_ID = %s"
#         sql_where = (info.pos_name, info.pos_ID)
#         cursor.execute(sql, sql_where)
#         conp.commit()
#         return JSONResponse(
#             status_code=201,
#             content={"message": 'ອັດເດດຂໍ້ມູນສຳເລັດ', 'status':'ok'}
#         )
#     except Exception as e:
#         return print(e)

# @app.delete('/myproject1/position', tags=['ຕຳແໜ່ງ'])
# async def delete_position(info: Delete_position, public_id=Depends(auth_handler.auth_wrapper)):
#     try:
#         sql = "DELETE FROM position WHERE pos_name =%s"
#         sql_where = (info.pos_name)
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

# def position_name(data):
#     cursor.execute('SELECT pos_ID FROM position WHERE pos_name = %s', (data, ))
#     pos = cursor.fetchone()
#     return pos['pos_ID']