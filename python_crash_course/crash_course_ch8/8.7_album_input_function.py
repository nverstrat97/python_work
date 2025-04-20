# made this similiar to the one in 8.6 but added a while loop to keep asking for input and added a function to make it easier to add new albums

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
print("Below you will find an example album:")
T_swift = make_album('Taylor Swift', '1989', 13, 'A pop album with a synth-pop sound.') 
print_album_info(T_swift)

# while loop to keep asking for input on album
input_album = True
while input_album:
    artist = get_input("\nWhat is a great album? Enter q at any time to quit the program. \nEnter the artist's name: ")
    album = get_input("Enter the album name: ")
    tracks = get_input("Enter the number of tracks (or leave blank): ")
    description = get_input("Enter a description of the album (or leave blank): ")

    # Convert tracks to an integer if provided
    if tracks:
        tracks = int(tracks)

    # Create the album dictionary
    album_info = make_album(artist, album, tracks, description)
    
    # Print the album information
    print_album_info(album_info)


