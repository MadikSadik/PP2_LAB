import psycopg2
import csv

conn = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='Madikosh4268'
)

cur = conn.cursor() 

def create_table():
    cur.execute( 
        '''
    create table if not exists phone_book(
        id serial primary key,
        name varchar(25),
        phone varchar(20)
    );
    '''
    )
    conn.commit()


def insert_from_csv(csv_file):
    with open(csv_file, 'r') as file:
        data = csv.DictReader(file)
        print(data)
        for row in data:
            print(row['name'], row['phone'])
            cur.execute(f"insert into phone_book (name, phone) values('{row['first_name']}', '{row['phone']}')")
    conn.commit()

def insert_manually():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    cur.execute(f"insert into phone_book (name, phone) values('{name}', '{phone}')")
    conn.commit()


def update_data(old_value, new_name=None, new_phone=None):
    if new_name:
        cur.execute(f"update phone_book set name = '{new_name}' where name = '{old_value}'")
    if new_phone:
        cur.execute(f"update phone_book set phone = '{new_phone}' where phone = '{old_value}'")
    conn.commit()


def query_data(name=None, phone=None):
    if name and phone:
        cur.execute(f"select * from phone_book where name = '{name}' and phone = '{phone}'")
    elif name:
        cur.execute(f"select * from phone_book where name = '{name}'")
    elif phone:
        cur.execute(f"select * from phone_book where phone = '{phone}'")
    else:
        cur.execute("select * from phone_book")
    rows = cur.fetchall()
    for row in rows:
        print(row)


def delete_data(name = None, phone=None):
    if name:
        cur.execute(f"delete from phone_book where name = '{name}'")
    if phone:
        cur.execute(f"delete from phone_book where phone = '{phone}'")


create_table() 

insert_manually()
update_data('Jonh', new_name='Jonathan')
query_data(name='Jonathan')
delete_data(phone='3456')
#insert_from_csv('/Users/madiyarbekmutat/Desktop/kbtu_pp/pp2_lab/Lab10/exampel.csv')