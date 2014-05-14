import datetime
import requests
from lxml import etree
from BeautifulSoup import BeautifulSoup
from config import DEBUG

def scrape():
	'''
	retrieve the headline and link url of the current top story on google news
	'''
	#using RSS so we're thriftier and don't need to parse html
	content_url = 'http://news.google.com/news/url?output=rss'
	content = requests.get(content_url)

	#expecting xml response.  json and html scraping options would be a todo.
	if 'application/xml' in content.headers['content-type']:
		content_xml = etree.fromstring(content.text)

		'''
		Structure of response looks like:
		<rss>
			<channel>		<---- element[0]
			<item>			<---- Top Story
				<title>		<---- [0]
				<link>		<---- [1]
				<guid>
				<category>
				<pubDate>
				<description>
		'''

		top_story_item = content_xml[0].find('item')
		top_story_item = top_story_item.getchildren()
		top_story_image = BeautifulSoup(top_story_item[-1].text).find('img')
		#grab the first attribute, then the value for the img tag
		#(u'src', u'//t2.gstatic.com/images?q=tbn:ANd9GcRbKgR....)
		top_story_image =  top_story_image.attrs[0][1]

		#if image starts with //, prefix it with http
		if top_story_image.startswith('//'):
			top_story_image = 'http:' + top_story_image

		#This could be an object, but I don't see the need until different
		#methods are needed to scrape a myriad of sources
		top_story_dict = {
			'title': top_story_item[0].text,
			'repeat_count' : None,
            'image': top_story_image,
			'link': top_story_item[1].text,
			'time_scraped': datetime.datetime.now()
		}

		return top_story_dict

def save_to_database(content_item):
	'''
	save a title, link, and timestamp to a database
	'''
	from config import db
	from models import Content

	content_insert = Content(
		title = content_item['title'],
		repeat_count = content_item['repeat_count'],
		image = content_item['image'],
		link = content_item['link'],
		time_scraped = content_item['time_scraped']
	)

	_db_session = db.session

	last_insert = _db_session.execute("select max(id), title, repeat_count from Content").first()
	last_insert_id = last_insert.values()[0]
	last_insert_title = last_insert.values()[1]
	last_insert_repeat_count = last_insert.values()[2]

	#_db_session.query(Content).filter_by(id=last_insert_id).update({"title": last_insert_title + "[repeat]"})
	#_db_session.commit()

	if last_insert_title == content_insert.title:
		if last_insert_repeat_count is None: last_insert_repeat_count = 0
		content_insert.repeat_count  = int(last_insert_repeat_count + 1)
		_db_session.query(Content).filter_by(id=last_insert_id).update({"repeat_count": content_insert.repeat_count})
		if DEBUG: print "Content was the same from last run, not storing content again."
	else:
		_db_session.add(content_insert)

	try:
		_db_session.commit()
	except:
		_db_session.rollback()
		raise
	finally:
		_db_session.close()

if __name__ == '__main__':
	save_to_database(scrape())