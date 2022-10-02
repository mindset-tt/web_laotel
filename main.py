from CRUD import department, employee, login, session, user, position, province
from asessment_form import assesment_form
from model import model
from Organization_Chart import moving
from config.config_db import app, cursor, auth_handler
from auth.auth import AuthHandler
import uvicorn
from starlette.responses import JSONResponse
from typing import List
from fastapi import Depends
from dataclasses import dataclass
from typing import Any, Dict, List
from pydantic import BaseModel
from werkzeug.utils import secure_filename
from pydantic import BaseModel
from typing import Optional
import aiofiles
from jose import jwt
from sshtunnel import SSHTunnelForwarder
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pymysql import cursors, connect
from fastapi import Depends, FastAPI, Request
from auth.auth import AuthHandler
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, FileResponse
import os
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
import jwt
from datetime import timezone
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host='0.0.0.0',
        port=3000,
        reload=True,
        debug=True,
    )
