from fastapi import HTTPException
from typing import List, Optional

from .postgres import database
from .models import StudentModel as Student

    # name:str
    # roll_no:str
    # standard:int
    # sex:SexEnum

class QueryHandler:
    async def get_student_by_roll(roll_no:str)->Student:
        query = """SELECT name,roll_No,standard,sex from students WHERE Roll_No=$1;"""
        try:
            async with database.pool.acquire() as conn:
                record = await conn.fetchrow(query, roll_no)
                return dict(record)
                # data = Student(name=record["name"], roll_no=record["roll_No"], standard=record["standard"], sex=record["sex"])
                # #print(record)
                # if record is not None:
                #     data = Student(name=record["name"], roll_no=record["roll_No"], standard=record["standard"], sex=record["sex"])
                #     print(data)
                #     return data
                # return None
        except Exception as e:
            print(f"Didnt got all record for: {roll_no}")
            raise HTTPException(status_code=404, detail=str(e))
        

    async def get_all_students(limit:int, offset:int):
        query = """SELECT name,roll_No,standard,sex from students LIMIT $1 OFFSET $2"""
        try:
            async with database.pool.acquire() as conn:
                records = await conn.fetch(query, limit, offset)
                # data = [Student(name=records["Name"], roll_no=records["Roll_No"], standard=records["Standard"], sex=records["Sex"])]
                # return data
                data = (dict(record) for record in records)
                print(data)
                return data
        except Exception as e:
            print("Didnt got all record")
            raise HTTPException(status_code=404, detail=str(e))
        

    async def insert_student(student:Student):
        query = """INSERT INTO students(name,roll_No,standard,sex) VALUES ($1, $2, $3, $4)"""
        try:
            async with database.pool.acquire() as conn:
                await conn.execute(query, student.name, student.roll_no, student.standard, student.sex)
        except:
            print("Unable to enter data")


    async def bulk_insert_students(students:List[Student]):
        query = """INSERT INTO students(name,roll_No,standard,sex) VALUES ($1, $2, $3, $4)"""
        students_tuple = [(student.name, student.roll_no, student.standard, student.sex) for student in students]
        try:
            async with database.pool.acquire() as conn:
                await conn.executemany(query, students_tuple)
        except:
            print("Unable to enter data")