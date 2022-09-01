from flask import Flask, render_template, request, redirect, url_for
from extensions import db
from models.models import Todo

def build_app():
	app = Flask(__name__)
	app.config.from_object('extensions.config.LocalConfig')

	db.app = app
	db.init_app(app)

	return app

app = build_app()


@app.route('/')
def index():
    query_todo = db.session.query(Todo).all()

    return render_template('base.html', query_todo=query_todo)


@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    description = request.form.get('description')

    new_todo = Todo()

    new_todo.title = title
    new_todo.description = description
    new_todo.complete = False

    db.session.add(new_todo)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/update/<int:todo_id>')
def update_todo(todo_id):
    todo = db.session.query(Todo).filter_by(id=todo_id).first()

    todo.complete = not todo.complete

    db.session.commit()

    return redirect(url_for('index'))


@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    todo = db.session.query(Todo).filter_by(id=todo_id).first()

    todo.complete = not todo.complete

    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
