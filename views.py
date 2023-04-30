from flask import render_template, url_for, Blueprint


views_blueprint = Blueprint('views', __name__)

# Home is supposed to return after login
@views_blueprint.route("/")
def home():
    return render_template('home.html')

# Contact Page
@views_blueprint.route("/contact")
def contactPage():
    return render_template('contact.html')

# About Page
@views_blueprint.route("/about")
def aboutPage():
    return render_template('about.html')

# Donation Page
@views_blueprint.route("/donate")
def donatePage():
    return render_template('donate.html')