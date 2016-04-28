# -*- coding: utf-8 -*-

from database import database_access
from gtfslib.model import Agency
from gtfslib.dao import Dao

def get_agencies():
	agencies = database_access.get_all_agencies()
	agencies_list = [None] * len(agencies)
	for i in range(len(agencies)):
		agencies_list[i] = {'name': agencies[i].agency_name, 'id': agencies[i].id}
		
	return agencies_list	
