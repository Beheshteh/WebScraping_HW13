from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.mars_mission

@app.route("/")
def index():
    listings = db.listings.find_one()
    #print("listing: %s" % listings)
    return render_template("index.html", listings=listings)
        
    
@app.route("/scrape")
def scrape():
    
    listings_data = scrape_mars.scrape()
    listings = db.listings
    listings.update({}, listings_data, upsert=True)
    return redirect("http://localhost:5002/", code=302)
    

if __name__ == "__main__":
    app.run(debug=True, port=5002)
    
