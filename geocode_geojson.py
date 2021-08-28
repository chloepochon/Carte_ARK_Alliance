# On importe les modules CSV et JSON
import csv, json
# Import du module Nominatim de la librairie Geopy pour pouvoir réaliser le géocodage
from geopy.geocoders import Nominatim
# Import de l'OS et du module path pour paraméter le chemin de fichier
import os
from os import path
# Import de la librairie GeoJSON et des différents modules pour permettre le formatage des données en GeoJSON
from geojson import Feature, FeatureCollection, Point



# GÉOCODAGE DES COORDONNÉÉS MANQUANTES DANS LE FICHIER CSV

# Documentation : Cours de Thibault Clérice - M2 TNAH de l'École nationale des chartes : https://github.com/PonteIneptique/cours-python
# Documentation : https://blog.adrienvh.fr/2015/01/18/geocoder-en-masse-plusieurs-milliers-dadresses-avec-python-et-nominatim/
# Documentation : https://stackoverflow.com/questions/38480909/writing-into-certain-csv-columns-using-python

# Paramétrage de la variable du chemin relatif
path="./"

# On ouvre le fichier d'entrée en mode lecture (fin) et on ouvre un fichier de sortie en mode écriture (fout)
with open('data_map_complete_input.csv', 'r') as fin, open('data_map_complete_output.csv', 'w') as fout :
    # Avec la méthode .reader() on lit le contenu du fichier d'entrée et on le stocke dans la variable
    # On définit le retour à la ligne comme fin de ligne et la virgule comme délimiteur entre les colonnes
    fichier_lu = csv.reader(fin, lineterminator='\n', delimiter=',')
    # La méthode .writer() nous retourne un objet dans lequel on peut écrire
    # On définit le retour à la ligne comme fin de ligne et la virgule comme délimiteur entre les colonnes
    fichier_ecrit = csv.writer(fout, lineterminator='\n', delimiter=',')
    # Dans le fichier dédié à l'écriture, on écrit la ligne d'en-tête comprenant le nom des différentes colonnes
    fichier_ecrit.writerow([ 'org_id','org_who', 'org_what', 'org_when', 'org_when_yyyy_mm', 'org_field', 'org_area',
        'org_where', 'org_nfp', 'org_nr', 'org_op',
       'org_cc',  'org_year', 'org_policy',  'org_why', 'org_ezid','org_contact_surname', 'org_contact_firstname',   'org_contact_email',   'org_provider_surname',  
     'org_provider_firstname',  'org_provider_email',  'org_address_postal',  'org_address_location',    'org_address_map', 'org_latitude',    'org_longitude', 'org_postcode', 'org_country'])
    # Dans le fichier lu, on passe l'en-tête pour ne pas bloquer le calcul des coordonnées géographiques
    next(fichier_lu)
    # Grâce au module Nominatim, on paramètre l'outil de géocodage
    geocoder = Nominatim(user_agent="stage")
    # Pour chaque colonne dans le fichier lu, on définit le champ de chaque colonne et son numéro d'index
    for row in fichier_lu :
        org_id= row[0]
        who= row[1]
        what=row[2]
        when=row[3]
        when_yyyy_mm= row[4]
        field= row[5]
        area= row[6]
        where=row[7]
        nfp = row[8]
        nr= row[9]
        op= row[10]
        cc= row[11]
        year= row[12]
        policy= row[13]
        why=row[14]
        ezid= row[15]
        contact_surname=row[16]
        contact_firstname=row[17]
        contact_email=row[18]
        provider_surname=row[19]
        provider_firstname= row[20]
        provider_email= row[21]
        address_postal=row[22]
        address_location= row[23]
        address_map= row[24]
        latitude= row[25]
        longitude= row[26]
        postcode = row[27]
        country= row[28]
        # S'il n'y a pas de latitude dans la cellule de la colonne dédiée
        if not latitude:
        # Alors on récupère la valeur de la cellule correspondante dans la colonne "address_map" pour la géocoder
            location = geocoder.geocode(address_map)
            # Et à partir de cette localisation on récupère la latitude
            latitude = location.latitude
        # S'il n'y a pas de longitude dans la cellule de la colonne dédiée
        if not longitude:
            # Alors on récupère la valeur de la cellule correspondante dans la colonne "address_map" pour la géocoder
            location = geocoder.geocode(address_map) 
            # Et à partir de cette localisation on récupère la longitude   
            longitude = location.longitude
        # Si le nom de famille du contact n'est pas indiqué alors écrire "Not communicated"
        if not contact_surname :
            contact_surname = "Not communicated"
        # Si le prénom du contact n'est pas indiqué alors écrire "Not communicated"
        if not contact_firstname : 
            contact_firstname = "Not communicated"
        # Pour toutes ces données
        for i in zip([(latitude, longitude)]):
            # On (ré)écrit dans le fichier dédié à l'écriture le contenu de chaque colonne
            fichier_ecrit.writerow([org_id, who, what, when, when_yyyy_mm, field, area,
             where, nfp, nr, op, cc, year, policy, why, ezid, contact_surname, contact_firstname,
            contact_email, provider_surname, provider_firstname, provider_email, address_postal, address_location, address_map, latitude, longitude, postcode, country])
            # On affiche ces valeurs dans le terminal pour s'assurer du succès de l'opération de calcul
            print([org_id, who, address_map, latitude, longitude])
            

# BOUCLE DE RENOMMAGE

# On définit une variable renvoyant respectivement au nom de fichier de sortie et au nom de fichier d'entrée
# Documentation : https://stackoverflow.com/questions/2491222/how-to-rename-a-file-using-python
old_file = os.path.join(path, "data_map_complete_output.csv")
new_file = os.path.join(path, "data_map_complete_input.csv")
# On renomme le fichier de sortie par le nom du fichier d'entrée de façon à effectuer une boucle et permettre l'actualisation du fichier d'entrée
os.rename(old_file, new_file)

# CONVERSION DU FICHIER CSV EN GÉOJSON

# Documentation : https://stackoverflow.com/questions/48586647/python-script-to-convert-csv-to-geojson
# On définit une liste vide de propriétés
features = []
# On reprend le fichier d'entrée initial et actualisé
with open('data_map_complete_input.csv', newline='') as csvfile:
    # Avec la méthode .reader() on retourne un objet : le fichier lu
    reader = csv.reader(csvfile, delimiter=',')
    # On passe l'en-tête du fichier
    next(reader)
    # Pour chaque colonne dans le fichier lu, on définit le champ de chaque colonne et son numéro d'index
    for row in reader :
        org_id= row[0]
        who= row[1]
        what=row[2]
        when=row[3]
        when_yyyy_mm= row[4]
        field= row[5]
        area= row[6]
        where=row[7]
        nfp = row[8]
        nr= row[9]
        op= row[10]
        cc= row[11]
        year= row[12]
        policy= row[13]
        why=row[14]
        ezid= row[15]
        contact_surname=row[16]
        contact_firstname=row[17]
        contact_email=row[18]
        provider_surname=row[19]
        provider_firstname= row[20]
        provider_email= row[21]
        address_postal=row[22]
        address_location= row[23]
        address_map= row[24]
        latitude= row[25]
        longitude= row[26]
        postcode = row[27]
        country= row[28]
        # Pour chacun de ces champs       
        for org_id, who, what, when, when_yyyy_mm, field, area, where, nfp, nr, op, cc, year, policy, why, ezid, contact_surname, contact_firstname, contact_email, provider_surname, provider_firstname, provider_email, address_postal, address_location, address_map, latitude, longitude, postcode, country in reader:
            # Les latitudes et longitudes sont définies comme des coordonnées géographiques et des 'float' (décimaux)
            latitude, longitude = map(float, (latitude, longitude))
            # On ajoute à la liste des propriétés
            features.append(
                # Une propriété (Feature) ou chaque "Feature" représente une ligne/institution différente
                Feature(
                    # Les latitudes et longitudes sont définies comme des coordonnées de type "Point"
                    geometry = Point((longitude, latitude)),
                    # On définit pour chaque propriété ses caractéristiques selon la syntaxe JSON : une clé (key") associée à la valeur de la cellule dans chaque colonne
                    # définie en amont
                    properties = {
                        'who': who,
                        'what': what,
                        'when': when,
                        'when_yyyy_mm': when_yyyy_mm,
                        'field': field,
                        'area': area,
                        'where' : where,
                        'nfp' : nfp,
                        'nr' : nr,
                        'op' : op,
                        'cc' : cc,
                        'year' : year,
                        'policy' : policy,
                        'why' : why,
                        'ezid': ezid,
                        'contact_surname' : contact_surname,
                        'contact_firstname' : contact_firstname,
                        'contact_email' : contact_email,
                        'provider_surname' : provider_surname,
                        'provider_firstname' : provider_firstname,
                        'provider_email' : provider_email,
                        'address_postal' : address_postal,
                        'address_location' : address_location,
                        'address_map' : address_map,
                        'latitude' : latitude,
                        'longitude' : longitude,
                        'postcode': postcode,
                        'country': country
                    }
                )
            )
# On ajoute l'ensemble de ces propriétés dans une "collection de propriétés"
collection = FeatureCollection(features)
# on ouvre un fichier GeoJSON en mode écriture
with open("data.geojson", "w") as f:
    # On écrit dans ce fichier le contenu de cette "collection de propriétés"
    f.write('%s' % collection)