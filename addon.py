import os
import xbmc

def playIt():	
	playlist = xbmc.PlayList( xbmc.PLAYLIST_VIDEO )
	playlist.clear()
	#playlist.add('plugin://plugin.video.youtube/play/?playlist_id=PLEZkO5Ag-uQqJN1VtzNojMt7pCzyHJxT2&order=shuffle')
	#playlist.add('plugin://plugin.video.youtube/play/?playlist_id=PL_8KXLhQVQMIQkRoOmytB6uKw_JZq7Ryv&order=shuffle')
	playlist.add('plugin://plugin.video.youtube/play/?playlist_id=PLLE0w4fS90JgX_-NsUxmJ6vA-58iwtjuo=shuffle')
	xbmc.Player().play(playlist)
	
try:
	playIt()

except Exception, e:
	playIt()
	exit(1)
