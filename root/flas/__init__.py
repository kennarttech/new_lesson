from tkinter import *
from flask import Flask
from flask import Blueprint
from flask import url_for, redirect, flash, render_template



app = Flask(__name__)



from flas.one.vum import home
from flas.two.boom import views


app.register_blueprint(home, url_prefix='/')
app.register_blueprint(views, url_prefix='/')

 




