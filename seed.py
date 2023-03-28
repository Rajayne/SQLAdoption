from models import Pet, db
from app import app

# Create tables
db.drop_all()
db.create_all()

# Make a bunch of departments
pet1 = Pet(name="Vader", 
           species="Dog",
           photo_url="https://images.fineartamerica.com/images/artworkimages/mediumlarge/1/black-german-shepherd-dog-ii-sandy-keeton.jpg",
           age=7,
           notes="German Shepherd Wolfhound Mix")
pet2 = Pet(name="Midna", 
           species="Cat",
           photo_url="https://www.pumpkin.care/wp-content/uploads/2021/05/Nebelung-Cat-Hero.jpg",
           age="",
           notes="Nebelung Breed")

db.session.add_all([pet1, pet2])
db.session.commit()