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
    print(f"Artist: {album_info['artist']} \nAlbum: {album_info['album']} \nTracks: {album_info.get('tracks', 'N/A')} \nDescription: {album_info.get('description', 'N/A')}")

T_swift = make_album('Taylor Swift', '1989', 13, 'A pop album with a synth-pop sound.') 
print_album_info(T_swift)

