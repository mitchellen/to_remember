#create the database in postgres using psql and create a user with perms then do something similar. I have seen an if statement that does this if not created.
import psycopg2

host = "localhost" 
port = "5432" 
dbname = "cityhealthscrape"
user = "scrape"
pw = "password"
conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=pw)
conn.autocommit = True # this gets from having to commit after every action, prob a newb move
cursor = conn.cursor()
sqlCreateTable = "create table rest_scores (name varchar(128),address text, phone varchar(128),permit varchar(128), score NUMERIC,date date NOT NULL);"
cursor.execute(sqlCreateTable)
#
