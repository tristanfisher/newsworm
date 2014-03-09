from newsworm import app
from newsworm.models import Content
from flask import render_template
debug = True

@app.route('/')
@app.route('/index')
def index():
	'''
	start an instance of our content view
	'''

	test_content = [
		{'link': 'http://news.google.com/news/url?sa=t&fd=R&usg=AFQjCNGKVf_OUF_ctYpsc4c2RJjLLDf_lw&cid=c3a7d30bb8a4878e06b80cf16b898331&url=http://stream.wsj.com/story/latest-headlines/SS-2-63399/SS-2-476213/', 'time_scraped': '2014-03-09 17:40:50', 'title': 'Stolen Passports on Malaysia Airlines Flight Raise Security Concerns - Wall Street Journal'},
		{'link': 'http://github.com/tristanfisher/newsworm', 'time_scraped': '2014-03-09 17:40:50', 'title': 'newsworm stub data added'}
	]

	content = Content.query.all()

	return render_template(
		'index.html',
		title = 'Top Stories',
		content = content
	)

app.run(debug=debug)