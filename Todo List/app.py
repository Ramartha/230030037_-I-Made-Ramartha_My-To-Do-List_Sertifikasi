from flask import Flask, render_template, request, redirect
from database import db
from models.task import Task

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


# READ
@app.route("/")
def index():
    tasks = Task.query.all()   # array/list data
    return render_template("index.html", tasks=tasks)


# CREATE
@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]

        new_task = Task(title)
        db.session.add(new_task)
        db.session.commit()

        return redirect("/")

    return render_template("add.html")


# UPDATE
@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id):
    task = Task.query.get(id)

    if request.method == "POST":
        task.title = request.form["title"]
        task.status = request.form["status"]

        db.session.commit()
        return redirect("/")

    return render_template("edit.html", task=task)


# DELETE
@app.route("/delete/<int:id>")
def delete(id):
    task = Task.query.get(id)

    db.session.delete(task)
    db.session.commit()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)


@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id):
    task = Task.query.get(id)

    if request.method == "POST":
        task.title = request.form["title"]
        task.status = request.form["status"]

        db.session.commit()

        return redirect("/")

    return render_template("edit.html", task=task)