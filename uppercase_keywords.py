import sys


def keyword_combos(keyword):
    """

    :param keyword: str
    :return: list of strings, combinations in which the keyword can appear in an sql file
             i.e.: '(select ', ' avg(' ...
    """
    start_possibilities = ['\n', ' ', '(']
    end_possibilities = ['\n', ' ', '(', ')']
    combos = []
    for start in start_possibilities:
        for end in end_possibilities:
            combos.append(start + keyword + end)
    return combos


def file_start_combos(keyword):
    """

    :param keyword: str
    :return: list of strings, combinations in which the keyword can appear at the beginning of an sql file
             i.e.: 'with\n', 'select ' ...
    """
    end_possibilities = ['\n', ' ', '(', ')']
    combos = []
    for end in end_possibilities:
        combos.append(keyword + end)
    return combos


def uppercase_keywords(text):
    """
    A file named 'keywords.txt' should be placed in the same directory as this .py file. The file should contain a list
    of the keywords--lowercase, separated by commas--to search for in the text.

    :param text: str, the body of an SQL query, typically the contents of a .sql file
    :return: str, SQL code with keywords upper-cased
    """
    # read keywords from file into a list
    with open('keywords.txt') as f:
        keywords = f.read().split(',')

    # if text starts with keyword, uppercase it
    for keyword in keywords:
        start_combos = file_start_combos(keyword)
        for combo in start_combos:
            if text.startswith(combo):
                text = combo.upper() + text[len(combo):]
                break

    # uppercase all other keywords in text
    for keyword in keywords:
        combos = keyword_combos(keyword)
        for combo in combos:
            if combo in text:
                text = text.replace(combo, combo.upper())
    return text


if __name__ == '__main__':
    file_name = sys.argv[1]
    with open(file_name) as input_file:
        content = input_file.read()
    # Create new .sql file in original directory with keywords upper-cased: name_UPPER.sql
    with open(file_name.split('.')[0] + '_UPPER.sql', 'w') as output_file:
        output_file.write(uppercase_keywords(content))
