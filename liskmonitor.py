#!/usr/bin/python
import os
import requests
import time

NODES = ["explorer.liskwallet.net:8000", "01.lskwallet.space:8000", "login.lisk.io:8000", "lisk.fastwallet.online:8000"]
NODE = "46.16.190.190:8000"
DELEGATE = "dakk"
DELEGATE_ADDRESS = "2324852447570841050L"

stats = None

def notify (title, message, i = None):
	print str (i) + title + message
	
	if i != None:
		os.system ('termux-notification -t "'+title+'" -c "'+message+'" -i '+str (i))
	else:
		os.system ('termux-notification -t "'+title+'" -c "'+message+'"')
	

while True:
	# Sync status
	heights = {}
	
	for n in NODES:
		try:
			r = requests.get ('http://' + n + '/api/blocks?limit=100&orderBy=height:desc')
			d = r.json ()
		
			height = d['blocks'][0]['height']
			if str (height) in heights:
				heights[str(height)] += 1
			else:
				heights[str(height)] = 1
		except:
			pass
	
	r = requests.get ('http://' + NODE + '/api/blocks?limit=100&orderBy=height:desc')
	d = r.json ()	
	height = d['blocks'][0]['height']
	
	best = 0
	besth = 0
	for x in heights:
		if heights[x] > best:
			best = heights[x]
			besth = x
			
	if str (besth) != str (height):
		notify ('Lisk node is not in sync', 'Height: ' + str (height) + ' (best height is ' + str (besth) + ' shared by ' + str (best) + ' nodes)')
	
	# Mined missed blocks
	r = requests.get ('http://' + NODE + '/api/delegates/?limit=101&offset=0&orderBy=rate:asc')
	d = r.json ()
	
	row = None
	
	for x in d['delegates']:
		if x['username'] == DELEGATE:
			row = x
			
	if stats == None:
		stats = row
	else:
		if row['producedblocks'] != stats['producedblocks']:
			notify ('Mined block', 'Mined a new block')
		elif row['missedblocks'] != stats['missedblocks']:
			notify ('Missed block', 'Missed a block, take care!')
		
		stats = row	
		
	notify ('Lisk Delegate Stats', 'Mined: ' + str (stats['producedblocks']) + '\nMissed: ' + str (stats['missedblocks']) + '\nHeight: ' + str (height) + ' (best height is ' + str (besth) + ' shared by ' + str (best) + ' nodes)' , 'delegatestats')
	
	time.sleep (5)
