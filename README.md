# Mission to Mars

In this project, I am building a web application that scrapes various websites for data related to the Mission to Mars and displays 
the information in a single HTML page. 

  Latest news: Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragragh Text. 
  Featured Image : JPL's Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
  Mars Weather : Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scrape the latest Mars weather tweet from the page. 
  Mars Facts : Mars Facts webpage [here](http://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
  Mars Hemisperes : The USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)
                    to obtain high resolution images for each of Mar's hemispheres.



I Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
I also Used splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.
I Used Pymongo for CRUD applications for my database. 
Also used Bootstrap to structure my HTML template.