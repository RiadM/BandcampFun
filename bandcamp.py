#! python3 - Bandcampfun
# 
# This Downloader will look on bandcamp to find the artist and give the choice to download.
# The album or a song


# Import the module we need
import bs4, requests
# Variable 
research_url_string = "https://bandcamp.com/search?q="

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

        res[0].getText().strip()

        if res[0].getText().strip() == "ARTIST":
            #print(test)
            print(result.select("div")[1].getText().strip())



    user_decision = input("\nExit the program (yes/no) ?")
    if user_decision.lower() != "yes":
        break

