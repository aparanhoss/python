#System module
import queue
import threading
import time

#Local Moduler
import feedparser

#Set up some global variables
num_fetch_threads=2
enclosure_queue=queue.Queue()

#a real app wouldnt use hard-coded data...
feed_urls=['http://www.castsampler.com/cast/feed/rss/guest','http://kickassto.co/blog/?rss=1']

def downloadEnclosures(i,q):
	"""This is the worker thread function.
	It proccesses items in the queue one after another. These daemon threads go into an infiniti  Loop,and only exit when the main thread ends.
	"""
	while True:
		print("%s: Looking for the next enclosure"%i)
		url=q.get()
		print("%s: Downloading: "%i,url)
		#intead of really download the url, we just pretend and sleep
		time.sleep(i+2)
		q.task_done()

#Set up some  threads to fetch the enclosures
for i in range(num_fetch_threads):
	worker=threading.Thread(target=downloadEnclosures,args=(i,enclosure_queue,))
	worker.setDaemon(True)
	worker.start()

#Download the feed and put de enclosure URLs into the queue
for url in feed_urls:
	response  =feedparser.parse(url,agent='fetch_podcasts.py')
	for entry in response['entries']:
		for enclosure in entry.get('enclosures',[]):
			print("Queuing: ",enclosure['url'])
			enclosure_queue.put(enclosure['url'])
			
#Now wait for the queue to be empty, indicatiting tha we have processed all of the downloads.
print("Main thread waiting")
enclosure_queue.join()
print("Done***")