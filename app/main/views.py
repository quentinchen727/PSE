from . import main
from .forms import PolicyForm
from flask import render_template, redirect, session, url_for


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/policy', methods=['GET','POST'])
def policy():
    form = PolicyForm()
    form.location_id.choices = [('a','1')]  # !!!!!!!!!!!
    form.event_type.choices = [('a', 'Enter'), ('b', 'Leave')]
    # form.group_id.choices = [(g.id, g.name) for g in Group.query.order_by('name')]

    return render_template('policy.html', form=form)


@main.route('/user', methods=['GET','POST'])
def user():
    return render_template('user.html')


@main.route('/notification')
def notification():
    return render_template('notification.html')