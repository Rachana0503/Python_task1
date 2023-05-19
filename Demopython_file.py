import mysql.connector
from flask import Flask,render_template
import csv
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
    )
mycursor = mydb.cursor()
#Creating the database and table products
mycursor.execute("CREATE DATABASE IF NOT EXISTS python")
mycursor.execute("USE python")
mycursor.execute("CREATE TABLE IF NOT EXISTS products (product_number VARCHAR(250), date_of_purchase DATE, product_type VARCHAR(250), Price INT)")

mydb.commit()


#Creating the text file which has product details
file1 = open("zample.txt","w")
L = ["MSETC4, 2021-06-04, i-Phone, 490000 \n",
     "MSETC3, 2022-07-08, hp-laptop, 698766 \n",
     "MSETAS2, 2021-04-09, CPU, 99000 \n",
     "MSETAS7, 2021-08-02, Mouse, 900 \n"]
file1.writelines(L)
file1.close()



#Converting the file to csv format
with open('zample.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",")for line in stripped if line)
    with open('zample.csv','w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('product_number','date_of_purchase','product_type','price'))
        writer.writerows(lines)

app =Flask(__name__)
@app.route('/')
def home():
    mycursor = mydb.cursor()
    csv_data = csv.reader(open('zample.csv'))
    header = next(csv_data)
    for row in csv_data:
        if(row):
            mycursor.execute("INSERT INTO products(product_number, date_of_purchase, product_type, Price) VALUES (%s, %s, %s, %s);", row)
    mydb.commit()
    mycursor.close()

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM products")

    myresult = mycursor.fetchall()
    return render_template('sample2023.html',data=myresult)

if __name__=='__main__':
    app.run(debug=True)












