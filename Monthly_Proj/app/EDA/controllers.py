from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

EDA = Blueprint('EDA', __name__, url_prefix='/EDA')

@EDA.route('/', methods=['GET'])
def show_EDA():
    return render_template("view_EDA/EDA_note.html")

@EDA.route('/note/', methods=['GET'])
def show_EDA_note():
    return render_template("view_EDA/EDA_note.html")
