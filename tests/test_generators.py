from src.generators import card_number_generator, filter_by_currency, transaction_descriptions, transactions

usd_transaction = filter_by_currency(transactions, "USD")
description = transaction_descriptions(transactions)
card = card_number_generator(1, 5)


def test_filter_by_currency() -> None:
    assert next(usd_transaction) == "939719570"
    assert next(usd_transaction) == "142264268"
    assert next(usd_transaction) == "895315941"
    """
    Фильтрация операций по валюте.
    """


def test_card_number_generator() -> None:
    assert next(card) == "0000000000000001"
    assert next(card) == "0000000000000002"
    assert next(card) == "0000000000000003"
    assert next(card) == "0000000000000004"
    assert next(card) == "0000000000000005"
    """
    Генерация номеров банковских карт.
    """


def test_transactions_for_test() -> None:
    assert next(description) == "Перевод организации"
    assert next(description) == "Перевод со счета на счет"
    assert next(description) == "Перевод со счета на счет"
    assert next(description) == "Перевод с карты на карту"
    assert next(description) == "Перевод организации"
    """
    Генерацию описаний операций.
    """
