from flask import render_template, current_app as app
from app import db


@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404


@app.errorhandler(403)
def forbidden(error):
    return render_template("403.html"), 403

