from flask import Flask, render_template,json
import os

app = Flask(__name__)

contributors = {
    "Mahaly" : 
        {   "name": "Mahalinoro Razafimanjato",
            "about": "I am passionate about programming. I enjoy UI design and creating design with Figma. Besides that, I am an Arch Linux user.",
            "twitter": "https://twitter.com/mahalinoro_raz",
            "github": "https://github.com/Mahalinoro",
            "facebook": "https://web.facebook.com/Rz.mahaly/",
            "color": "pink" # [Options: Blue | Pink]
        }
    # To add a card in the home page, add your information same as the above [N.B: Do not forget the comma before adding your key/value pair]
    # Pour ajouter une carte dans la page d'accueil, ajoutez les mêmes informations que ci-dessus [N.B. : N'oubliez pas la virgule avant d'ajouter votre configuration].
    }

cl
@app.route('/', methods=['GET'])
def home():
    return render_template("home.html", data=contributors)

if __name__ == '__main__':
    app.run()