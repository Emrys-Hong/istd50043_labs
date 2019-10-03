# MongoDB

Few useful commands in the console:

* `show dbs`
* `use <db name>`
* `show collections`
* `db.createCollection(<collection name>)`
* `db.<collection name>.drop()`
* `db.drop()`

### Dumping a collection to files
`mongodump -d <dbname> -c <colname> -o <path>`

The output is a directory containing a `.bson` file and a `...metadata.json` file

### Loading the dumped files
`mongorestore -d <dbname> <path to .bson file>`

# MySQL and MongoDB data loading
For MySQL, use the bike-sharing dataset
* Unzip `bike-sharing.zip`
* Look at `setup.sql`, make sure you understand it
* Run `mysql -u root -b <dbname> < setup.sql`

For MongoDB, use the restaurant dataset
* Run `mongoimport -d <dbname> -c <collection_name> < restaurant.json`

Try out whatever queries you like. 

# Flask
A route represents a web service endpoint. Requests sent to the endpoint address are *routed* through Flask into the
defined method. 

## Define a route
Put `@app.route <path>` before a method that implement that route's logic

The body of the request is available in `request` variable inside the method. 

* `request.json` returns the json content

The result is a JSON object, or simply a dictionary of string. 

## Query the service

* Using browser's URI: can carry data, but in form of flat key-value store
  * Example: localhost/query?key1=val1&key2=val2...
  
  Recommended use: when the endpoint takes no (or very simple) parameter

* Using `curl`:
  * Simple GET request: `curl -i <endpoint>`
    This works like browser's URI. The `-i` flags tells it to print header

  * Requests with JSON content:
      `curl -i -X GET/POST -H "Content-Type: application/json" -d '{<request content>}' <endpoint>` 

* Using Python `requests` package:
  * Look at `fabfile.py` to see how to send requests and retreive responses
  * Change `ADDR` to the **public IP address** of the server running Flask
  * Try out some test, using `fab <method name>`
  

# Database execution from Python
* Look at and `db_demo.py`. Make sure you understand what they do, and how to invoke them. 

* Test using the public IP address of the database server. 
