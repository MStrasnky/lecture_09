import json
import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as json_file:
        data = json.load(json_file)

    if field in set(data.keys()):
        return data[field]


def linear_search(search_sequence, number):
    positions = []
    count = 0

    for index, cislo in enumerate(search_sequence):
        if number == cislo:
            count += 1
            positions.append(index)
    slovnik = dict()
    slovnik["positions"] = positions
    slovnik["count"] = count


    return slovnik


def pattern_search(search_sequence, hledany_vzor):
    positions = []
    for index in range(len(search_sequence) - len(hledany_vzor)):
        if search_sequence[index:index + len(hledany_vzor)] == hledany_vzor:
            positions.append(index)
    return positions



def main():
    unordered_numbers = read_data("sequential.json", "unordered_numbers")
    print(unordered_numbers)
    search_output_dict = linear_search(unordered_numbers, 0)
    print(search_output_dict)
    print(pattern_search(read_data("sequential.json", "dna_sequence"), "ACG"))
if __name__ == '__main__':
    main()