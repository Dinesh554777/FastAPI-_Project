from fastapi import FastAPI
from fastapi import Path

app = FastAPI()
students={
    1:{"name":"John",
       "age":17,
       "class":"year 12"
       }
}
@app.get("/")
def index():
    return {"name": "first Data"}

@app.get("/get-students/{student_id}")
def get_students(student_id: int= Path(description="The ID of the student you want to view", gt=0
                )
    ):
    return students[student_id]