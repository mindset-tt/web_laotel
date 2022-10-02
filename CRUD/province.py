from config.config_db import app, cursor, auth_handler
from starlette.responses import JSONResponse
from fastapi import Depends


@app.get('/myproject1/provinces', tags=['ແຂວງ'])
async def province():
    cursor.execute("SELECT prov_ID, province FROM province")
    provRows = cursor.fetchall()
    return JSONResponse(status_code=200, content={"province": provRows})

def province_name(data):
    cursor.execute('SELECT prov_ID FROM province WHERE province = %s', (data, ))
    prov = cursor.fetchone()
    return prov['prov_ID']