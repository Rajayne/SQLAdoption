from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[
        InputRequired(message='Pet name cannot be blank.')])
    species = StringField("Pet Species", validators=[
        InputRequired(message='Pet species cannot be blank.')])
    photo_url = StringField("Pet Image")
    age = FloatField("Pet Age", validators=[Optional()])
    notes = StringField("Pet Notes")