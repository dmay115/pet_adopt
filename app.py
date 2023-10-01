from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "shhhh"

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

connect_db(app)


def create_tables():
    with app.app_context():
        db.create_all()


create_tables()


@app.route("/")
def homepage():
    """Shows List of All Pets"""
    pets = Pet.query.all()
    return render_template("pet_list.html", pets=pets)


@app.route("/pet/add", methods=["GET", "POST"])
def add_pet():
    """Renders pet form for (GET) or handles pet form submission (POST)"""
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        pet = Pet(
            name=name,
            species=species,
            photo_url=photo_url,
            age=age,
            notes=notes,
            available=available,
        )
        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add.html", form=form)

@app.route('/pet/<int:id>/edit', methods=["GET", "POST"])
def edit_pet(id):
    """Renders pet edit form for (GET) or handles pet edit form for (POST)"""
    pet = Pet.query.get_or_404(id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template("edit_pet.html", form=form)