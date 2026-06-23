from fastapi import FastAPI
from fastapi import Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
students={
    1:{"name":"John",
       "age":17,
       "year":"year 12"
       }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

@app.get("/")
def index():
    return {"name": "first Data"}

@app.get("/get-students/{student_id}") #path parameter
def get_students(student_id: int= Path(description="The ID of the student you want to view", gt=0
                )
    ):
    return students[student_id]

@app.get("/get-by-name/{student_id}") #path and query parameter
def get_student(*, student_id : int,    # keyword-only arguments start here
                name : Optional[str] = None, # keyword-only arguments start here
                test : int):  # required integer parameter
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}  

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Data": "Student already exists"}
    students[student_id] = student
    return students[student_id]