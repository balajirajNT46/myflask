from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

app.config.from_object('core.config.DevelopmentConfig')
# print(app.config)

from core.auth.controller import app as auth
app.register_blueprint(auth)