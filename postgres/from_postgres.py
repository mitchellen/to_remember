# shows how to import a database into pandas
import pandas as pd
import psycopg2
host = "localhost" # name, IP or localhost
port = "5432" #default port
dbname = "cityhealthscrape"
user = "scrape"
pw = "password"
conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=pw)

df = pd.read_sql_query("SELECT * FROM rest_scores",con=conn) # can do a much better query, but this gets the whole thing
df.head()
