import psycopg2

conn = psycopg2.connect("dbname=postgres user=postgres password=18082004Ab")
cur = conn.cursor()
cur.execute("SELECT * FROM ggwp")
print(cur.fetchall())

# 1
def print_all_pattern():
    conn = psycopg2.connect("dbname=postgres user=postgres password=18082004Ab")
    cur = conn.cursor()
    cur.execute("SELECT * FROM ggwp")
    for data in cur.fetchall():
        name, surname, number = data
        print(f'Name: {name} || Surname: {surname} || Number: {number}')
    conn.commit()
    conn.close()

# 2
# name = input()
# surname = input()
# number = int(input())
def check_user(name, surname, number):
    conn = psycopg2.connect("dbname=postgres user=postgres password=18082004Ab")
    cur = conn.cursor()
    cur.execute("SELECT * FROM ggwp")
    
    if cur.fetchone() is None:   
        cur.execute("insert into public.ggwp(name, surname, phone_number) values('%s', '%s', '%s')" % (name, surname, number)) 
    else:
        cur.execute("Update ggwp set phone_number=%s where name=%s", (number, name))
    conn.commit()
    conn.close()

# 3
arr = [
    ['name1', 'surname1', 87783772991],
    ['name2', 'surname2', 87783777991],
    ['name3', 'surname3', 87753772991],
    ['name4', 'surname4', 87783872991],
    ['name5', 'surname5', 87783772771]
]
def insert_list(arr):
    conn = psycopg2.connect("dbname=postgres user=postgres password=18082004Ab")
    cur = conn.cursor()
    for data in arr:
        cur.execute("insert into public.ggwp(name, surname, phone_number) values(%s, %s, %s)", (data))
    conn.commit()
    conn.close()

# 4
n = int(input())
def limit():
    conn = psycopg2.connect("dbname=postgres user=postgres password=18082004Ab")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM ggwp limit {n}")
    print(cur.fetchall())

def offset():
    conn = psycopg2.connect("dbname=postgres user=postgres password=18082004Ab")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM ggwp offset {n}")
    print(cur.fetchall())

# 5
def delete_user(name):
    conn = psycopg2.connect("dbname=postgres user=postgres password=18082004Ab")
    cur = conn.cursor()
    cur.execute("delete from ggwp where name='%s'" % name)
    conn.commit()
    conn.close()