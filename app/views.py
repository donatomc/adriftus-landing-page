from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")

#@app.route("/tutorials")
#def tutorials():
#    return render_template("tutorials.html")

#@app.route("/partners")
#def partners():
#    return render_template("partners.html")

#@app.route("/shop")
#def shop():
#    return render_template("shop.html")