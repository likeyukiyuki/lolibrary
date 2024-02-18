import sqlite3
from fastapi.middleware.cors import CORSMiddleware
from pyparsing import Optional
import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI, File, Form,  UploadFile
from io import BytesIO
import cv2
import base64
from typing import Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)



# conn = sqlite3.connect('test.db')
# print ("数据库打开成功")
# c = conn.cursor()
# c.execute('''CREATE TABLE images
#         (
#         id text(50) PRIMARY KEY,
#         dress_id text(50) not null,
#         images BLOB not null
#         );''')
# print ("数据表创建成功")
# conn.commit()
# conn.close()

    
import uuid




@app.post("/insert")

async def insert(fileslist:list[UploadFile]=File(None),name:str=Form(), 
                category:str=Form(),brand:str=Form(),colorway:str=Form(),
                features:Optional[str]=Form(None),tags:Optional[str]=Form(None),
                images:UploadFile=File(),years:str=Form(),
                product:Optional[str]=Form(None),price:Optional[str]=Form(None),
                bust:Optional[str]=Form(None),waist:Optional[str]=Form(None),
                length:Optional[str]=Form(None),note:Optional[str]=Form(None)):
    print(tags)
    id=uuid.uuid1()
    id=str(id)
    data=images.file.read()
    with sqlite3.connect('test.db') as conn:
        c=conn.cursor()
        print ("数据库打开成功")

        c.execute(
            "insert into dress(id,name,category,brand,colorway,features,tags,images,years,product,price,bust,waist,length,note) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (id,name,category,brand,colorway,features,tags,data,years,product,price,bust,waist,length,note)
        )
        if fileslist!=None:
             for files in fileslist:
                print(files)
                files=files.file.read()
                c.execute(
                    "insert into images(id,images) values(?,?)",(id,files)
                )
       

        conn.commit()
        print("插入成功")
        return "添加成功~"
    
class detail_searchInfo(BaseModel):
    id:str

class name_searchInfo(BaseModel):
    onlyname:str

class searchInfo(BaseModel):
      scategory:str|None=Form()
      sbrand:str|None=Form()
      sfeatures:str|None=Form()
      scolorway:str|None=Form()
      stags:str|None=Form()
      syears:str|None=Form()

class loginInfo(BaseModel):
    user:str
    password:str

class user_loginInfo(BaseModel):
    user:str
    password:str

@app.post("/name_search")
async def name_search(info:name_searchInfo): 
    conn = sqlite3.connect('test.db')
    c=conn.cursor()
    print ("数据库打开成功")

    data= c.execute(
        "select * from dress where name like ? ",('%'+info.onlyname+'%',)
    ).fetchall()
    conn.commit()
    rtdata=[]
    
    for row in data:
        img=row[7]
        strimg=base64.b64encode(img).decode('utf-8')
        strimg='data:image/png;base64,'+strimg
        
        rowdata=row[0:7]+(strimg,)+row[8:15]
        rtdata.append(rowdata)
    conn.close()
    
    return rtdata
    

@app.post("/detail_search")
async def detail_search(info:detail_searchInfo): 
    print(info.id)
    conn = sqlite3.connect('test.db')
    c=conn.cursor()
    print ("数据库打开成功")

    data=c.execute(
        "select * from dress where id=?",(info.id,),
        
    ).fetchall()
    images=c.execute(
        "select images from images where id=?",(info.id,)
    ).fetchall()

    conn.commit()
    rtdata=[]
    data=data[0]
    img=data[7]
    strimg=base64.b64encode(img).decode('utf-8')
    strimg='data:image/png;base64,'+strimg
    rtdata=data[0:7]+(strimg,)+data[8:15]
    print(len(data))
    print(len(images))
    for irow in images:
      
        img1=irow[0]
        img1=base64.b64encode(img1).decode('utf-8')
        img1='data:image/png;base64,'+img1
        rtdata=rtdata+(img1,)

    
    print(len(rtdata))
    return rtdata

# sbrand:str|None=Form(),scategory:str|None=Form(),sfeatures:str|None=Form(),
#                  scolorway:str|None=Form(),stags:str|None=Form(),syears:str|None=Form()

@app.post("/search")
async def search(info:searchInfo):
    slist=[("brand",info.sbrand),("category",info.scategory),("features",info.sfeatures),
           ("colorway",info.scolorway),("tags",info.stags),("years",info.syears)]
    conn = sqlite3.connect('test.db')
    c=conn.cursor()
    print ("数据库打开成功")
    sql="select * from dress where 1"
    for (i,j) in slist:
        if j != "":
            sql += f" and {i} = '{j}' "
    print(sql)
    data=c.execute(sql).fetchall()
    rtdata=[]
        
    for row in data:
            img=row[7]
            strimg=base64.b64encode(img).decode('utf-8')
            strimg='data:image/png;base64,'+strimg
            
            rowdata=row[0:7]+(strimg,)+row[8:15]
            rtdata.append(rowdata)
    conn.close()
        
    return rtdata

@app.post("/login")
async def login(info:loginInfo): 
    conn = sqlite3.connect('test.db')
    c=conn.cursor()
    print ("数据库打开成功")
    c.execute(
        "select count(*) from adminstrator where user=?",(info.user,)
    )
    user=c.fetchone()
    c.execute(
        "select count(*) from adminstrator where password=?",(info.password,)
    )
    password=c.fetchone()
    
    if user[0] > 0 and password[0] > 0:
        return ("登录成功")
    elif user[0] > 0 and password[0] == 0:
        print("cw")
        return ("密码错误")
    elif user[0] == 0:
        print("bcz")
        return ("账号不存在")
    conn.commit()
    
class removeInfo(BaseModel):
    name:str

@app.post("/remove")
async def remove(info:removeInfo): 
    print(info.name)
    conn = sqlite3.connect('test.db')
    c=conn.cursor()
    print ("数据库打开成功")
    c.execute(
        "DELETE from dress where name=?",(info.name,)
    )
    print("删除成功")
    conn.commit()
    return ("删除成功")


@app.post("/user_login")
async def user_login(info:user_loginInfo): 
    conn = sqlite3.connect('test.db')
    c=conn.cursor()
    print ("数据库打开成功")
    c.execute(
        "select count(*) from user where user=?",(info.user,)
    )
    user=c.fetchone()
    c.execute(
        "select count(*) from user where password=?",(info.password,)
    )
    password=c.fetchone()
    
    if user[0] > 0 and password[0] > 0:
        return ("登录成功")
    elif user[0] > 0 and password[0] == 0:
        print("cw")
        return ("密码错误")
    elif user[0] == 0:
        print("bcz")
        return ("账号不存在")
    conn.commit()

class registerInfo(BaseModel):
    user:str
    password:str

@app.post("/register")
async def register(info:registerInfo): 
    id=uuid.uuid1()
    id=str(id)
    adminstration=0
    conn = sqlite3.connect('test.db')
    c=conn.cursor()
    print ("数据库打开成功")
    x: tuple[int] = c.execute(
        "select count(*) from user where id=?", (info.user,)).fetchone()
    print(x)
    # 注册
    n = x[0]
    if n > 0:
        print("已有账号")
        return "已有账号，请登录哦"
    else:
        c.execute("INSERT INTO USER (id,user,password,adminstration) VALUES (?,?,?,?)",
                  (id,info.user,info.password,adminstration))
        conn.commit()
        print("数据插入成功")
        conn.close()
        return "注册成功~"

if __name__ == '__main__':
    uvicorn.run(app="main:app", host="127.0.0.1", port=8888, reload=True)
