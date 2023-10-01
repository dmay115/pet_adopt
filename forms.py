from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField
from wtforms.validators import InputRequired, Optional, Email, NumberRange, URL


class PetForm(FlaskForm):
    """Form for adding or editing pet"""

    name = StringField("Pet's Name", validators=[InputRequired()])
    species = RadioField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("frog", "Frog"), ("other", "Other")], validators=[InputRequired()]
    )
    photo_url = StringField("Photo URL of pet", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[NumberRange(min=None, max=100)])
    notes = StringField("Notes about the pet", validators=[Optional()])
    available = BooleanField("Available?")

