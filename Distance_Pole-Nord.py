POLE_NORD = 86, 172 # Valeur pole nord magnétique en format DD
PARIS = 48, 51, 23.81, 2, 21, 7.999 # Localisation test en format D, M, S, D, M, S (vertical, horizontal)

def dms_to_dd(dms): # Fonction pour convertir D, M, S, D, M, S à DD, DD
    degv, minv, secv, degh, minh, sech = dms # Décortiquer les données du dms-dms test
    return degv + minv/60 + secv/3600, degh + minh/60 + sech/3600 # Retourner le DD, DD converti

def dist_dms_to_dd_pole_nord(dms): # Fonction pour retourner l'hypothénuse entre 2 points DD
    verti, horiz = dms_to_dd(dms) # Aller chercher des DD convertis
    pnverti, pnhoriz = POLE_NORD # Décortiquer les DD du pole nord
    return ((pnverti - verti)**2 + (pnhoriz - horiz)**2)**0.5 # Retourner l'hypothénuse (la distance entre les 2 points)

print(dist_dms_to_dd_pole_nord(PARIS)) # Testons avec PARIS