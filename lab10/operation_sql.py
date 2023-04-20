import psycopg2
import csv

conn = psycopg2.connect("dbname=postgres user=postgres password=18082004Ab")
cur = conn.cursor()
cur.execute("SELECT * FROM ggwp")
record = cur.fetchall()
print(record)


# delete function
def del_db(user_name):
    conn = psycopg2.connect("dbname=postgres user=postgres password=18082004Ab")
    cur = conn.cursor()
    cur.execute("delete from ggwp where name='%s'" % user_name)
    conn.commit()
    conn.close()

# update function
def update_name(name):
    conn = psycopg2.connect("dbname=postgres user=postgres password=18082004Ab")
    cur = conn.cursor()
    cur.execute("Update ggwp set name='Bakdaulet' where name='%s'" % name)
    conn.commit()
    conn.close()

# add from console
# name = input()
# surname = input()
def add_db(name, surname):
    conn = psycopg2.connect("dbname=postgres user=postgres password=18082004Ab")
    cur = conn.cursor()
    cur.execute("insert into public.ggwp(name, surname) values('%s', '%s')" % (name, surname))
    conn.commit()
    conn.close()


# add from csv file
def import_csv():
    with open('data.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(
            ('user_name', 'user_surname')
        )


    users_data = [
        ['name1', 'surname1'],
        ['name2', 'surname2'],
        ['name3', 'surname3'],
        ['name4', 'surname4'],
        ['name5', 'surname5'],
    ]
    for user in users_data:
        with open('data.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(
                user
            )

    conn = psycopg2.connect("dbname=postgres user=postgres password=18082004Ab")
    cur = conn.cursor()
    cur.execute("Copy ggwp(name, surname, phone_number) from '%s' delimiters ',' csv header;" % r'C:\Users\user\PycharmProjects\week 3\week 3\PP2_Python_study\lab10\data.csv')
    conn.commit()
    conn.close()

# queries data from the tables
def que():
    conn = psycopg2.connect("dbname=postgres user=postgres password=18082004Ab")
    cur = conn.cursor()
    cur.execute("SELECT * FROM ggwp")
    for data in cur.fetchall():
        name, surname = data
        print(f'User name is: {name} and User surname is: {surname}')
    conn.commit()
    conn.close()