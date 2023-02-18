from data import db_session
from data.users import User
from data.jobs import Jobs
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET KEY'] = 'yandexlyceum_secret_key'


@app.route('/works_log')
def works_log():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return render_template('index.html', jobs=jobs)


def main():
    db_session.global_init("db/blogs.db")
    app.run()


if __name__ == '__main__':
    main()
