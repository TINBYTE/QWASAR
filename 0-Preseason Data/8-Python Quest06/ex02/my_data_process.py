import json

def my_data_process(param_1):
    # Récupérer l'en-tête (1ère ligne) et la découper en colonnes
    header = param_1[0].split(',')
    
    # Colonnes à ignorer
    ignored_columns = {"FirstName", "LastName", "UserName", "Coffee Quantity"}
    
    # Indices des colonnes à conserver
    column_indices = [i for i, col in enumerate(header) if col not in ignored_columns]
    # Colonnes filtrées dans l'ordre
    selected_columns = [header[i] for i in column_indices]

    # Initialisation du dictionnaire résultat
    result = {col: {} for col in selected_columns}

    # Parcours des lignes de données (sauf l'en-tête)
    for row in param_1[1:]:
        values = row.split(',')
        for i in column_indices:
            col_name = header[i]
            value = values[i]
            if value not in result[col_name]:
                result[col_name][value] = 1
            else:
                result[col_name][value] += 1

    # Conversion en JSON string sans espaces inutiles
    return json.dumps(result, separators=(',', ':'))
    
input_data = [
 "Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At",
 "Male,Carl,Wilderman,carl,yahoo.com,21->40,Seattle,Safari iPhone,2,afternoon",
 "Male,Marvin,Lind,marvin,hotmail.com,66->99,Detroit,Chrome Android,2,afternoon",
 "Female,Shanelle,Marquardt,shanelle,hotmail.com,21->40,Las Vegas,Chrome,1,afternoon",
 "Female,Lavonne,Romaguera,lavonne,yahoo.com,66->99,Seattle,Chrome,2,morning",
 "Male,Derick,McLaughlin,derick,hotmail.com,41->65,Chicago,Chrome Android,1,afternoon"
]

print(my_data_process(input_data))