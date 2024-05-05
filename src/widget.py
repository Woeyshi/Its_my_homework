from src.masks import mask_bank_account, mask_credit_card


def masked_cards(card_or_count: str) -> str:
    """
    Функция для отличия и замаскирования номеров карт/счётов
    """
    card_or_count_split = card_or_count.split("")
    if card_or_count_split[0] == "Счет":
        return f"{card_or_count_split[0]} {mask_bank_account(card_or_count_split[-1])}"
    else:
        return f'{" ".join(card_or_count_split[:-1])} {mask_credit_card(card_or_count_split[-1])}'


def converted_date(date: str) -> str:
    """
    Функция определяющая дату
    """
    date_split = date.split("T")[0].split("-")
    return f"{date_split[2]}.{date_split[1]}.{date_split[0]}"
