# -*- coding: utf-8 -*-

from services.insee import get_population

def get_population_insee(lon, lat, dist):
	distDegree = dist * 0.0001 / 7.89 #Conversion des mètres en degrés
	left = lon - distDegree
	right = lon + distDegree
	top = lat + distDegree
	bottom = lat - distDegree
	if left > right :
		left = right
		right = lon + distDegree
	if bottom > top :
		top = bottom
		bottom = lat + distDegree
	return get_population(left,bottom,right,top)