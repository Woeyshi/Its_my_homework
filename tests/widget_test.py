from datetime import datetime


def convert_date(input_date: str) -> str:
    """
    Converts the input date string to the required format.

    Args:
        input_date (str): The input date string in the format '%Y-%m-%dT%H:%M:%S.%f'.

    Returns:
        str: The converted date string in the format '%d.%m.%Y'.
    """
    date_obj = datetime.strptime(input_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")


print(convert_date("2018-07-11T02:26:18.671407"))
