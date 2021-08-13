# Carte des autorités nommantes de l'ARK Alliance


:camera_flash: **Présentation du projet**

Cette carte a été développée durant mon stage réalisé au SIAF dans le cadre de ma deuxième année de master "Technologies numériques appliquées à l'Histoire" de l'Ecole nationale des chartes.
La carte représente l'ensemble des autorités nommantes inscrites au registre international ARK disponible à cette adresse : https://n2t.net/e/pub/naan_registry.txt
> NB : Cette carte ne représente que les autorités nommantes inscrites au registre au 12 juillet 2021.

 
:gear: **Les fonctionnalités**

Le projet comprend trois fichiers principaux :
* Le fichier CSV reprend l'ensemble des données du registre et ont été enrichies.
* Un script Python permettant le calcul des coordonnées géographiques à partir du fichier CSV et le formatage de l'ensemble des données en GeoJSON.
* Un fichier HTML pour la représentation de la carte.

Il comprend également le fichier des données formatées en GeoJSON et l'image PNG pour l'affichage des marqueurs.
  
:desktop_computer: **Installation**
 
 * Via son terminal, l'utilisateur-ice doit créer un environement virtuel dans un dossier de son choix : `virtualenv env -p python3`
 * L'utilisateur-ice devra installer des packages et libraries : 
  1. Pour cela il doit sourcer son environnement virtuel 
    -> dans le dossier choisi faire la commande `source env/bin/activate` 
  2.  Puis : 
       - Geopy : `pip install geopy`
       - GeoJSON : `pip install geojson`
       
  OU installer les packages nécessaires directement avec la commande `pip install -r requirements.txt`
  
  3. Vérifier que tout est bien installé : `pip freeze`
  4. Désactiver l'environnement : `deactivate`
 
 * Enfin l'utilisateur-ice devra cloner le dossier : `git clone https://github.com/chloepochon/Carte_ARK_Alliance`
 
 * Il pourra alors lancer la carte : 
    - Via le terminal dans le dossier du projet, simuler le server http : `python3 -m http.server`
    - Aller sur http://0.0.0.0:8000/ 
    - Cliquer sur map_ark_alliance.html
  
  
 :earth_africa: ** Utilisation **
  
  - Dans le fichier CSV, entrer l'adresse de votre choix dans la colonne 'address_map'
  - Dans votre terminal, lancer le calcul avec la commande python `python geocode_geojson.py`
  - Fermer le fichier.
  - Réactualiser la carte pour voir le nouveau marqueur apparaître.
