from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable=False)
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.id}: {self.date_creation}"


@app.route("/", methods=["POST","GET"])
def index():
    if request.method == 'POST':
        new_creation = request.form['content']
        task = Todo(content=new_creation)
        try:
            db.session.add(task)
            db.session.commit()
            return redirect("/")
        except:
            return "There was an issure regarding adding a task"
    else:
        tasks = Todo.query.order_by(Todo.date_creation).all()
        return render_template('index.html', entries=tasks)

@app.route("/delete/<int:id>")
def delete(id):
    content_del = Todo.query.get_or_404(id)
    try:
        db.session.delete(content_del)
        db.session.commit()
        return redirect("/")
    except:
        return "There was an error, cannot delete the element"

@app.route("/update/<int:id>", methods=["POST","GET"])
def update(id):
    content_update = Todo.query.get_or_404(id)
    if request.method == "POST":
        content_update.content = request.form["content"]

        try:
            db.session.commit()
            return redirect("/")

        except:
            return "There was an error, cannot update the element"
    else:
        return render_template("update.html", entries=content_update)
    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    print("Database path:", app.config["SQLALCHEMY_DATABASE_URI"])
    app.run(debug=True)
    

