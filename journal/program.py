import journal

def main():
    run_event_loop()


def run_event_loop():
    print("What do you want to do with your journal?")
    journal_name = "Default"
    journal_data = journal.load(journal_name) # [] 
    cmd = 'EMPTY'

    while cmd != 'x' and cmd:

        cmd = input("[L]ist enries, [A]dd an entry, E[x]it: ")

        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data) 
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != "x" and cmd:
            print("Sorry we don't understand '{}'.".format(cmd))
    journal.save(journal_name, journal_data)


def list_entries(data):
    print("Your journal entries: ")
    entries = reversed(data)
    for index, entry in enumerate(entries):
        print('* [{}] {}'.format(index + 1, entry))


def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)
    #data.append(text)

if __name__ == '__main__':
    main()
