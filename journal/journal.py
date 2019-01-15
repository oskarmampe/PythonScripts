import os

def load(name):
    """
    This method loads up a file with entries
    :param name: the base name of the journal to load.
    :return: a new journal data structure populated with the file data
    """
    data = []
    filename = getFilePath(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data

def save(name, journal_data):
    print("Saving...")
    filename = getFilePath(name)

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')

    print("File saved to: {}".format(filename))

def add_entry(name, journal_data):
    journal_data.append(name)

def getFilePath(name):
    return os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))