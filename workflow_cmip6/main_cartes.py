
##------------------------------------------------------------------------------------------------
#
#					IMPORTS NÉCESSAIRES POUR LE CODE
#
##------------------------------------------------------------------------------------------------

import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.patches
#from mpl_toolkits.axes_grid1 import make_axes_locatable
#import cartopy.feature as cfeature
#import cartopy.crs as ccrs
import sys
import os
#import matplotlib.image as mpimg
#from random import uniform
#IMPORT DES MODULES CREES
import Lecture as LECTURE
#import carte as CARTE
import Densité as DENSITE
#import Carte_densité as CARTE_DENSITE
import pickle

##------------------------------------------------------------------------------------------------
#
#					DONNÉES NÉCESSAIRES POUR LA CRÉATION DE LA CARTE DE DENSITÉ
#
##------------------------------------------------------------------------------------------------
title="Carte de densité"
lon_min=-90 
lon_max=90
lat_min=-90
lat_max=90
zradius=3.0e+5
resolution=1.5
ires=4
##------------------------------------------------------------------------------------------------
#
#					LECTURE, REFORMATAGE ET FILTRAGE DES DONNEES DE FICHIERS DE TRACKING
#
##------------------------------------------------------------------------------------------------

file = "Tracks_PCBR_19500101-20091231.txt" 		# Modifier le jeu de données ici

#file =sys.argv[1]
"""
Domaine =[-90,30,30,90]

cwd = os.getcwd()
os.system('mkdir Plots')
path =os.path.join(cwd,'/Plots','Trajectoires_seuillées_FFBR.png')
plt.savefig(path)




print("================================= LECTURE DES DONNEES =================================")

NCyclones, Latitudes, Longitudes, Pressure, Vortex, Heures, Jours, Mois, Annees, Boundaries = LECTURE.ReadFile(file)


print("############ LECTURE DES DONNEES : OK ##################")

Variableaseuiller = Pressure 				#Indiquer ici la variable à seuiller parmi celles présentées ci-dessus
seuil = None						#seuil = None
SensDuSeuil = 'majoration'				#Sens du seuil : 'majoration','minoration' ou 'egalité'

print("=============== Données non seuillées =================")

Listecyclonesnonseuilles = LECTURE.FilteringSEUIL(Variableaseuiller,seuil,SensDuSeuil,Latitudes,Longitudes,Pressure,Vortex,Heures,Jours,Mois,Annees)
LatitudesNS,LongitudesNS,PressureNS,VortexNS,HeuresNS,JoursNS,MoisNS,AnneesNS = LECTURE.FilteredData(Listecyclonesnonseuilles,Latitudes,Longitudes,Pressure,Vortex,Heures,Jours,Mois,Annees)

print("############ FILTRAGE DES DONNEES : OK ##################")
"""
##------------------------------------------------------------------------------------------------
#
#					TRACE DES CARTES DE TRAJECTOIRES DES CYCLONES
#
##------------------------------------------------------------------------------------------------
"""
print("================================= CARTE 0 : TRACE DES TRAJECTOIRES DES CYCLONES SANS FILTRE ==============================")

ax=CARTE.Background(Domaine,'PlateCarree')
for cyclone in Listecyclonesnonseuilles :
	ax=CARTE.DrawTrajectory(Longitudes[cyclone], Latitudes[cyclone],ax,'cyan')
plt.savefig('Trajectoires_non_seuillées_PCBR.png')
"""
"""



Variableaseuiller = Pressure 				# Indiquer ici la variable à seuiller parmi celles présentées ci-dessus
seuil =1000						#Si seuil = None, pas de changement sur la liste
SensDuSeuil = 'majoration'				#Sens du seuil : 'majoration','minoration' ou 'egalité'


print("=============== FILTRAGE DES DONNEES PAR SEUILLAGE  A ", seuil, " ===============")

Listecyclonesseuilles = LECTURE.FilteringSEUIL(Variableaseuiller,seuil,SensDuSeuil,Latitudes,Longitudes,Pressure,Vortex,Heures,Jours,Mois,Annees)
LatitudesS,LongitudesS,PressureS,VortexS,HeuresS,JoursS,MoisS,AnneesS = LECTURE.FilteredData(Listecyclonesseuilles,Latitudes,Longitudes,Pressure,Vortex,Heures,Jours,Mois,Annees)

"""





"""



print("================================= CARTE 1 : TRACE DES TRAJECTOIRES DES CYCLONES FILTRES PAR SEUIL ==============================")
ax=CARTE.Background(Domaine,'PlateCarree')
for cyclone in Listecyclonesseuilles :
	ax=CARTE.DrawTrajectory(Longitudes[cyclone], Latitudes[cyclone],ax,'cyan')


plt.savefig('Trajectoires_seuillées_PCBR.png')


print("================================= CARTE 2 : TRACE DES TRAJECTOIRES DES CYCLONES FILTRES PAR QUANTILES ==============================")

ax=CARTE.Background(Domaine,'PlateCarree')


STRONGCyclonesList, WEAKCyclonesList, EXTREMECyclonesList,  NSTRONGCyclones, NWEAKCyclones , NEXTREMECyclones =LECTURE.FilteringQUANTILES(Listecyclonesnonseuilles,Pressure,Vortex)
for cyclone in STRONGCyclonesList :
	ax=CARTE.DrawTrajectory(LongitudesNS[cyclone], LatitudesNS[cyclone],ax,'red')
for cyclone in WEAKCyclonesList : 
	ax=CARTE.DrawTrajectory(LongitudesNS[cyclone], LatitudesNS[cyclone],ax,'cyan')
plt.savefig('Trajectoires_seuillées_par_quantiles_PCBR.png')

##------------------------------------------------------------------------------------------------
#
#					TRACÉ DES CARTES DE DENSITÉ
#
##------------------------------------------------------------------------------------------------

print("================================= CARTE 3 : TRACE D'UNE CARTE DE DENSITÉ NON SEUILLÉE==============================")
tab_lat=[]
tab_lon=[]
for cyclone in Listecyclonesnonseuilles: # for cyclone in FilteredCyclonesList
	lat = LatitudesNS[cyclone]
	lon = LongitudesNS[cyclone]
	for x in range(len(lat)-1):
		lattemp=np.linspace(lat[x],lat[x+1], num=2, endpoint=True)
		tab_lat=np.concatenate((tab_lat,lattemp))
	for y in range(len(lon)-1):
		lontemp=np.linspace(lon[y],lon[y+1], num=2, endpoint=True)
		tab_lon=np.concatenate((tab_lon,lontemp))
N_ech=len(tab_lat)
matrice_densite=DENSITE.Densite(N_ech,tab_lon,tab_lat,lat_max,lat_min,lon_max,lon_min,zradius,resolution,ires)
matrice_densite=np.transpose(matrice_densite)
title="Carte de densité totale PCBR non seuillée"
ax=CARTE_DENSITE.Carte_Densité(matrice_densite,lat_min,lat_max,lon_min,lon_max,resolution,zradius,N_ech,title=title,vmax=max)
plt.savefig('densité_totale_PCBR_non_seuillée.png')

##------------------------------------------------------------------------------------------------
#
#					CRÉATION DES ANIMATIONS GIF POUR LES CARTES DE DENSITÉ MENSUELLE
#
##------------------------------------------------------------------------------------------------


print("================================= CARTE 4 : TRACE DU GIF DES DENSITÉS MENSUELLES ==============================")
for i in range (1,13):
	FilteredCyclonesList=LECTURE.FilteringSEUIL(Mois,i,'egalité',LatitudesS,LongitudesS,PressureS,VortexS, Heures, Jours, Mois, Annees)
	tab_lat=[]
	tab_lon=[]
	for cyclone in FilteredCyclonesList: # for cyclone in FilteredCyclonesList
		lat = Latitudes[cyclone]
		lon = Longitudes[cyclone]
		for x in range(len(lat)-1):
			lattemp=np.linspace(lat[x],lat[x+1], num=2, endpoint=True)
			tab_lat=np.concatenate((tab_lat,lattemp))
		for y in range(len(lon)-1):
			lontemp=np.linspace(lon[y],lon[y+1], num=2, endpoint=True)
			tab_lon=np.concatenate((tab_lon,lontemp))

	N_ech=len(tab_lat)
	matrice_densite=DENSITE.Densite(N_ech,tab_lon,tab_lat,lat_max,lat_min,lon_max,lon_min,zradius,resolution,ires)
	matrice_densite=np.transpose(matrice_densite)
	max=np.max(matrice_densite)
	ax=CARTE_DENSITE.Carte_Densité(matrice_densite,lat_min,lat_max,lon_min,lon_max,resolution,zradius,N_ech,vmax=max,title="Densité Mensuelle pour le mois n°"+str(i))
	plt.savefig('Densité_PCBR_pour_le_mois_N°'+str(i)+'.png')

cmd = 'convert -delay 50 Densité_PCBR_pour_le_mois_N°*.png Densité_mensuelle_PCBR.gif'
os.system(cmd)


##------------------------------------------------------------------------------------------------
#
#					CRÉATION DES ANIMATIONS GIFS POUR LES CARTES DE DENSITÉ SAISONNIÈRE
#
##------------------------------------------------------------------------------------------------

print("================================= CARTE 4.2 : TRACE DU GIF DES DENSITÉS SAISONNIÈRES ==============================")
tab_lat_winter=[]
tab_lon_winter=[]
tab_lat_summer=[]
tab_lon_summer=[]
tab_lat_spring=[]
tab_lon_spring=[]
tab_lat_fall=[]
tab_lon_fall=[]
winter=[1,2,12]
spring=[3,4,5]
summer=[6,7,8]
fall=[9,10,11]
for i in range (1,13):
	FilteredCyclonesList=LECTURE.FilteringSEUIL(MoisS,i,'egalité',LatitudesNS,LongitudesNS,PressureNS,VortexNS, HeuresNS, JoursNS, MoisNS, AnneesNS)
	LatitudesS1,LongitudesS1,PressureS1,VortexS1,HeuresS1,JoursS1,MoisS1,AnneesS1 = LECTURE.FilteredData(FilteredCyclonesList,LatitudesS,LongitudesS,PressureS,VortexS,HeuresS,JoursS,MoisS,AnneesS)
	for cyclone in FilteredCyclonesList: # for cyclone in FilteredCyclonesList
		if (i in winter)==True:
			lat = LatitudesS1[cyclone]
			lon = LongitudesS1[cyclone]
			for x in range(len(lat)-1):
				lattemp=np.linspace(lat[x],lat[x+1], num=2, endpoint=True)
				tab_lat_winter=np.concatenate((tab_lat_winter,lattemp))
			for y in range(len(lon)-1):
				lontemp=np.linspace(lon[y],lon[y+1], num=2, endpoint=True)
				tab_lon_winter=np.concatenate((tab_lon_winter,lontemp))
		if (i in spring)==True:
			lat = LatitudesS1[cyclone]
			lon = LongitudesS1[cyclone]
			for x in range(len(lat)-1):
				lattemp=np.linspace(lat[x],lat[x+1], num=2, endpoint=True)
				tab_lat_spring=np.concatenate((tab_lat_spring,lattemp))
			for y in range(len(lon)-1):
				lontemp=np.linspace(lon[y],lon[y+1], num=2, endpoint=True)
				tab_lon_spring=np.concatenate((tab_lon_spring,lontemp))
		if (i in summer)==True:
			lat = LatitudesS1[cyclone]
			lon = LongitudesS1[cyclone]
			for x in range(len(lat)-1):
				lattemp=np.linspace(lat[x],lat[x+1], num=2, endpoint=True)
				tab_lat_summer=np.concatenate((tab_lat_summer,lattemp))
			for y in range(len(lon)-1):
				lontemp=np.linspace(lon[y],lon[y+1], num=2, endpoint=True)
				tab_lon_summer=np.concatenate((tab_lon_summer,lontemp))
		if (i in fall)==True:
			lat = LatitudesS1[cyclone]
			lon = LongitudesS1[cyclone]
			for x in range(len(lat)-1):
				lattemp=np.linspace(lat[x],lat[x+1], num=2, endpoint=True)
				tab_lat_fall=np.concatenate((tab_lat_fall,lattemp))
			for y in range(len(lon)-1):
				lontemp=np.linspace(lon[y],lon[y+1], num=2, endpoint=True)
				tab_lon_fall=np.concatenate((tab_lon_fall,lontemp))
N_ech=len(tab_lat_winter)
matrice_densite=DENSITE.Densite(N_ech,tab_lon_winter,tab_lat_winter,lat_max,lat_min,lon_max,lon_min,zradius,resolution,ires)
matrice_densite=np.transpose(matrice_densite)
max=np.max(matrice_densite)
title="Carte de densité hiver"
ax=CARTE_DENSITE.Carte_Densité(matrice_densite,lat_min,lat_max,lon_min,lon_max,resolution,zradius,N_ech,vmax=max,title=title)
plt.savefig('Densité_Saison_Hiver_PCBR.png')

N_ech=len(tab_lat_spring)
matrice_densite=DENSITE.Densite(N_ech,tab_lon_spring,tab_lat_spring,lat_max,lat_min,lon_max,lon_min,zradius,resolution,ires)
matrice_densite=np.transpose(matrice_densite)
max=np.max(matrice_densite)
title="Carte de densité printemps"
ax=CARTE_DENSITE.Carte_Densité(matrice_densite,lat_min,lat_max,lon_min,lon_max,resolution,zradius,N_ech,vmax=max,title=title)
plt.savefig('Densité_Saison_Printemps_PCBR.png')

N_ech=len(tab_lat_summer)
matrice_densite=DENSITE.Densite(N_ech,tab_lon_summer,tab_lat_summer,lat_max,lat_min,lon_max,lon_min,zradius,resolution,ires)
matrice_densite=np.transpose(matrice_densite)
max=np.max(matrice_densite)
title="Carte de densité été"
ax=CARTE_DENSITE.Carte_Densité(matrice_densite,lat_min,lat_max,lon_min,lon_max,resolution,zradius,N_ech,vmax=max,title=title)
plt.savefig('Densité_Saison_Été_PCBR.png')

N_ech=len(tab_lat_fall)
matrice_densite=DENSITE.Densite(N_ech,tab_lon_fall,tab_lat_fall,lat_max,lat_min,lon_max,lon_min,zradius,resolution,ires)
matrice_densite=np.transpose(matrice_densite)
max=np.max(matrice_densite)
title="Carte de densité automne"
ax=CARTE_DENSITE.Carte_Densité(matrice_densite,lat_min,lat_max,lon_min,lon_max,resolution,zradius,N_ech,vmax=max,title=title)
plt.savefig('Densité_Saison_Automne_PCBR.png')



cmd = 'convert -delay 60 Densité_Saison_*.png Densité_Saisonnière.gif'
os.system(cmd)



print("================================= CARTE 5 : TRACE DE LA DENSITÉ SEUILLÉE SUR UNE PERIODE TOTALE ==============================")



tab_lat=[]
tab_lon=[]
for cyclone in Listecyclonesseuilles: # for cyclone in FilteredCyclonesList
	lat = LatitudesS[cyclone]
	lon = LongitudesS[cyclone]
	for x in range(len(lat)-1):
		lattemp=np.linspace(lat[x],lat[x+1], num=2, endpoint=True)
		tab_lat=np.concatenate((tab_lat,lattemp))
	for y in range(len(lon)-1):
		lontemp=np.linspace(lon[y],lon[y+1], num=2, endpoint=True)
		tab_lon=np.concatenate((tab_lon,lontemp))

N_ech=len(tab_lat)
matrice_densite=DENSITE.Densite(N_ech,tab_lon,tab_lat,lat_max,lat_min,lon_max,lon_min,zradius,resolution,ires)
max=np.max(matrice_densite)
matrice_densite=np.transpose(matrice_densite)
ax=CARTE_DENSITE.Carte_Densité(matrice_densite,lat_min,lat_max,lon_min,lon_max,resolution,zradius,N_ech,vmax=max,title="Densité totale PCBR seuillée à "+str(seuil) )
plt.savefig('Densité_Totale_PCBR.png')


##------------------------------------------------------------------------------------------------
#
#					CRÉATION DES TRACÉS POUR LES CYCLONES EXTRÈMES
#
##-----------------------------------------------------------------------------------------------
print("================================ CARTE 6 : TRACÉ TRAJECTOIRE DE CYCLONES EXTRÈMES =====================================")
ax=CARTE.Background(Domaine,'PlateCarree')
CycloneList = LECTURE.FilteringSEUIL(Variableaseuiller,seuil,SensDuSeuil,Latitudes,Longitudes,Pressure,Vortex,Heures,Jours,Mois,Annees)
LatitudesS,LongitudesS,Pressure,Vortex,HeuresS,JoursS,MoisS,AnneesS = LECTURE.FilteredData(Listecyclonesseuilles,Latitudes,Longitudes,Pressure,Vortex,Heures,Jours,Mois,Annees)
Variableaseuiller = Pressure
STRONGCyclonesList, WEAKCyclonesList, EXTREMECyclonesList,  NSTRONGCyclones, NWEAKCyclones , NEXTREMECyclones =LECTURE.FilteringQUANTILES(CycloneList,Pressure,Vortex)
for cyclone in EXTREMECyclonesList :
	ax=CARTE.DrawTrajectory(Longitudes[cyclone], Latitudes[cyclone],ax,'red')
plt.savefig('Trajectoire_cyclones_extremes_PCBR.png')

print("================================ CARTE 7 : TRACÉ DENSITÉ DE CYCLONES EXTRÈMES =====================================")

tab_lat=[]
tab_lon=[]
for cyclone in EXTREMECyclonesList : 
	lat = Latitudes[cyclone]
	lon = Longitudes[cyclone]
	for x in range(len(lat)-1):
		lattemp=np.linspace(lat[x],lat[x+1], num=2, endpoint=True)
		tab_lat=np.concatenate((tab_lat,lattemp))
	for y in range(len(lon)-1):
		lontemp=np.linspace(lon[y],lon[y+1], num=2, endpoint=True)
		tab_lon=np.concatenate((tab_lon,lontemp))
N_ech=len(tab_lat)
matrice_densite=DENSITE.Densite(N_ech,tab_lon,tab_lat,lat_max,lat_min,lon_max,lon_min,zradius,resolution,ires)
matrice_densite=np.transpose(matrice_densite)
max=np.max(matrice_densite)
title="Carte de densité pour les cyclones extrêmes"
ax=CARTE_DENSITE.Carte_Densité(matrice_densite,lat_min,lat_max,lon_min,lon_max,resolution,zradius,N_ech,vmax=max,title=title)

plt.savefig('Densité_cyclones_extremes_PCBR.png')
"""

"""
def Formatage(Dictionnaire):
    Liste = []
    for cyclone in Dictionnaire.keys() :
        Liste = np.concatenate((Liste,Dictionnaire[cyclone]),axis = None)
    return Liste
Annees=Formatage(AnneesNS)
print(Annees)
Sauvegarde = open('Sauvegarde.txt','wb')
for annee in range(int(np.min(Annees)),int(np.max(Annees))+1,1):
    print('min :',int(np.min(Annees)),'max:',int(np.max(Annees)))
    print('annee :',annee)
    FilteredCyclonesList=LECTURE.FilteringSEUIL(AnneesNS,annee,'egalité',LatitudesNS,LongitudesNS,PressureNS,VortexNS, HeuresNS, JoursNS, MoisNS, AnneesNS)
    LatitudesS,LongitudesS,PressureS,VortexS,HeuresS,JoursS,MoisS,AnneesS = LECTURE.FilteredData(FilteredCyclonesList,LatitudesNS,LongitudesNS,PressureNS,VortexNS,HeuresNS,JoursNS,MoisNS,AnneesNS)
    tab_lat=[]
    tab_lon=[]
    for cyclone in FilteredCyclonesList: # for cyclone in FilteredCyclonesList
        print(cyclone)
        lat = LatitudesNS[cyclone]
        lon = LongitudesNS[cyclone]
        for x in range(len(lat)-1):
            lattemp=np.linspace(lat[x],lat[x+1], num=2, endpoint=True)
            tab_lat=np.concatenate((tab_lat,lattemp))
        for y in range(len(lon)-1):
            lontemp=np.linspace(lon[y],lon[y+1], num=2, endpoint=True)
            tab_lon=np.concatenate((tab_lon,lontemp))
    N_ech=len(tab_lat)
    matrice_densite=DENSITE.Densite(N_ech,tab_lon,tab_lat,lat_max,lat_min,lon_max,lon_min,zradius,resolution,ires)
    matrice_densite=np.transpose(matrice_densite)
    lon=matrice.shape[0]
    lat=matrice.shape[1]
    vecteur=matrice.reshape(1,lon*lat)

    pickle.dump(matrice_densite,Sauvegarde)
                                                                                                                                                      
Sauvegarde.close()

"""
Sauvegarde = open('Sauvegarde.txt','rb') 


for i in range(60):
    matrice=pickle.load(Sauvegarde)
    print(i)
    lon=matrice.shape[0]
    lat=matrice.shape[1]
    print(lon,lat)
    vecteur=matrice.reshape(1,lon*lat)
    print(vecteur.shape)
    if i==0 :
	    big_matrice = vecteur
    if i!=0:
	    big_matrice = np.concatenate((big_matrice,vecteur),axis=0)

ecart_type=np.std(big_matrice,axis=0)
print(ecart_type)
ecart_type=ecart_type.reshape(lon,lat)
print(ecart_type.shape)
for i in range(120):
	for j in range(120):
		print(ecart_type[i,j])

Sauvegarde.close()














##------------------------------------------------------------------------------------------------
#
#					COMPARAISON DENSITÉ POUR 2 MODÈLES
#
##------------------------------------------------------------------------------------------------



print("================================ CARTE 9 : COMPARATIF DEUX MODÈLES =====================================")

"""

file1 = "Tracks_PFBR_19500101-20091231.txt"
NCyclones, Latitudes, Longitudes, Pressure, Vortex, Heures, Jours, Mois, Annees, Boundaries = LECTURE.ReadFile(file1)
Variableaseuiller = Pressure 				# Indiquer ici la variable à seuiller parmi celles présentées ci-dessus
seuil = None						#Si seuil = None, pas de changement sur la liste
SensDuSeuil = 'majoration'				#Sens du seuil : 'majoration','minoration' ou 'egalité'

Listecyclonesseuilles1 = LECTURE.FilteringSEUIL(Variableaseuiller,seuil,SensDuSeuil,Latitudes,Longitudes,Pressure,Vortex,Heures,Jours,Mois,Annees)
LatitudesS1,LongitudesS1,PressureS1,VortexS1,HeuresS1,JoursS1,MoisS1,AnneesS1 = LECTURE.FilteredData(Listecyclonesseuilles1,Latitudes,Longitudes,Pressure,Vortex,Heures,Jours,Mois,Annees)



file2 = "Tracks_FFBR_20150101-20441231.txt"
NCyclones, Latitudes, Longitudes, Pressure, Vortex, Heures, Jours, Mois, Annees, Boundaries = LECTURE.ReadFile(file2)
Variableaseuiller = Pressure 				# Indiquer ici la variable à seuiller parmi celles présentées ci-dessus
seuil = None						#Si seuil = None, pas de changement sur la liste
SensDuSeuil = 'majoration'				#Sens du seuil : 'majoration','minoration' ou 'egalité'

Listecyclonesseuilles2 = LECTURE.FilteringSEUIL(Variableaseuiller,seuil,SensDuSeuil,Latitudes,Longitudes,Pressure,Vortex,Heures,Jours,Mois,Annees)
LatitudesS2,LongitudesS2,PressureS2,VortexS2,HeuresS2,JoursS2,MoisS2,AnneesS2 = LECTURE.FilteredData(Listecyclonesseuilles2,Latitudes,Longitudes,Pressure,Vortex,Heures,Jours,Mois,Annees)

tab_lat1=[]
tab_lon1=[]
tab_lat2=[]
tab_lon2=[]
for cyclone in Listecyclonesseuilles1: 
	lat1 = LatitudesS1[cyclone]
	lon1 = LongitudesS1[cyclone]
	for x in range(len(lat1)-1):
		lattemp=np.linspace(lat1[x],lat1[x+1], num=2, endpoint=True)
		tab_lat1=np.concatenate((tab_lat1,lattemp))
	for y in range(len(lon1)-1):
		lontemp=np.linspace(lon1[y],lon1[y+1], num=2, endpoint=True)
		tab_lon1=np.concatenate((tab_lon1,lontemp))
for cyclone in Listecyclonesseuilles2: 
	lat2 = LatitudesS2[cyclone]
	lon2 = LongitudesS2[cyclone]
	for x in range(len(lat2)-1):
		lattemp=np.linspace(lat2[x],lat2[x+1], num=2, endpoint=True)
		tab_lat2=np.concatenate((tab_lat2,lattemp))
	for y in range(len(lon2)-1):
		lontemp=np.linspace(lon2[y],lon2[y+1], num=2, endpoint=True)
		tab_lon2=np.concatenate((tab_lon2,lontemp))

N_ech1=len(tab_lat1)
N_ech2=len(tab_lat2)
matrice_densite1=DENSITE.Densite(N_ech1,tab_lon1,tab_lat1,lat_max,lat_min,lon_max,lon_min,zradius,resolution,ires)
matrice_densite1=np.transpose(matrice_densite1)
matrice_densite2=DENSITE.Densite(N_ech2,tab_lon2,tab_lat2,lat_max,lat_min,lon_max,lon_min,zradius,resolution,ires)
matrice_densite2=np.transpose(matrice_densite2)
matrice_densite=matrice_densite1 - matrice_densite2
print(np.min(matrice_densite))
ax=CARTE_DENSITE.Carte_Densité(matrice_densite,lat_min,lat_max,lon_min,lon_max,resolution,zradius,N_ech1,vmax=max,title=title)
plt.savefig('Carte_de_comparaison_densité_PFBR_FFBR.png')

"""
