# made this similiar to the one in 8.7 but fixed while loop to quit when 'q' is entered

# funcion with dictionary to describe albums and data in it
def make_album(artist=None, album=None, tracks=None, description=None):
    """Return a dictionary containing information about an album."""
    album_info = {
        'artist': artist,
        'album': album,
    }
    if tracks:
        album_info['tracks'] = tracks
    if description:
        album_info['description'] = description
    return album_info

def print_album_info(album_info):
    """Print the album information."""
    print(f"\nHere is the album information... \nArtist: {album_info['artist']} \nAlbum: {album_info['album']} \nTracks: {album_info.get('tracks', 'N/A')} \nDescription: {album_info.get('description', 'N/A')}")

def get_input(prompt):
    """Get input from the user and check for 'q' to quit."""
    response = input(prompt)
    if response.lower() == 'q':
        return None
    return response

# print example album
print("\nBelow you will find an example album:")
T_swift = make_album('Taylor Swift', '1989', 13, 'A pop album with a synth-pop sound.') 
print_album_info(T_swift)

# while loop to keep asking for input on album
while True:
    artist = get_input("\nWhat is a great album? Enter q at any time to quit the program. \nEnter the artist's name: ")
    if artist is None:
        break
    album = get_input("Enter the album name: ")
    if album is None:
        break
    tracks = get_input("Enter the number of tracks (or leave blank): ")
    if tracks is None:
        break
    description = get_input("Enter a description of the album (or leave blank): ")
    if description is None:
        break

    # Convert tracks to an integer if provided
    if tracks:
        try:
            tracks = int(tracks)
        except ValueError:
            print("Invalid number for tracks. Skipping track count.")
            tracks = None

    # Create the album dictionary
    album_info = make_album(artist, album, tracks, description)
    
    # Print the album information
    print_album_info(album_info)


