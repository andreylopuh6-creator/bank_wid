def filter_by_state(data, state='EXECUTED'):
    '''
    Фильтр списка словарей по ключу.
    
    '''
    result = []
    for item in data:
        if item.get('state') == state:
            result.append(item)
    return result

def sort_by_date(data, reverse=True):
    '''
    Сортирует список операций по дате.
    '''
    return sorted(data, key=lambda x: x.get('date',''),reverse=reverse)