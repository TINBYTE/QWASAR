#Input: 
#       "Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At\n
#        Male,Carl,Wilderman,carl,wilderman_carl@yahoo.com,29,Seattle,Safari iPhone,2,2020-03-06 16:37:56\n
#        Male,Marvin,Lind,marvin,marvin_lind@hotmail.com,77,Detroit,Chrome Android,2,2020-03-02 13:55:51\n
#        Female,Shanelle,Marquardt,shanelle,marquardt.shanelle@hotmail.com,21,Las Vegas,Chrome,1,2020-03-05 17:53:05\n
#        Female,Lavonne,Romaguera,lavonne,romaguera.lavonne@yahoo.com,81,Seattle,Chrome,2,2020-03-04 10:33:53\n
#        Male,Derick,McLaughlin,derick,mclaughlin.derick@hotmail.com,47,Chicago,Chrome Android,1,2020-03-05 15:19:48\n"
#Output: 
#        ["Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At", 
#        "Male,Carl,Wilderman,carl,yahoo.com,21->40,Seattle,Safari iPhone,2,afternoon", 
#        "Male,Marvin,Lind,marvin,hotmail.com,66->99,Detroit,Chrome Android,2,afternoon", 
#        "Female,Shanelle,Marquardt,shanelle,hotmail.com,21->40,Las Vegas,Chrome,1,afternoon",
#        "Female,Lavonne,Romaguera,lavonne,yahoo.com,66->99,Seattle,Chrome,2,morning", 
#        "Male,Derick,McLaughlin,derick,hotmail.com,41->65,Chicago,Chrome Android,1,afternoon"]
import datetime

def my_data_transform(csv_content):
    lines = csv_content.strip().split('\n')  # On retire les espaces vides éventuels
    if not lines:
        return []
    
    result = [lines[0]]  # Garder la ligne d'en-tête telle quelle
    
    for line in lines[1:]:
        if not line.strip():
            continue  # Ignorer les lignes vides
            
        columns = line.split(',')
        if len(columns) < 10:
            continue  # Si ligne incomplète, on la saute
            
        # 📧 Traiter Email (extraire le provider)
        email = columns[4]
        if '@' in email:
            columns[4] = email.split('@')[1]
        
        # 🎂 Transformer Age en groupe
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
                age_group = str(age)
            columns[5] = age_group
        except ValueError:
            pass  # On ignore si age non convertible
        
        # ⏰ Transformer Order At en moment de la journée
        try:
            order_time = datetime.datetime.strptime(columns[9], '%Y-%m-%d %H:%M:%S')
            hour = order_time.hour
            if 6 <= hour < 12:
                time_group = "morning"
            elif 12 <= hour < 18:
                time_group = "afternoon"
            elif 18 <= hour < 24:
                time_group = "evening"
            else:
                time_group = "night"
            columns[9] = time_group
        except ValueError:
            pass  # On ignore si date invalide
        
        # ✅ Ajouter la ligne transformée
        result.append(','.join(columns))  # <-- ✔ Parenthèse FERMÉE ici
        
    return result
