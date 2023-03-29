from flask import Flask, request, render_template,  redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm
from models import db, connect_db, Pet

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.app_context().push()

app.config["SECRET_KEY"] = "key"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def show_home():
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet_form():
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template("add_form.html", form=form)
    
@app.route("/<int:id>", methods=["GET", "POST"])
def show_pet_details(id):
    pet = Pet.query.get_or_404(id)
    form = AddPetForm()
    return render_template('/details.html', pet=pet, visibility="hidden", form=form)

@app.route("/<int:id>/edit", methods=["GET", "POST"])
def edit_pet_details(id):
    pet = Pet.query.get_or_404(id)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data

        db.session.commit()
        return redirect(f'/{pet.id}')
    else:
        return render_template('/details.html', pet=pet, visibility="visible", form=form)