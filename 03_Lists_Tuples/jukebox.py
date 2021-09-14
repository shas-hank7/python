from jukebox_resources import albums

while True:
    print("Please choose your album(invalid choice exists). Enter 0 to exit!")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index+1, title))

    choice = int(input())
    if 1<=choice<=len(albums):
        songs_list = albums[choice - 1][3]
    elif choice == 0:
        break
    else:
        continue
    
    print("Please Choose a song")
    for index, (trackNumber, song) in enumerate(songs_list):
        print("{}: {}".format(index+1, song))
    choice = int(input())
    if 1<=choice<=len(songs_list):
        title = songs_list[choice-1][1]
    elif choice==0:
        break
    else:
        continue
    print("Playing: {}".format(title))
    print("=" * 40)
