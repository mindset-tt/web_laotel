from dataclasses import dataclass
from typing import Any, Dict, List
from pydantic import BaseModel


class login(BaseModel):
    username: str
    password: str


class Post_user(login):
    pass


class Put_user(login):
    pass


class User_delete(BaseModel):
    username: str


class department(BaseModel):
    dep_ID: str
    dep_name: str


class post_department(BaseModel):
    dep_name: str


class put_department(department):
    pass


class Department_delete(post_department):
    pass


class position(BaseModel):
    pos_ID: str
    pos_name: str


class Update_position(position):
    pass


class Create_position(BaseModel):
    pos_name: str


class Delete_position(Create_position):
    pass


class Update_session(BaseModel):
    session_ID: str
    session_name: str


class Create_session(BaseModel):
    session_name: str


class Delete_session(Create_session):
    pass


class Post_moving(BaseModel):
    emp_ID: str
    dep_name: str
    pos_name: str
    session_name: str


@dataclass
class Title2:
    title2_name: str

    @staticmethod
    def from_dict(obj: Any) -> 'Title2':
        _title2_name = str(obj.get("title2_name"))
        return Title2(_title2_name)


@dataclass
class Title1:
    title1_name: str
    title2: List[Title2]

    @staticmethod
    def from_dict(obj: Any) -> 'Title1':
        _title1_name = str(obj.get("title1_name"))
        _title2 = [Title2.from_dict(y) for y in obj.get("title2")]
        return Title1(_title1_name, _title2)


@dataclass
class Assessment:
    head_name: str
    emp_ID: str
    title1: List[Title1]

    @staticmethod
    def from_dict(obj: Any) -> 'Assessment':
        _head_name = str(obj.get("head_name"))
        _emp_ID = str(obj.get("emp_ID"))
        _title1 = [Title1.from_dict(y) for y in obj.get("title1")]
        return Assessment(_head_name, _emp_ID, _title1)


@dataclass
class Title2_update:
    title2_ID: str
    title2_name: str

    @staticmethod
    def from_dict(obj: Any) -> 'Title2_update':
        _title2_ID = str(obj.get("title2_ID"))
        _title2_name = str(obj.get("title2_name"))
        return Title2_update(_title2_ID, _title2_name)


@dataclass
class Title1_update:
    title1_ID: str
    title1_name: str
    title2: List[Title2_update]

    @staticmethod
    def from_dict(obj: Any) -> 'Title1_update':
        _title1_ID = str(obj.get("title1_ID"))
        _title1_name = str(obj.get("title1_name"))
        _title2 = [Title2_update.from_dict(y) for y in obj.get("title2")]
        return Title1_update(_title1_ID, _title1_name, _title2)


@dataclass
class Assessment_update:
    head_ID: str
    head_name: str
    emp_ID: str
    title1: List[Title1_update]

    @staticmethod
    def from_dict(obj: Any) -> 'Assessment_update':
        _head_ID = str(obj.get("head_ID"))
        _head_name = str(obj.get("head_name"))
        _emp_ID = str(obj.get("emp_ID"))
        _title1 = [Title1.from_dict(y) for y in obj.get("title1")]
        return Assessment_update(_head_ID, _head_name, _emp_ID, _title1)


class Delete_header_form(BaseModel):
    head_ID: str

class Assessment_record(BaseModel):
    emp_ID: str
    title2_ID: str
    score: str


@dataclass
class Title2record:
    title2_id: str
    score: int


@dataclass
class Assessment_record:
    title2: List[Title2record]


class user(BaseModel):
    username: str
    password: str
    public_id: str

class forgot_password(BaseModel):
    username: str
    tel: str
    new_password: str

class change_password(BaseModel):
    username: str
    old_password: str
    new_password: str

class change_password_while_login(BaseModel):
    username: str
    frist_password: str
    new_password: str

@dataclass
class Title2record:
    title2_id: str
    score: int


@dataclass
class Assessment_record:
    emp_ID: str
    title2: List[Title2record]