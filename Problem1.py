"""
Alexander Urbanyak
CS4720(01)
Created: 01-25-2019
Python 3.6
"""
# The program reads a text file "in.txt", converts all letters to uppercase,
# and writes all contents of the read file to "out.txt"
# reads and writes multiple lines
# "out.txt" will be created if it doesn't exist,
# otherwise all its contents will be erased and re-written
# numbers and special characters are unaffected


def read_file(file_name):
    assert file_name is not None
    file = open(file_name, "r")
    result = file.readlines()
    file.close()
    return result


def to_upper_case(lines):
    for line in lines:
        lines[lines.index(line)] = line.upper()


# assumes something must be written to a file
def write_file(file_name, lines):
    assert file_name is not None
    if len(lines) < 1:
        raise ValueError("No text is provided to write to " + file_name)

    file = open(file_name, "w")
    file.writelines(lines)
    file.close()


if __name__ == '__main__':

    input_file = "in.txt"
    output_file = "out.txt"

    # read file
    content = read_file(input_file)

    # convert all characters to upper case
    to_upper_case(content)

    # write to a file
    write_file(output_file, content)
