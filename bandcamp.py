#! python3 - Bandcampfun
# 
# This Downloader will look on bandcamp to find the artist and give the choice to download.
# The album or a song


# Import the module we need
import bs4, requests

# Variable 
research_url_string = "https://bandcamp.com/search?q="
confirm_choice = ["yes","ya","y"]


def list_album_in_artist_page(url_artist):
    set_of_url = set()
    
    res = requests.get(url_artist)
    element = bs4.BeautifulSoup(res.text, "html.parser")
    results = element.findAll("a", href=True)


    for element in results:
        print(len(element))
        if "album" in element["href"]:
            print(element)
        
    



print("\nWelcome to Bandcamp fun, which artist would you like to find on the website.\n")


while True:
    # TODO we should make something so we can decide between artist or album
    # user_search_query = input("Artist to look for: ")
    
    user_search_query = "loud larry adjust"
    
    url_for_the_search = research_url_string + user_search_query
    
    res = requests.get(url_for_the_search)

    artist = bs4.BeautifulSoup(res.text, "html.parser")

    search_results = artist.findAll("div", {"class":"result-info"})

    for result in search_results:
        
        # Find every other element div in the search result we founded
        res = result.select("div")

        # Find the lenght of the list of element
        info_lenght = len(res)

        # If we looking for an artist it will show the artist info
        if res[0].getText().strip() == "ARTIST":
            for element in res[:5]:
                print(element.getText().strip())

            # Clean the artist name so we can add it to the question string
            artist = str(res[1].getText()).strip()
            # The question string, with the artist name added
            question_string = "\n\nWould you like to go to %s page to find the albums(yes or no)?: " % (artist) 
            
            # If the user want to go the artist page we will give them all the infos
            if input(question_string) in confirm_choice:
                print(res[3].getText().strip())
                list_album_in_artist_page(res[3].getText().strip())
                



    user_decision = input("\nExit the program (yes/no) ?")
    if user_decision.lower() != "yes":
        break


