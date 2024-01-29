from logging import root
from sshtunnel import SSHTunnelForwarder
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pymysql import cursors, connect
from fastapi import Depends, FastAPI, Request
# from auth.auth import AuthHandler
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, FileResponse
import os
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
tunnel = SSHTunnelForwarder(('10.233.121.1', 22), ssh_password="root",
                            ssh_username="root", remote_bind_address=("127.0.0.1", 3306))
tunnel.start()
conp = connect(host='127.0.0.1', user="root", passwd="RL@2024",
               database="mydb", port=tunnel.local_bind_port)


engine = create_engine(
    f"mysql://root:123456Aa!@127.0.0.1:{tunnel.local_bind_port}/pos")


SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

cursor = conp.cursor(cursors.DictCursor)

SECRET_KEY = "cairocoders-ednalan"

# auth_handler = AuthHandler()

app = FastAPI(openapi_url="/myproject1/openapi.json", docs_url="/myproject1/docs", redoc_url="/myproject1/redoc", title="KobkoiApi", description="Just only want money", version="1.0.0")

origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get('/', response_class=RedirectResponse, include_in_schema=False)
# async def docs():
#     return RedirectResponse(url='/docs')


@app.get('/myproject1/display/{filename}', tags=['ຮູບພະນັກງານ'])
async def display(filename: str):
    file_path = os.path.join(f"/home/took/myproject/config/static/uploads/{filename}")
    if (filename.endswith('.png')):
        return FileResponse(file_path, media_type="image/png", filename=filename)
    elif (filename.endswith('.jpg')) or (filename.endswith('.jpeg')):
        return FileResponse(file_path, media_type="image/jpeg", filename=filename)
    elif filename.endswith('.webp'):
        return FileResponse(file_path, media_type="image/webp", filename=filename)
    else:
        return {"message": "ບໍ່ພົບຮູບພະນັກງານ"}


@app.get('/static/uploads/{filename}', tags=['ຮູບພະນັກງານ'])
async def display(filename: str):
    file_path = os.path.join(f"/home/took/myproject/config/static/uploads/uploads/{filename}")
    if (filename.endswith('.png')):
        return FileResponse(file_path, media_type="image/png", filename=filename)
    elif (filename.endswith('.jpg')) or (filename.endswith('.jpeg')):
        return FileResponse(file_path, media_type="image/jpeg", filename=filename)
    elif filename.endswith('.webp'):
        return FileResponse(file_path, media_type="image/webp", filename=filename)
    else:
        return {"message": "ບໍ່ພົບຮູບພະນັກງານ"}

