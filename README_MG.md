<img height=auto width=auto src="https://user-images.githubusercontent.com/57705801/135631172-2cc14ad0-c97c-4a98-8d0d-42d26d7b2eb6.png">


# Fampidirana


## Manomboka
Ataovy azo antoka fa napetrakao ao amin'ny milinao ny git, [Git Installation Setup here](https://help.github.com/articles/set-up-git/).


## 1. Fork This Repository
Fork ity fitadiavana ity amin'ny alalan'ny fanindriana ny tsindry "Fork" eo an-tampon'ity fizarana ity.
Ny tahadikan'ity fitahirizana ity dia hoforonina ao amin'ny mombananao manokana.

## 2. Clone This Repository
Ajanony ny milina fitahirizana anao. Ho any amin'ny kaonty GitHub-nao, sokafy ny tobim-pamaharana misongadina, tsindrio eo amin'ny tsindrin'ny kaody ary tsindrio ny _copy amin'ny kisary clipboard_.

Sokafy ny terminaln'ny milina ary alefaso ity baiko manaraka ity:

```
git clone "url of forked envertiora"
```

Ohatra:

```
git clone "https://github.com/PyladiesTNR/Hackotberfest-PyladiesTNR-2020.git"
```
Hiseho ao amin'ny milina misy anao eo an - toerana ny tahadikan'io fitaovam - pitaterana io eto.

## 3. Mamorona A Branch
Mankanesa any amin'ny toeram-pitahirizana ahitana ny fitahirizana voaloko ao amin'ny milinao (raha tsy hoe efa eo ianao):
```
cd Hacktoberfest-PyladiesTNR-2020
```

Aorian'izay dia mamorona sampana iray misy baiko 'git checkout':

```
git checkout -b-new-branch-nomena
```

Ohatra:
```
git checkout -b add-yourname-info
```

Ankehitriny ianao dia nanangana sampana vaovao izay ahafahanao mametraka endrika vaovao na manamboatra ireo zavatra efa nialoha tapitra.

## 4. Make Changes & Commit
Mba hanampiana ny anaranao ao amin'ny pejin'ny fandraisanao, miaraka amin'ny tononkalo nodimandryo, dia amboarina ny
Rakitra: <strong>static/contributors.json</strong>. Ampidiro toy ny ao anatin'ilay rakitra ny fampahalalana mikasika anao, ataovy eo amin'ny farany ambany amin'ilay lisitra izany.  <strong>[N.B: Aza adino ilay comma alohan'ny hampidirana ny ekimpira manan-danja/sanda</strong>] 

Pour ajouter une carte dans la page d'accueil, ajoutez les mêmes informations que vous
voyez dans le fichier. Mettez les tout en bas.  
[N.B. : N'oubliez pas la virgule avant d'ajouter votre configuration].
Safidy loko: Manga na Mavokely


```
vim contributors.json
````
Aorian'ny fanatanterahana ireo fanovana rehetra ilaina, raha manatanteraka ny baiko 'git status' ianao, dia ho hitanao avokoa izy rehetra.

Ampio ireo fanovana ireo amin'ny alalan'ny fampiasana ny baiko 'git add':

```
git add contributors.json
```
Avy eo, omeo ireo fanovana ireo amin'ny fampiasana ny baiko 'git':

```
git commit -m "Ampio `<anaranao>` to ny karatra fampahalalam-baovao"
```

Aza adino ny manolo ny `<anaranao>` amin'ny anaranao.
## 5. Te hahita ny fiovanao eo an-toerana?

Mba hahitana ireo fanovana nataonao, eo amin'ny milinao, dia alefaso ireto baiko ireto:
```
python3 -m venv .env
source .env/bin/activate
pip3 install -r requirements.txt
python3 app.py
```
Mba hijerena ny dikan'ny python-nao sy ny pip napetraka teo amin'ny milinao. Ataovy ireo
baiko:
- eo amin'ny Fikandrana, linux na mac terminal
```
python --version
pip --version
```
Raha tsy manana azy ireo nametraka azy ireo ao amin'ny milinao ianao. Afaka manao ny firafitra ianao amin'ny alalan'ny fanarahana ireo rohy ireo:
- linux: https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/
- windows: https://phoenixnap.com/kb/how-to-install-python-3-windows

Raha tsorina, tokony ho hita ao amin'ity url ity ny fanovanao : http://127.0.0.1:5000 

## 6. Push Changes
Ataovy izao didy izao eo amin'ny sampanao, mba hahafahanao manosika ny varotra;
```
git remote set-url origin ssh://git@github.com/PyladiesTNR/Hackotberfest-PyladiesTNR-2020.git
```
Tsindrio ny fanovanao amin'ny fampiasana ny baiko 'git push':

```
git push -u origin<add-your-branch-name>
```

Aza adino ny manolo ny `<add-your-branch-name>` amin'ny anaran'ilay sampana vao noforoninao.

## 7. Submit Your PR 
Raha mankany amin'ny trano fitahirizanao ao amin'ny GitHub ianao dia hahita bokotra `Mampitaha & misintona '. Tsindrio io bokotra io.
Omeo <a href=""> lohateny misy famaritana </a> ny fangatahanao misarika ary amin'ny famaritana, aza hadino ny milaza ny olana izay hakatony.
Ohatra, raha mamaha ny olana #123 ny PR, lazao ao amin'ny famaritanao ny PR 
```
resolves #123
```
Farany, alefaso ilay fangatahana fisintahana!.
> **NB:** Hodinihina sy ho avoaka ny PR-nao. Raha vantany vao hivoaka izany, hahazo fampahafantarana amin'ny alalan'ny mailaka ianao.

## 8. Next Step
Arahabina ianao nanao izany tamin'ny farany! Ankehitriny, afaka miroso ianao ary mitady ireo fitahirizana hafa izay ahafahanao manomboka mandray anjara.
<br><br>
<img align='center' height=auto width=auto src="https://media.giphy.com/media/3otPoS81loriI9sO8o/giphy.gif">

##  License
[MIT LICENSE](https://github.com/PyladiesTNR/Hackotberfest-PyladiesTNR-2020/blob/main/LICENSE)

## Contributors List
<table>
	<tr>
		<td>
   <a href="https://github.com/PyladiesTNR/Hackotberfest-PyladiesTNR-2021/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=PyladiesTNR/Hackotberfest-PyladiesTNR-2021" />
</a>
		</td>
	</tr>
</table>
<hr></hr>      
<p align=center>
  <samp align=center><i>mahatratra anay:</i></samp>
</p>

<p align=center>
  <a href="https://web.facebook.com/djangogirlsTNR"><img margin-right=20 height=30 width=30 src="https://github.com/Mahalinoro/Hackotberfest-PyladiesTNR-2020/blob/main/public/facebook.png"></a>
  <a href="https://twitter.com/PyladiesTNR"><img height=30 width=30 src="https://github.com/Mahalinoro/Hackotberfest-PyladiesTNR-2020/blob/main/public/twitterlight.png"></a>
</p>
