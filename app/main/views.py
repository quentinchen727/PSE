from . import main
from flask import render_template, redirect, session, url_for


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/policy', methods=['GET','POST'])
def policy():
    return render_template('policy.html')


@main.route('/user', methods=['GET','POST'])
def user():
    return render_template('user.html')


@main.route('/notification')
def notification():
    return render_template('notification.html')