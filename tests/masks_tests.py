from src.masks import mask_credit_card, mask_bank_account

card_number = "7000792289606361"
masked_card = mask_credit_card(card_number)
print(masked_card)

account_number = "73654108430135874305"
masked_account = mask_bank_account(account_number)
print(masked_account)
