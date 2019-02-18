#! python3 - album downloader


# Import the module we need

def downloader(url):
    import os, re, requests

    text = requests.get(url).text

    # Regex that find the mp3 download link in the html
    regex_mp3_link = re.compile('{"mp3-128":"(.*?)"}')
    # Regex that find the title of the songs
    regex_title = re.compile('"title":"(.*?)",')
    
    # Find the titles and put them in a list. Index 0 = name album and last index is just CD
    titles = re.findall(regex_title, text)    
    # Link of the songs
    mp3_link = re.findall(regex_mp3_link, text)

    print(titles)
    # To verify if the album is already downloaded
    # TODO we should add something to ask the user if they want to download missing songs
    if os.getcwd() == titles[0]:
        print("Download could not be done")
    else:
        # Create a directory for the album
        os.makedirs(titles[0])
        # Go to the album directory
        os.chdir(titles[0])

        os.system('cls||clear')
        # Will download the file one by one
        for index in range(0,len(mp3_link)):
            
            track_number = index + 1
            track_title = titles[track_number].capitalize()
            track_url = mp3_link[index]

            print("downloading %s track %d of %d" % (track_title, track_number, len(mp3_link)))
            
            # Request the url for DL and if it fail raise a status
            mp3_object = requests.get(track_url)
            mp3_object.raise_for_status

            # Set the title for the file
            title_mp3 = "%d - %s.mp3" % (track_number, track_title)       
            mp3_file = open(title_mp3, 'wb')
            
            # Download the song and save them
            for chunk in mp3_object.iter_content(10000):
                mp3_file.write(chunk)
            # Close the file after it's completed
            mp3_file.close()

        os.system('cls||clear')
        return "%s was downloaded\n" % (titles[0])