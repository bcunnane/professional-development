"""
CS3B Lab 2
Brandon Cunnane
This program opens files, validates their contents, and computes the sum if
validation passes.
"""


def get_filename():
    """
    Gets filename from the user
    """
    filename = input("Please enter the file name: ")
    return filename


def file_exists(filename):
    """
    Determines if the file exists (return True) or not (return False)
    """
    try:
        f = open(filename, 'r')
        return True
    except:
        print("Error: file not found.")
        return False


def read_file(filename):
    """
    Reads raw data from file with each line as list entry.
    """
    f = open(filename, 'r')
    raw = []
    for line in f:
        line = line.strip("\n")
        raw.append(line)
    f.close()
    return raw


def valid_content(raw):
    """
    Determines if file contents are valid based on assignment specification
    """
    try:
        for num in raw:
            int(num)
        if not (len(raw) - 1 == int(raw[0])):
            raise Exception
    except:
        print("Error: file contents invalid")
        return False
    else:
        return True


def get_data_sum(raw):
    """
    Computes the sum of all values in the data file
    """
    total = 0
    for num in raw[1:]:
        total = total + int(num)
    return total


def main():
    while True:
        filename = get_filename()
        if not file_exists(filename):
            continue
        raw = read_file(filename)
        if not valid_content(raw):
            continue
        total = get_data_sum(raw)
        print(f"The sum is: {total}")


if __name__ == '__main__':
    main()


"""
Please enter the file name: nofile.dat
Error: file not found.
Please enter the file name: bad1.dat
Error: file contents invalid
Please enter the file name: bad2.dat
Error: file contents invalid
Please enter the file name: bad3.dat
Error: file contents invalid
Please enter the file name: bad4.dat
Error: file contents invalid
Please enter the file name: good.dat
The sum is: 55
Please enter the file name: 
"""