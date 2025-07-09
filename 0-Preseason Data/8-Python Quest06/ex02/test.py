import datetime
import json

def my_csv_parser(param1, param2):
    param1 = param1.strip()
    return [row.split(param2) for row in param1.split("\n")]


def my_data_transform(csv_content):
    lines = csv_content.split('\n')
    if not lines:
        return []
    
    result = [lines[0]]  # Keep the header as is
    
    for line in lines[1:]:
        if not line.strip():
            continue
            
        columns = line.split(',')
        if len(columns) < 10:
            continue
            
        # Transform Email
        email = columns[4]
        if '@' in email:
            email_provider = email.split('@')[1]
            columns[4] = email_provider
        
        # Transform Age
        try:
            age = int(columns[5])
            if 1 <= age <= 20:
                age_group = "1->20"
            elif 21 <= age <= 40:
                age_group = "21->40"
            elif 41 <= age <= 65:
                age_group = "41->65"
            elif 66 <= age <= 99:
                age_group = "66->99"
            else:
                age_group = str(age)  # fallback for ages outside ranges
            columns[5] = age_group
        except ValueError:
            pass  # leave as is if not a number
        
        # Transform Order At
        order_time_str = columns[9]
        try:
            order_time = datetime.datetime.strptime(order_time_str, '%Y-%m-%d %H:%M:%S')
            hour = order_time.hour
            if 6 <= hour < 12:
                time_group = "morning"
            elif 12 <= hour < 18:
                time_group = "afternoon"
            elif 18 <= hour < 24:
                time_group = "evening"
            else:
                time_group = "night"  # for hours 0-5, though not in requirements
            columns[9] = time_group
        except ValueError:
            pass  # leave as is if not in expected format
        
        result.append(','.join(columns))
    
    return result


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
