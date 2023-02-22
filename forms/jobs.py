from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, IntegerField, DateField


class JobForm(FlaskForm):
    job = StringField('Описание работы')
    work_size = IntegerField('Объём работы, ч')
    collaborators = StringField('Соучастники')
    start_date = DateField('Начало работы')
    end_date = DateField('Конец работы')
    is_finished = BooleanField('Завершение')
    submit = SubmitField('Применить')
