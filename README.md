##newsworm
---

Grab the top headline off of Google News and save it to a database for future consumption.


#####To get started:
1. `git` clone this repo.
2. install the requirements using `pip`
3. edit the database dictionary in server.py with your credentials and host
4. run `scrape.py` at least once to put some content in the DB
5. open a webbrowser and look to port 5000 (default) 


#####Scripts:

- scrape.py
 
Scrapes HTML and saves top story text and href to a database.

- server.py 
 
Runs a simple Flask application that renders the content saved by `scrape.py` in a Jinja2 template.


######TODO:
 - Add error handling (e.g. check response code for http get)

 - Getting the top story currently requests the whole page/tree.  This is not necessary and is wasteful (could make a request for N-bytes)

 - Support other news/link sources.

 - Store content in GMT. Leave it to the view to decide the timezone