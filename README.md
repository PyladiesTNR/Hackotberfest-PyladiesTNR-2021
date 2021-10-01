<img height=auto width=auto src="https://github.com/Mahalinoro/Hackotberfest-PyladiesTNR-2020/blob/main/public/main.png">

> **Announcement:** Happy Hacktoberfest 2020!! We need some help translating this *`*README.md** into **Malagasy** :madagascar: and **French** :fr:, if you are interested submit your PR and we will review it! Also, if you want to improve it - you are highly welcomed! For the Malagasy translation, edit the file: **README_MG**. For the French, edit this: **README_FR** 

## Introduction

## Get Started
Make sure you have git installed in you machine, [Git Installation Setup here](https://help.github.com/articles/set-up-git/).

### 1. Fork This Repository
Fork this repository by clicking the "Fork" button on top of this section.
A copy of this repository will be created in your personal profile.

### 2. Clone This Repository
Clone the forked repository to your machine. Go to your GitHub account, open the forked repository, click on the code button and then click the _copy to clipboard_ icon.

Open your machine's terminal and run the following command:

```
git clone "url of forked repository"
```

For example:

```
git clone "https://github.com/PyladiesTNR/Hackotberfest-PyladiesTNR-2020.git"
```
Here, a copy of this repository will appear in your local machine.

### 3. Create A Branch
Go to the repository containing the cloned repository in your machine (unless you are already there):
```
cd Hacktoberfest-PyladiesTNR-2020
```

After, create a branch with `git checkout` command:

```
git checkout -b your-new-branch-name
```

For example:
```
git checkout -b add-yourname-info
```
### 4. Make Changes & Commit
To add your card-name in the home page, with your prefered editor, edit the
file: static/contributors.json. Add your information same as in the file, put them at the bottom of the list.  [N.B: Do not forget the comma before adding your key/value pair] 

Pour ajouter une carte dans la page d'accueil, ajoutez les mêmes informations que vous
voyez dans le fichier. Mettez les tout en bas.  
[N.B. : N'oubliez pas la virgule avant d'ajouter votre configuration].
color options: Blue or Pink



```
vim contributors.json
````
After all the necessary changes are done, if you execute the command `git status`, you will see all of them.

Add those changes using the `git add` command:

```
git add contributors.json
```
Then, commit those changes using the `git commit` command:

```
git commit -m "Add <your-name> to the Information cards"
```
Do not forget to replace `<your-name>` by your name.

### 5. Wanna see your changes locally?
To see the changes that you have done, on your machine, do those commands:
```
python3 -m venv .env
source .env/bin/activate
pip3 install -r requirements.txt
python3 app.py
```
To check the version of your python and pip installed on your machine. Do those
commands:
- on a linux or mac osx terminal
```
python --version
pip --version
```
- on windows
```
```
if you don't have them installed on your machine. you can do the setup by following those link:
- linux: https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/
- windows: https://phoenixnap.com/kb/how-to-install-python-3-windows

By default, your changes should be visible on this url : http://127.0.0.1:5000 
### 6. Push Changes
Do this command on your branch, to enable pushing over ssh:
```
git remote set-url origin ssh://git@github.com/PyladiesTNR/Hackotberfest-PyladiesTNR-2020.git
```
Push your changes using the command `git push`:

```
git push -u origin <add-your-branch-name>
```

Do not forget to replace `<add-your-branch-name>` with the name of the your newly created branch.
### 7. Submit Your PR 
If you go to your repository on GitHub, you'll see a `Compare & pull request` button. Click on that button.
Finally, submit the pull request.
> **NB:** Your PR Will be reviewed and merged. Once, it will be merged, you will receive a notification by email.

### 8. Next Steps
Congrats you finally did it! Now, you can go ahead and find other repositories where you can start contributing.
<img align='center' height=auto width=auto src="https://media.giphy.com/media/3otPoS81loriI9sO8o/giphy.gif">

## License
[MIT LICENSE](https://github.com/PyladiesTNR/Hackotberfest-PyladiesTNR-2020/blob/main/LICENSE)


<hr></hr>      
<p align=center>
  <samp align=center><i>reach us on:</i></samp>
</p>

<p align=center>
  <a href="https://web.facebook.com/djangogirlsTNR"><img margin-right=20 height=30 width=30 src="https://github.com/Mahalinoro/Hackotberfest-PyladiesTNR-2020/blob/main/public/facebook.png"></a>
  <a href="https://twitter.com/PyladiesTNR"><img height=30 width=30 src="https://github.com/Mahalinoro/Hackotberfest-PyladiesTNR-2020/blob/main/public/twitterlight.png"></a>
</p>
