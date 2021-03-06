import json
import os
from flask import Blueprint, render_template, current_app as app
apartment = Blueprint('apartment', __name__)

@apartment.route('/apartment/<string:fewo>')
def init(fewo):
    import os
    res_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static')

    data = json.load(open(os.path.join(res_path, 'content', 'apartments.json'), encoding='utf-8'))
    images = []

    for filename in os.listdir(os.path.join(res_path, 'img', 'apartments', fewo ,'rooms')):
        if filename.split(".")[-1].lower() in ["png", "jpg", "jpeg"]:
            images.append('apartments/' + fewo + '/rooms/' + filename)
        else:
            continue
    filename = os.listdir(os.path.join(res_path, 'img', 'apartments', fewo, 'thumbnail'))[0]
    thumbnail = 'apartments/' + fewo + '/thumbnail/' + filename
    
    return render_template("apartment.html", contact=app.config['CONTACT'], info=data[fewo], images=images, thumbnail=thumbnail)

