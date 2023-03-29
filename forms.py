from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[
        InputRequired(message='Pet name cannot be blank.')])
    species = SelectField("Pet Species", choices=[
        ('Cat', 'Cat'), ('Dog', 'Dog'), ('Rabbit', 'Rabbit'), ('Deer', 'Deer')])
    photo_url = StringField("Pet Image", validators=[Optional(), URL() ])
    age = FloatField("Pet Age", validators=[
        Optional(), NumberRange(min=0, max=30, message="Pet age may range between 0 and 30 years")])
    notes = StringField("Pet Notes")
    available = SelectField("Available for Adoption?", validators=[Optional()], choices=[('', 'No'), (True, 'Yes')], 
                            coerce=bool)