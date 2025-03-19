from typing import Optional, List
from fastapi import APIRouter

from .database import QueryHandler as db
from .models import StudentModel

routes = APIRouter(prefix="/student")

@routes.get("/")
async def get_students(limit:Optional[int]=10, offset:Optional[int]=0):
    return await db.get_all_students(limit, offset)

@routes.get("/{roll_no}")
async def get_one_student(roll_no:str):
    test =  await db.get_student_by_roll(roll_no)
    print(test)
    return test

@routes.post("/insert")
async def insert_student_data(student:StudentModel):
    return await db.insert_student(student)

@routes.post("/insert/bulk")
async def bulk_insert_students_data(students:List[StudentModel]):
    return await db.bulk_insert_students(students)