import movie
import requests.exceptions

def main():
    print_header()
    search_event_loop()

def print_header():
    print("------------------")
    print("---MOVIE APP---")
    print("------------------")

def search_event_loop():
    search = "ONCE_THROUGH_LOOP"
    while search != 'x':
        try:
            search = input('Movie search text (x to exit):  ')
            if search != 'x':
                results = movie.find_movies(search)
                print("Found {} results.".format(len(results)))
                for r in results:
                    print("{} -- {}".format(r.year, r.title))
                print()
        except requests.exceptions.ConnectionError:
            print("Error: Could not connect to the internet")
        except ValueError:
            print("Cannot search for empty")
        except Exception as x:
            print("Unexpected error. Details: {}".format(x))
    print('Exiting...')

if __name__  == '__main__':
    main()