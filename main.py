import json
import requests
import sqlite3
conn = sqlite3.connect("../books_sqlite")


key = 'AIzaSyBiJYVKvx7l63JcrHq6fyoOgIKmJl6YmGw'
ISBN = input("შეიყვანეთ 10 ციფრიანი ISBN: ")
playload = {'q': ISBN, 'appid': key }
r = requests.get( "https://www.googleapis.com/books/v1/volumes?", params=playload)
resp= json.loads(r.text)
with open('../books.txt', 'w') as file:
    json.dump(resp, file, indent=4)

ISBN = resp["items"][0]["volumeInfo"]
author = ISBN["authors"]
author2 = author if len(author) > 1 else author[0]

#შევქმენი წიგნებისთვის მონაცემთა ბაზა, სადაც მომხმარებელს შეუძლია წიგნის სათაური, ავტორი, გვერდების რაოდენობა და გამოშვების თარიღი ჩაამატოს ISBN კოდით
cursor = conn.cursor()
#cursor.execute(""" CREATE TABLE books
#          (ISBN INTERGER PRIMARY KEY ,
#           author TEXT(100),
#           title TEXT(200),
#           page INTEGER(2000),
#           year INTEGER(100))
#""")

#conn.commit()

cursor.execute("INSERT INTO books (ISBN, author, title, page, year) VALUES ('{}','{}',{},{})".format(author2, ISBN['title'], ISBN['pageCount'], ISBN['publishedDate']))
conn.commit()


#print(resp.headers)
print(f"\nTitle: {ISBN['title']}")
print(f"Author: {author2}")
print(f"Page Count: {ISBN['pageCount']}")
print(f"Publication Date: {ISBN['publishedDate']}")
print("\n***\n")

conn.close()





