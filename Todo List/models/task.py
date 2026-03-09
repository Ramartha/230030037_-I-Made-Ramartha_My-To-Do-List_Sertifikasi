from database import db

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)

class Task(BaseModel):
    title = db.Column(db.String(200))
    status = db.Column(db.String(50))

    def __init__(self, title, status="Belum"):
        self.title = title
        self.status = status

    def selesai(self):
        self.status = "Selesai"