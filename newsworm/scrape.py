import datetime
import requests
from lxml import etree

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

		#This could be an object, but I don't see the need until different
		#methods are needed to scrape a myriad of sources
		top_story_dict = {
			'title': top_story_item[0].text,
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
		link = content_item['link'],
		time_scraped = content_item['time_scraped']
	)

	db.session.add(content_insert)
	db.session.commit()

if __name__ == '__main__':
	save_to_database(scrape())

