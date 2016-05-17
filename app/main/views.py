from . import main
from .forms import PolicyForm, UserForm
from .core import Policy
from flask import render_template, redirect, session, url_for


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/policy', methods=['GET', 'POST'])
def policy():
    form = PolicyForm()
    form.location_id.choices = [('a', '1')]  # !!!!!!!!!!!
    form.event_type.choices = [('a', 'Enter'), ('b', 'Leave')]
    # form.group_id.choices = [(g.id, g.name) for g in Group.query.order_by('name')]

    if form.validate_on_submit():
        # create an object of Policy
        return redirect(url_for('.policy'))
    return render_template('policy.html', form=form)


@main.route('/user', methods=['GET','POST'])
def user():
    form = UserForm()
    if form.validate_on_submit():
        return redirect(url_for('.user'))
    return render_template('user.html', form=form)


@main.route('/notification')
def notification():
    return render_template('notification.html')