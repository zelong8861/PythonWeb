# -*- coding:utf-8 -*-

from nowstagram import app
from flask import render_template, Flask, redirect

from nowstagram.models import Image


@app.route("/")
@app.route("/index")
def index():
    image = Image.query.order_by('id desc').limit(8).all()

    return render_template("index.html", images=image)

@app.route('/image/<int:image_id>/')
def image(image_id):
    image = Image.query.get(image_id)
    if image == None:
        return redirect('/')
    return render_template('pageDetail.html', image=image)

