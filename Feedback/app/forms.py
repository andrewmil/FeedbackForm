from flask_wtf import Form
from wtforms import RadioField, TextField

class Feedback(Form):
    satisfaction = RadioField('satisfaction', choices = [('very dissatisfied','very dissatisfied'),('dissatisfied','dissatisfied'),('neither','neither'), ('satisfied', 'satisfied'), ('very satisfied', 'very satisfied')])
    feedback = TextField('feedback')
