<img height=auto width=auto src="public/hack2021-light.png">

> **Announcement:** Salut! Happy Hacktoberfest 2021! Nous avons besoin de ton aide pour la traduction de ce **README.md** en **Français** :fr:. Si cela t'intèresse tu peux faire un PR. Nous serions ravis de faire un review. Si tu as aussi une proposition pour ameliorer ceux qui est déja écrit, ce serait cool! :)  


## Commencer
Assurez-vous que Git est installé sur votre machine, [Installation de Git ici](https://help.github.com/articles/set-up-git/).

### 1. Créer un fork(copie) de ce dépôt
Créer un fork de ce dépôt en cliquant sur le bouton "Fork" en haut de cette section.
Une copie de ce dépôt sera créée sur votre compte github personnel.

### 2. Cloner le dépôt forké
Cloner sur votre machine le dépôt que vous venez de forker. Allez sur votre compte Github, ouvrez le dépôt forké, cliquez sur le bouton **code** et ensuite cliquez l'icône _copy to clipboard_.

Ouvrez le terminal de votre machine et exécutez la commande suivante :

```
git clone "url du dépôt forké"
```

Par exemple:

```
git clone "https://github.com/PyladiesTNR/Hackotberfest-PyladiesTNR-2021.git"
```
Une copie du dépôt forké apparaîtra dans votre machine locale.

### 3. Créer une branche
Entrez dans le dépôt cloné sur votre machine(sauf si vous êtes déjà là):
```
cd Hacktoberfest-PyladiesTNR-2021
```
Ensuite, créez une branche avec la commande `git checkout`:

```
git checkout -b nom-de-votre-nouvelle-branche
```

Par example:
```
git checkout -b ajouter-votrenom-info
```
### 4. Effectuer des changements & Fait un "Commit"
Pour ajouter une carte dans la page d’accueil, avec votre éditeur préféré, modifiez le fichier: static/contributors.json. Ajoutez vos informations comme vous voyez dans le fichier, mettez-les tout en bas de la liste. [N.B: N’oubliez pas la virgule avant d’ajouter vos informations]

```
vim contributors.json
````
Après avoir effectué toutes les modifications nécessaires, si vous exécutez la commande `git status`, vous les verrez toutes.

Ajoutez ces modifications en utilisant la commande `git add` :

```
git add contributors.json
```

Ensuite, commitez ces modifications en utilisant la commande `git commit` :

```
git commit -m "Ajouter <votre-nom> à la fiche d'information"
```
N'oubliez pas de remplacer `<votre-nom>` par votre nom.

### 5. Voulez-vous voir vos modifications localement sur votre machine?
Pour voir les changements que vous avez effectués, sur votre machine, exécutez ces commandes :

```
python3 -m venv .env
source .env/bin/activate
pip3 install -r requirements.txt
python3 app.py
```
Pour savoir la version de python et pip installée sur votre machine, executez ces deux commandes: 
- sur un terminal linux ou mac osx
```
python --version
pip --version
```
<!-- Ina ny an'i windows toa tsy misy? -->
- sur windows
```
python --version
```

Si vous ne les avez pas installés sur votre machine, vous pouvez faire la configuration en suivant ces tutoriels:
- linux: https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/
- windows: https://phoenixnap.com/kb/how-to-install-python-3-windows

Par défaut, vos modifications doivent être visibles sur cette url :
http://127.0.0.1:5000 
Pour pouvoir envoyer vos changements dans le dépôt forké sur votre compte github via shh, exécutez cette commande:

```
git remote set-url origin ssh://git@github.com/PyladiesTNR/Hackotberfest-PyladiesTNR-2020.git
```
Envoyez vos modifications en exécutant la commande `git push`:

```
git push -u origin <ajouter-le-nom-de-votre-branche>
```

N’oubliez pas de remplacer `<ajouter-le-nom-de-votre-branche>` par le nom de la branche que vous avez créée.

### 7. Créer votre Pull Request(PR)
Si vous allez dans le dépôt forké sur votre compte github, vous verrez un bouton `Compare & pull request`. Cliquez ce bouton.
Enfin, cliquez `Create pull request`

> **NB:** Votre PR sera examiné et vous recevrez une notification par email quand vos changements seront fusionnés dans ce dépôt original.

### 8. Prochaines étapes
Félicitations! Vous l'avez fait! Vous pouvez maintenant chercher d'autres dépôts auxquels contribuer. 
<img align='center' height=auto width=auto src="https://media.giphy.com/media/3otPoS81loriI9sO8o/giphy.gif">

## License
[MIT LICENSE](https://github.com/PyladiesTNR/Hackotberfest-PyladiesTNR-2020/blob/main/LICENSE)


<hr></hr>     

### CONTRIBUTEURS
<a href="https://github.com/PyladiesTNR/Hackotberfest-PyladiesTNR-2021/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=PyladiesTNR/Hackotberfest-PyladiesTNR-2021" />
</a>

<!-- <p align=center>
  <samp align=center><i>reach us on:</i></samp>
</p>

<p align=center>
  <a href="https://web.facebook.com/djangogirlsTNR"><img margin-right=20 height=30 width=30 src="https://github.com/Mahalinoro/Hackotberfest-PyladiesTNR-2020/blob/main/public/facebook.png"></a>
  <a href="https://twitter.com/PyladiesTNR"><img height=30 width=30 src="https://github.com/Mahalinoro/Hackotberfest-PyladiesTNR-2020/blob/main/public/twitterlight.png"></a>
</p> -->
