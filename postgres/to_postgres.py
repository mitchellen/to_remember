#junk to keep track of postgres hoe-to
import psycopg2 



t_host = "localhost"# I am running DB locally
t_port = "5432" 
t_dbname = "cityhealthscrape"
t_user = "scrape"
t_pw = "password"
db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
db_conn.autocommit = True
db_cursor = db_conn.cursor()
if db_conn is not None:
    print('Connection established to PostgreSQL.')
else:
    print('Connection not established to PostgreSQL.')
    #normally this would be from a scrape in my scenario or another program
    name = 'Burger King'
    address = 'Somehwere,state'
    phone = '000000000'
    permit = 'FS'
    score = 100
    when = '2021-01-01'
    postgres_insert_query = "INSERT INTO rest_scores (name,address,phone,permit,score,date) VALUES (%s,%s,%s,%s,%s,%s);"
    record_to_insert = (name, address, phone, permit, score, when,) # note the trailing comma
    # Trap errors for opening the file
    try:
        db_cursor.execute(postgres_insert_query, record_to_insert)
    except psycopg2.Error as e:
        print(e)
