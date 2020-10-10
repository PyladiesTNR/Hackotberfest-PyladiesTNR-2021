from flask import Flask, render_template, json
import os

app = Flask(__name__)

contributors = {
    """
    To add a card in the home page, add your information same as the above [N.B: Do not forget the comma before adding your key/value pair] 
    Pour ajouter une carte dans la page d'accueil, ajoutez les mêmes informations que ci-dessus [N.B. : N'oubliez pas la virgule avant d'ajouter votre configuration].
    """
    "Mahaly": {
        "name": "Mahalinoro Razafimanjato",
        "about": "I am passionate about programming. I enjoy UI design and creating design with Figma. Besides that, I am an Arch Linux user.",
        "twitter": "https://twitter.com/mahalinoro_raz",
        "github": "https://github.com/Mahalinoro",
        "facebook": "https://web.facebook.com/Rz.mahaly/",
        "color": "pink",  # [Options: Blue | Pink]
    },
    "Fenoun": {
        "name": "Aina Anjary Fenomamy R.",
        "about": "currently, I'm a Full Stack Developer, I am passionate about IT Architecture and programming. I enjoy Ballet Dance and hikking",
        "twitter": "https://twitter.com/afenoum",
        "github": "https://github.com/anjaniacatus",
        "facebook": "https://web.facebook.com/fenoumR/",
        "color": "blue",  # [Options: Blue | Pink]
    },
}


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html", data=contributors)


if __name__ == "__main__":
    app.run()
