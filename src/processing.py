from typing import Dict, List


def filter_by_state(dict_list: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список словарей по указанному состоянию.

    Args:
        dict_list: Список словарей для фильтрации.
        state: Состояние для фильтрации (по умолчанию "EXECUTED").

    Returns:
        Отфильтрованный список словарей.
    """
    return [item for item in dict_list if item.get("state") == state]


def sort_dict_list_by_date(dict_list: List[Dict[str, object]], order: str = "desc") -> List[Dict[str, object]]:
    """
    Sorts a list of dictionaries by the value of the 'date' key.

    :param dict_list: list of dictionaries
    :param order: sort order ('asc' for ascending, 'desc' for descending)
    :return: sorted list of dictionaries
    """

    sorted_list = sorted(dict_list, key=lambda x: str(x["date"]), reverse=(order.lower() == "desc"))
    return sorted_list
