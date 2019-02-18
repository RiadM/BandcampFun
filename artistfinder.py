#! python3 - Find artist album
#


# Import the module we need
import bs4, requests

# Variable 
research_url_string = "https://gullywood.bandcamp.com"

confirm_choice = ["yes","ya","y"]


def list_album_in_artist_page(url_artist):
    # A dictionary containing all the album from this artist
    albums_name_available = ["All the album"]
    albums_url = []
    
    res = requests.get(url_artist)
    element = bs4.BeautifulSoup(res.text, "html.parser")
    results = element.findAll("a", href=True)

    # Iterate to find only the one that have a ref to an album
    for element in results:
        if "album" in element["href"] and "help" not in element["href"]:
            albums_name_available.append(element.find("p").getText().strip())
            albums_url.append(element["href"])
    
    # Ask the user what album they would like to download
    user_response = ""
    
    # Loop that will only accept choice from the list
    while user_response != len(albums_name_available):
        print("Which album would you like to download?")
        
        # Print the list with the available choice
        for index in range(0,len(albums_name_available)):
            print(str(index) + "- %s" % (albums_name_available[index]))
        print(str(len(albums_name_available)) +"- Exit")  
    
        # Ask the user for what they want
        user_response = input("Write the number of the selection: ")
        
        # Verify if the user input is only decimal 
        if user_response.isdecimal():

            # Find what the user want
            if int(user_response) in range(0, len(albums_name_available)):
                print(user_response)
            elif int(user_response) == len(albums_name_available) :
                print("No album will be downloaded.\n")
                break
        else:
            print("\nPlease make a choice in the list using the numbers for selection.\n")
        

list_album_in_artist_page(research_url_string)