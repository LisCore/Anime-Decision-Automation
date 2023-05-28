import time
import sys
from random import choice
from testing_api import ANIME



# This program allows the user to input which animes they wish to watch on
# a txt file. Then they can choose certain options. THe main goal is to help
# the user come to a decision for an anime they will watch. Perhaps can change over
# to more broad analysis

# Added jikanpy api to aid with having a database that can give titles and description of the anime
# implementation coming soon


def gather_info(data):
    anime_data_list = data['data']
    anime_info = []
    for anime_data in anime_data_list:
        anime_title = anime_data['title']
        anime_episodes = anime_data['episodes']
        anime_popularity = anime_data['popularity']
        anime_duration = anime_data['duration']
        anime_dict = {'title': anime_title, 'episodes': anime_episodes,
                      'popularity': anime_popularity, 'duration': anime_duration}
        anime_info.append(anime_dict)
    return anime_info


'''
# get info about anime
def get_api(anime_info):
    api_load = 'https://api.jikan.moe/v4/anime/{id}/moreinfo'
    query_params = {
        'moreinfo': anime_info
    }

    response = requests.get(
        api_load
        )

    if response.status_code == 200:
        data = response.json()
        with open('../response.json', 'w') as fileManager:
            fileManager.write(json.dumps(response.json(), indent=4))
        return data

    return response.status_code
'''


def pick_random():
    open_file = open("anime.txt", "r")
    if open_file.readable():
        file = choice(open_file.readlines())
        print(file.replace(',', ""))


def layout_anime():
    open_file = open("anime.txt", "r")
    if open_file.readable():
        for file in open_file.readlines():
            file = file.replace(',', "")
            print(file)
            time.sleep(.25)

    else:
        print("Error, no file read")
    print("\n\n")
    open_file.close()


def remove_from_list():
    with open("anime.txt", "r") as file:
        lines = file.readlines()
    anime_to_remove = input("Enter anime you wish to remove: ")
    modify = [line.replace(str(anime_to_remove) + ",", '').strip() for line in lines if line.strip()
              and line.strip() != str(anime_to_remove)]
    # list comprehension
    with open("anime.txt", "w") as file:
        file.write("\n".join(line for line in modify if line))


def add_new_anime():
    write_file = open("anime.txt", "a")
    new_title = input("Please enter new anime title: ")
    flag = is_copy(new_title)
    if flag == 1:
        write_file.write("\n" + str(new_title) + ",")
    write_file.close()


def is_copy(new_title):
    with open("anime.txt", "r") as file:
        file.seek(0)
        for line in file.readlines():
            if line.replace(",", "").strip() == new_title:
                print("Error, name already on list: " + str(new_title))
                return 0
    return 1


def main_application():
    print("Please choose option: ")
    print("A) Layout Anime List\nB) Add New Anime\nC) Anime Decision\nD) Remove from List\nE) Anime Info\nF) "
          "Close Program\n")
    ans = input(">> ")
    ans = ans.lower()
    while (ans != 'a' and
           ans != 'b' and
           ans != 'c' and
           ans != 'd' and
           ans != 'e' and
           ans != 'f'):
        print("Error, try again\n\n")
        print("A) Layout Anime List\nB) Add New Anime\nC) Anime Decision\nD) Remove from List\nE) Anime Info\nF) "
              "Close Program\n")
        ans = input(">> ")
    return ans


def main():
    while True:
        user_input = main_application()
        if user_input == 'a':
            layout_anime()

        if user_input == 'b':
            add_new_anime()

        if user_input == 'c':
            pick_random()

        if user_input == 'd':
            remove_from_list()

        if user_input == 'e':
            anime = ANIME()
            anime_title = input("Enter Title for anime: ")
            anime_info = gather_info(anime.get_info(anime_title))
            for anime_data in anime_info:
                print("Title      -\t", anime_data['title'])
                print("Episodes   -\t", anime_data['episodes'])
                print("Popularity -\t", anime_data['popularity'])
                print("Duration   -\t", anime_data['duration'])
                print("\n\n")

        if user_input == 'f':
            sys.exit()


if __name__ == "__main__":
    main()
