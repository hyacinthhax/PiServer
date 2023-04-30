from flask import render_template, url_for, flash, redirect, Blueprint
from forms import RegistrationForm, LoginForm
from views import views_blueprint


auth_blueprint = Blueprint('auth', __name__)

# Register User Page
@auth_blueprint.route("/reguse", methods=["GET", "POST"])
def registerUser():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('views.home'))
    return render_template('register.html', title='Register', form=form)

# Login Page
@auth_blueprint.route("/login", methods=["GET", "POST"])
def loginUser():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
