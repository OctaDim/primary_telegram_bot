from string import punctuation


def clean_text_punctuation(punctuated_text: str) -> str:
    """
    Remove all punctuation symbols from a string
    :param punctuated_text: str: Origin string to remove punctuation
    :return: str: Text without punctuation
    """
    translation_table = str.maketrans("", "", punctuation)
    cleaned_text = punctuated_text.translate(translation_table)
    return cleaned_text
