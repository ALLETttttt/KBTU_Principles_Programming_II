import psycopg2

 
def create_table():
    command = """
        CREATE TABLE Snake (
            username VARCHAR (20) UNIQUE NOT NULL,
            score VARCHAR (20) UNIQUE NOT NULL,
            level VARCHAR (20) UNIQUE NOT NULL,
            started_time VARCHAR (17) UNIQUE NOT NULL,
            ended_time VARCHAR (17) UNIQUE NOT NULL
        );
    """
    conn = None
    try:
        conn = psycopg2.connect("dbname=postgres user=postgres password=18082004Ab")
        cur = conn.cursor()
        cur.execute(command)
        cur.close()
        conn.commit()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
            
create_table()
