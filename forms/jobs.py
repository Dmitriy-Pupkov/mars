from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField, EmailField, SelectField, StringField, IntegerField, \
    DateField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    team_leader = SelectField('Ответственный', validators=[DataRequired])
    job = StringField('Описание работы')
    work_size = IntegerField('Объём работы, ч')
    collaborators = StringField('Соучастники')
    start_date = DateField('Начало работы')
    end_date = DateField('Конец работы')
    is_finished = BooleanField('Завершение')
    submit = SubmitField('Войти')
