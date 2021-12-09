def spanish_and_brazilian_fruits(spanish_fruits, brazilian_fruits):
    list = []
    for i in spanish_fruits:
        for j in brazilian_fruits:
            if i == j:
                list.append(i)
    return list

def spanish_and_japan_fruits(spanish_fruits, japanese_fruits):
    return spanish_and_brazilian_fruits(spanish_fruits, japanese_fruits)

def brazilian_and_japan_fruits(brazilian_fruits, japanese_fruits):
    return spanish_and_brazilian_fruits(brazilian_fruits, japanese_fruits)

def popular_spanish_or_brazilian_fruits(popular_fruits, spanish_fruits, brazilian_fruits):
    list = []
    for i in popular_fruits:
        for j in spanish_fruits:
            for k in brazilian_fruits:
                if i == j == k:
                    list.append(i)
    return list

def popular_only_spanish_fruits(popular_fruits, spanish_fruits, japanese_fruits, brazilian_fruits):
    list = []
    for i in popular_fruits:
        for j in spanish_fruits:
            for k in japanese_fruits:
                for l in brazilian_fruits:
                    if i == j == k == l:
                        list.append(i)
    return list

def only_yahoo_emails(emails_list):
    list = []
    for i in emails_list:
        if i.lower().find("yahoo") != -1:
            if i not in list:
               list.append(i)
    result = set(list)
    return result

def only_hotmail_emails(emails_list):
    list = []
    for i in emails_list:
        if i.lower().find("hotmail") != -1:
            if i not in list:
               list.append(i)
    result = set(list)
    return result

def only_br_emails(emails_list):
    list = []
    for i in emails_list:
        if i.lower().find("com.br") != -1:
            if i not in list:
               list.append(i)
    result = set(list)
    return result
