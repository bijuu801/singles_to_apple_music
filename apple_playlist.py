from applemusicpy import AppleMusic
import os


am = applemusicpy.AppleMusic(#secret_key, #key_id, #team_id)


def checkAM(row):

	row = row.split('-')
	
	artist_name = row[0].strip() 

	print(artist_name)
	
	song_title = row[1].strip()

	print(song_title)

    am_search_string = f"{artist_name} {song_title}"

	search_result = am.search(am_search_string, types=["songs"], limit = 1) 

	return search_result

singles_counter = 0;

playlist = am.create_playlist(
    name="Singles Playlist",
    description="A playlist created with AppleMusicPy",
    public=True
)

apple_artist_list_file = open('Music.txt', 'r')


song_row = apple_artist_list_file.readlines()

for row in song_row: 
	singles_counter += 1 
	is_song_found_in_AM = checkAM(row)

	if(is_song_found_in_AM):
		am.add_to_playist(playlist.id, row)
	else: 
		continue; 


	


