from auth.auth import AuthHandler
from starlette.responses import JSONResponse
from fastapi import Depends, Form
from config.config_db import app, cursor, auth_handler, conp
from typing import List
from model.model import Assessment, Assessment_update, Delete_header_form, Assessment_record


@app.get('/myproject1/header_form', tags=['ແບບຟອມ'])
async def view_form(public_id=Depends(auth_handler.auth_wrapper)):
    cursor.execute(
        "SELECT head_ID, head_name, emp_ID, DATE_FORMAT(date_create, '%Y-%m-%d') as create_date FROM header_form")
    header = cursor.fetchall()
    return JSONResponse(status_code=200, content={"form": header})


@app.get('/myproject1/header_form_detail', tags=['ແບບຟອມ'])
async def detail_form(header_name: str, public_id=Depends(auth_handler.auth_wrapper)):
    cursor.execute(
        "SELECT head_ID, head_name, DATE_FORMAT(date_create,'%%Y-%%m-%%d') as create_date FROM pos.header_form where head_name = %s", header_name)
    header = cursor.fetchone()
    head_ID = header['head_ID']
    cursor.execute(
        "SELECT title1_ID, title1_name FROM header_title1 where head_ID = %s", head_ID)
    title1 = cursor.fetchall()
    title_1 = []
    tit1 = {}
    tit2 = {}
    title_2 = []
    for i in range(len(title1)):
        title1_ID = title1[i]['title1_ID']
        title_1.append(title1_ID)
        cursor.execute("SELECT d3.title2_ID, d3.title2_name, d2.title1_ID \
                        FROM header_title1 as d2 \
                            inner join header_title2 as d3 on (d2.title1_ID = d3.title1_ID) where d2.title1_ID = %s", title1_ID)
        title2 = cursor.fetchall()
        for j in range(len(title2)):
            title2_ID = title2[j]['title2_name']
            title_2.append(title2_ID)
        tit1 = title1
        tit2 = title2
        header['title'] = tit1
        header['title'][i]['title2'] = tit2
    return JSONResponse(status_code=200, content={"form": header})


@app.post('/myproject1/header_form' , tags=['ແບບຟອມ'])
async def create_form(info: Assessment, public_id=Depends(auth_handler.auth_wrapper)):
    # sourcery skip: avoid-builtin-shadow, hoist-statement-from-loop
    sql = "INSERT INTO header_form (head_name, emp_ID) VALUES (%s, %s)"
    sql_where = (info.head_name, info.emp_ID)
    cursor.execute(sql, sql_where)
    conp.commit()
    sql = "SELECT head_ID FROM header_form WHERE head_name = %s"
    sql_where = (info.head_name)
    cursor.execute(sql, sql_where)
    id = cursor.fetchone()
    id = id['head_ID']
    for i in range(len(info.title1)):
        title1 = info.title1[i].title1_name
        sql = "INSERT INTO header_title1 (title1_name, head_ID) VALUES (%s, %s)"
        sql_where = (title1, id)
        cursor.execute(sql, sql_where)
        conp.commit()
        sql = "SELECT title1_ID FROM header_title1 WHERE title1_name = %s"
        sql_where = (info.title1[i].title1_name)
        cursor.execute(sql, sql_where)
        ida = cursor.fetchone()
        idsa = ida['title1_ID']
        for j in range(len(info.title1[i].title2)):
            sql = "INSERT INTO header_title2 (title2_name, title1_ID) VALUES (%s, %s)"
            sql_where = [(info.title1[i].title2[j].title2_name, idsa)]
            cursor.executemany(sql, sql_where)
            conp.commit()
    return JSONResponse(
        status_code=201,
        content={"message": 'ສາ້ງແບບຟອມສຳເລັດ', 'status': 'ok'}
    )


@app.put('/myproject1/header_form', tags=['ແບບຟອມ'])
async def update_form(info: Assessment_update, public_id=Depends(auth_handler.auth_wrapper)):
    # sourcery skip: avoid-builtin-shadow, hoist-statement-from-loop
    sql = "UPDATE header_form SET head_name = %s, emp_ID = %s WHERE (head_ID = %s)"
    sql_where = (info.head_name, info.emp_ID, info.head_ID)
    cursor.execute(sql, sql_where)
    conp.commit()
    sql = "SELECT head_ID FROM header_form WHERE head_name = %s"
    sql_where = (info.head_name)
    cursor.execute(sql, sql_where)
    id = cursor.fetchone()
    id = id['head_ID']
    for i in range(len(info.title1)):
        title1 = info.title1[i].title1_name
        sql = "UPDATE header_title1 SET title1_name = %s, head_ID = %s WHERE (title1_ID = %s)"
        sql_where = (title1, id, info.title1[i].title1_ID)
        cursor.execute(sql, sql_where)
        conp.commit()
        sql = "SELECT title1_ID FROM header_title1 WHERE title1_name = %s"
        sql_where = (info.title1[i].title1_name)
        cursor.execute(sql, sql_where)
        ida = cursor.fetchone()
        idsa = ida['title1_ID']
        for j in range(len(info.title1[i].title2)):
            sql = "UPDATE header_title2 SET title2_name = %s, title1_ID = %s WHERE (title2_ID = %s)"
            sql_where = [(info.title1[i].title2[j].title2_name,
                          idsa, info.title1[i].title2[j].title2_ID)]
            cursor.executemany(sql, sql_where)
            conp.commit()
    return JSONResponse(
        status_code=201,
        content={"message": 'ອັບເດດແບບຟອມສຳເລັດ', 'status': 'ok'}
    )


@app.delete('/myproject1/header_form', tags=['ແບບຟອມ'])
async def delete_form(info: Delete_header_form, public_id=Depends(auth_handler.auth_wrapper)):
    cursor.execute(
        "DELETE FROM header_form WHERE (head_ID = %s)", info.head_ID)
    conp.commit()
    return JSONResponse(
        status_code=201,
        content={"message": 'ລົບຂໍ້ມູນສຳເລັດ', 'status': 'ok'}
    )

@app.post('/myproject1/assessment_form_record', tags=['ການຕອບແບບຟອມ'])
async def create_form_record(info: Assessment_record, public_id=Depends(auth_handler.auth_wrapper)):
    for i in range(len(info.title2)):
        sql = "INSERT INTO assessment_record (title2_ID, emp_ID, answer_score) VALUES (%s, %s, %s)"
        sql_where = [(info.title2[i].title2_id, info.emp_ID, info.title2[i].score)]
        cursor.executemany(sql, sql_where)
        conp.commit()
    return JSONResponse(
        status_code=201,
        content={"message": 'ສຳເລັດ', 'status': 'ok'}
    )