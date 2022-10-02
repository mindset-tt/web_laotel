from CRUD import department, employee, login, session, user, position, province
from asessment_form import assesment_form
from model import model
from Organization_Chart import moving
from config.config_db import app, cursor, auth_handler
from auth.auth import AuthHandler
import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host='0.0.0.0',
        port=3000,
        reload=True,
        debug=True,
    )
