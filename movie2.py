import sqlite3
import csv

conn=sqlite3.connect("Moviedb.sqlite")
cur=conn.cursor()


try:
    cur.execute('''CREATE TABLE Movies (Name text,Actor text,Actress text,Director text,Year int)''')
    cur.execute('''Insert into Movies(Name,Actor,Actress,Director,Year)values("Interstellar","Matthew McConaughey","Anne Hathaway","Christopher Nolan",2014)''')
    cur.execute('''Insert into Movies(Name,Actor,Actress,Director,Year)values("Gravity","George Clooney","Sandra","Alfonso Cuarón",2013)''')
    cur.execute('''Insert into Movies(Name,Actor,Actress,Director,Year)values("Furious 7","Vin Diesel","Michelle Rodriguez","James Wan",2015)''')
    cur.execute('''Insert into Movies(Name,Actor,Actress,Director,Year)values("Fast Five","Vin Diesel","Gal Gadot","Justin Lin",2011)''')
except:
    pass

#insert
def add():
    name=input('Enter the Name: ')
    actor=input('Enter the Actor: ')
    actress=input('Enter the name of Actress: ')
    director=input('Enter the Director: ')
    year= input('Enter the year: ')
    cur.execute('Insert into Movies values(?,?,?,?,?)',(name,actor,actress,director,year))

#csv
def output(d):
    with open('Output.csv','w') as f:
                writer=csv.writer(f)
                writer.writerow(['Name','Actor','Actress','Director','Year'])
                writer.writerows(d)
#search
def search():
    print("\nSearch by,")
    print("1.Name")
    print("2.Actor")
    print("3.Actoress")
    print("4.Director")
    print("5.year")
    print("6.All")
    choice=input("Enter choice: ")
    match choice:
        case '1':
            name=input()
            data=cur.execute('SELECT * FROM Movies  where Name = (?)',(name,))
            output(data)

        case '2':
            actor=input()
            data=cur.execute('SELECT * FROM Movies where Actor = (?)',(actor,))
            output(data)

        case '3':
            actress=input()
            data=cur.execute('SELECT * FROM Movies where Actress = (?)',(actress,))
            output(data)

        case '4':
            director=input()
            data=cur.execute('SELECT * FROM Movies where  Director = (?)',(director,))
            output(data)

        case '5':
            year=input()
            data=cur.execute('SELECT * FROM Movies where  Year = (?)',(year,))
            output(data)

        case '6':
            data=cur.execute('SELECT * FROM Movies')
            output(data)
            
        case _:
            print('Wrong choice')
    


if __name__ == "__main__":
    while(True):
        print("\n1.Add ")
        print("2.Search")
        ch=input("Enter the choice: ")
        match ch:
            case '1':
                add()
            case '2':
                search()
        if(input("Do you want to continue?(y/n)")!='y'):
            break

    conn.commit()
    cur.close()
    conn.close()



