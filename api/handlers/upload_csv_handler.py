import csv

from models.benfords_law_tracker import BenfordsLawTracker

COLUMN_TO_CHECK = '7_2009'
TAB_DELIMITER = "\t"
COMMA_DELIMITER = ","

def delimiter_present(uploaded_delimited_file, delimiter):
    delimiters_present = 0
    index = 0

    while index <= 10:
        possible_columns = len(uploaded_delimited_file[index].split(delimiter))

        if delimiters_present == 0 and possible_columns > 1:
            delimiters_present = possible_columns

        if delimiters_present != possible_columns:
            return False

        index +=1

    return True

def select_delimiter(uploaded_delimited_file):
    if delimiter_present(uploaded_delimited_file, COMMA_DELIMITER):
        return COMMA_DELIMITER

    if delimiter_present(uploaded_delimited_file, TAB_DELIMITER):
        return TAB_DELIMITER

    return

def get_counts(uploaded_file):
    uploaded_delimited_file = uploaded_file.read().decode().splitlines()
    percentage_tracker = BenfordsLawTracker()
    reader = csv.DictReader(uploaded_delimited_file,
                            delimiter=select_delimiter(uploaded_delimited_file),
                            skipinitialspace=True)
    for row in reader:
        percentage_tracker.increase_row_count()
        if row[COLUMN_TO_CHECK]:
            first_digit = int(row[COLUMN_TO_CHECK][0])
            percentage_tracker.increase_digit_counter(first_digit)


    return percentage_tracker.counters
