from database import db

class Note(db.model):
    id = db.Column("id", db.Integer, primary_key = True)
    title = db.Column("titile", db.string(200))
    text = db.Column("text", db.string(100))
    date = db.Column("date", db.string(50))

    def __init__(self, title, text, date):
        self.title = title
        self.text = text
        self.date = date

class User(db.model):
    id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email 