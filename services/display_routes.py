# -*- coding: utf-8 -*-

from database.database_access import get_dao
from gtfslib.model import Route
from gtfsplugins import decret_2015_1610
from database.database_access import get_dao

def get_routes(agency_id):
	dao = get_dao(agency_id)
	parsedRoutes = list()

	for route in dao.routes(fltr=Route.route_type == Route.TYPE_BUS):
		parsedRoute = dict()
		parsedRoute["name"] = route.route_long_name
		parsedRoutes.append(parsedRoute)

	return parsedRoutes

