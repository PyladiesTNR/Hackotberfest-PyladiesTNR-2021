<img height=auto width=auto src="https://user-images.githubusercontent.com/57705801/135631172-2cc14ad0-c97c-4a98-8d0d-42d26d7b2eb6.png">

> **Announcement:** Salama! Tratry ny Hacktoberfest 2021 indray! Mila ny fanampianao izahay handika an'ity **README.md** amin'ny teny **Malagasy** :mg:. Raha liana ianao dia afaka manao PR. Raha manana tolo-kevitra hanatsara ireo efa voasoratra ianao, dia ho tsara izany! :) 

## Manomboka
Hamarino tsara raha tafiditra ao anaty masininao Git, [Git "Installation" torolàlana ato](https://help.github.com/articles/set-up-git/).


## 1. "Fork" ito "Repository" ito:
"Fork" ito "Repository" ito amin'ny alalan'ny fanindriana ny tsindry "Fork" eo an-tampony ito "Repository" it.
Hisy "Repository" mitovy amin'ito hiforonina ao amin'ny "profile" pejinao.

## 2. "Clone" ito "Repository"
"Clone"-o ao anaty masininao ito "Repository" ito. Mandehana ao amin'ny kaonty GitHub-nao, sokafy ilay "Repository" nanaovanao "clone" teo, tsindrio eo amin'ny tsindrin'ny kaody ary tsindrio ny _copy to clipboard_.

Sokafy ny "terminal" ny masininao ary alefaso ity baiko manaraka ity:

```
git clone "url of forked repository"
```

Ohatra:

```
git clone "https://github.com/PyladiesTNR/Hackotberfest-PyladiesTNR-2020.git"
```
Hiseho ao amin'ny masininao ny tahadikan'io "Repository" io.

## 3. Mamorona "Branch" (Sampana) iray
Mankanesa any amin'ny "Repository" izay natao "clone" teo (raha tsy hoe efa eo ianao):
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

Ankehitriny ianao dia afaka mamorona sampana vaovao izay ahafahanao manamboatra ireo zavatra tinao atao amin'ilay "Repository"

## 4. Manaova Fanovana & "Commit"
Mba hanampiana ny anaranao ao amin'ny pejin'ny fandraisana, miaraka amin'ny "editeur de texte" tinao, dia amboarina ny
Rakitra: <strong>static/contributors.json</strong>. Ampidiro toy ny ao anatin'ilay rakitra ny fampahalalana mikasika anao, ataovy eo amin'ny farany ambany amin'ilay lisitra izany.  <strong>[N.B: Aza adino ilay comma alohan'ny hampidirana azy</strong>] 

Misafidiana loko: Manga na Mavokely


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
git commit -m "Nanampy `<anaranao>` tao amin'ny karatra"
```

Aza adino ny manolo ny `<anaranao>` amin'ny anaranao.

## 5. Te hahita ny fiovanao eo an-toerana?

Mba hahitana ireo fanovana nataonao, eo amin'ny masininao, dia alefaso ireto baiko ireto:
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
Raha tsy manana azy ireo nametraka azy ireo ao amin'ny masininao ianao. Afaka manao ny firafitra ianao amin'ny alalan'ny fanarahana ireo rohy ireo:
- linux: https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/
- windows: https://phoenixnap.com/kb/how-to-install-python-3-windows

Raha tsorina, tokony ho hita ao amin'ity url ity ny fanovanao : http://127.0.0.1:5000 

## 6. Push ny Fanovana nataonao
Ataovy izao didy izao eo amin'ny sampanao, mba hahafahanao manosika ny fanovana nataonao;
```
git remote set-url origin ssh://git@github.com/PyladiesTNR/Hackotberfest-PyladiesTNR-2020.git
```
Tsindrio ny fanovanao amin'ny fampiasana ny baiko 'git push':

```
git push -u origin<add-your-branch-name>
```

Aza adino ny manolo ny `<add-your-branch-name>` amin'ny anaran'ilay sampana vao noforoninao.

## 7. "Submit" ny "PR"-anao 
Raha mankany amin'ny trano fitahirizanao ao amin'ny GitHub ianao dia hahita bokotra `Mampitaha & misintona '. Tsindrio io bokotra io.
Omeo <a href=""> lohateny misy famaritana </a> ny fangatahanao misarika ary amin'ny famaritana, aza hadino ny milaza ny olana izay hakatony.
Ohatra, raha mamaha ny olana #123 ny PR, lazao ao amin'ny famaritanao ny PR 
```
resolves #123
```
Farany, alefaso ilay fangatahana fanovana!.
> **NB:** Hodinihina sy ho avoaka ny PR-nao. Raha vantany vao hivoaka izany, hahazo fampahafantarana amin'ny alalan'ny mailaka ianao.

## 8. Dingana Manaraka
Arahabaina ianao nanao izany tamin'ny farany! Ankehitriny, afaka miroso ianao ary mitady ireo "Repository" hafa izay ahafahanao manomboka mandray anjara.
<br><br>
<img align='center' height=auto width=auto src="https://media.giphy.com/media/3otPoS81loriI9sO8o/giphy.gif">

##  "License"
[MIT LICENSE](https://github.com/PyladiesTNR/Hackotberfest-PyladiesTNR-2020/blob/main/LICENSE)

### Mpandray Anjara
<a href="https://github.com/PyladiesTNR/Hackotberfest-PyladiesTNR-2021/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=PyladiesTNR/Hackotberfest-PyladiesTNR-2021" />
</a>
