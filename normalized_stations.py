# normalized_stations.py

# data structure build from -mapa-subte.jpg file to associate subway stations with their corresponding subway line
# It is a list of dictionaries where each dict has the station letter as key and a list of stations as value
# Station names are accesed as stations_list_for_a_line = stations_to_lines[0-7][line-letter]
# if this are the "expected" names and i reach all the places where subway stations are named i will reach a point
# were i will have a list/dict of non expected -like the weirdo street names-
# kind of "audit_station_names func" ....audit function review the dataset and call is_station_name (this function should look for
# this sequence k = railway v = station k = station v = subway k = subway  v = yes k = name    v = Pichincha ....in a node and find the
# name key ...if found, call audit_station_names) 
# then we need to update_station_names for failed ones and then add the subway line information
stations_to_lines = [
					{ "A" : ["Plaza de Mayo", "Peru", "Piedras", "Lima", "Saenz Pena", "Congreso", "Pasco", "Alberti", "Plaza Miserere", "Loria", "Castro Barros", "Rio de Janeiro", "Acoyte", "Primera Junta", "Puan", "Carabobo", "San Jose de Flores", "San Pedrito"] },

					{ "B" : ["Leandro N. Alem", "Florida", "Carlos Pellegrini", "Uruguay", "Callao", "Pasteur Amia", "Pueyrredon", "Carlos Gardel", "Medrano", "Angel Gallardo", "Malabia O. Pugliese", "Dorrego", "F. Lacroze", "Tronador Villa Ortuzar", "De los Incas Parque Chas", "Echeverria", "Juan Manuel de Rosas Villa Urquiza"] },

					{ "C" : ["Retiro", "General San Martin", "Lavalle", "Diagonal Norte", "Av. de Mayo", "Moreno", "Independencia", "San Juan", "Constitucion"] },

					{ "D" : ["Catedral", "9 de Julio", "Tribunales Teatro Colon", "Callao", "Facultad de Medicina", "Pueyrredon", "Aguero", "Bulnes", "Scalabrini Ortiz", "Plaza Italia", "Palermo", "Ministro Carranza", "Olleros", "Jose Hernandez", "Juramento", "Congreso de Tucuman"] },

					{ "E" : ["Bolivar", "Belgrano", "Independencia", "San Jose", "Entre Rios Rodolfo Walsh", "Pichincha", "Jujuy", "Gral. Urquiza", "Boedo", "Av. La Plata", "Jose Maria Moreno", "Emilio Mitre", "Medalla Milagrosa", "Varela", "Plaza de los Virreyes Eva Peron"] },

					{ "H" : ["Las Heras", "Santa Fe Carlos Jauregui", "Cordoba", "Corrientes", "Once - 30 de Diciembre", "Venezuela", "Humberto I", "Inclan", "Caseros", "Parque Patricios", "Hospitales"] },

 					{ "P" : ["Int. Saguier", "Balbastro", "Mariano Acosta", "Somellera", "Ana Maria Janer", "Ntra. Sra. de Fatima", "Fernandez de la Cruz", "Pte. Illia", "Parque de la Ciudad", "Cecilia Grierson", "Escalada", "Pola", "Ana Diaz", "Centro Civico Lugano", "Larrazabal", "Nicolas Descalzi", "Gabino Ezeiza", "General Savio"] }

]


def stations_by_line(line_letter):
	stations_in_a_line = []
	for dic_line in stations_to_lines:
		if dic_line.get(line_letter):
			stations_in_a_line = dic_line.get(line_letter)
	
	if stations_in_a_line != []:
		return stations_in_a_line
	else:
		print "wrong line letter selected : please choose A, B, C, D, E, H or P"

def all_stations():
	all_stations = []
	for dic_line in stations_to_lines:
		for lista in dic_line.values():
			all_stations = all_stations + lista
	return all_stations
