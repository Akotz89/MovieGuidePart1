# Aaron Kotz, CIS261, Movie Guide Part 1

def display_heading():
    print("The Movie List program\n")

def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit program\n")

def prepopulate_movies():
    return ["Doctor Zhivago", "Brief Encounter", "The Bridge on the River Kwai"]

def display_movies(movies):
    print()
    for index, movie in enumerate(movies, start=1):
        print(f"{index}. {movie}")

def add_movie(movies):
    movie_title = input("Name: ")
    movies.append(movie_title)
    print(f"{movie_title} was added.\n")

def delete_movie(movies):
    try:
        movie_number = int(input("Number: "))
        if 1 <= movie_number <= len(movies):
            removed_movie = movies.pop(movie_number - 1)
            print(f"{removed_movie} was deleted.\n")
        else:
            print("Invalid movie number.\n")
    except ValueError:
        print("Invalid movie number.\n")

def main():
    movies = prepopulate_movies()
    display_heading()
    while True:
        display_menu()
        command = input("Command: ").lower()
        if command == 'list':
            display_movies(movies)
        elif command == 'add':
            add_movie(movies)
        elif command == 'del':
            delete_movie(movies)
        elif command == 'exit':
            print("Bye!\n")
            break
        else:
            print("Not a valid command. Please try again.\n")

if __name__ == "__main__":
    main()

