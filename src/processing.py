from typing import Dict, List


def filter_by_state(dict_list: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
Функция фильтрует словари в данном списке, оставляя только те словари, у которых значение ключа "state".
    """
    return [item for item in dict_list if item.get("state") == state]


def sort_dict_list_by_date(dict_list: List[Dict[str, object]], order: str = "desc") -> List[Dict[str, object]]:
    """
Функция сортирует словари в данном списке в соответствии с ключом "date", преобразуя дату в строку перед сравнением.
    """

    sorted_list = sorted(dict_list, key=lambda x: str(x["date"]), reverse=(order.lower() == "desc"))
    return sorted_list
