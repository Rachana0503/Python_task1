from flask import Flask,render_template
import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="chikmagalur"
    )
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE monday")

#mycursor.execute("SHOW DATABASES")
mycursor.execute("SHOW TABLES")
if mycursor.fetchall():
    print("already exits")
else:
    mycursor.execute("CREATE TABLE products (product_number VARCHAR(250), date_of_purchase DATE, product_type VARCHAR(250), Price INT)")
#ycursor.execute("CREATE TABLE products (product_number VARCHAR(250), date_of_purchase DATE, product_type VARCHAR(250), Price INT)")
#mycursor.execute("SHOW TABLES")




file1 = open("rachana.txt","w")
L = ["RS00122, 2021-06-04, Charger, 40000 \n","RS00222, 2022-07-08, Cable, 6666 \n","RS44003, 2022-01-08, Headset, 40000 \n"]
#file1.write("product_number, date_of_purchase, product_typr, Price \n")
file1.writelines(L)
file1.close()


with open('rachana.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",")for line in stripped if line)
    with open('rachanamc.csv','w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('product_number','date_of_purchase','product_type','price'))
        writer.writerows(lines)



csv_data = csv.reader(open('rachanamc.csv'))
header = next(csv_data)
#mycursor.execute("INSERT INTO products (product_number, date_of_purchase, product_type, Price) VALUES ('e001', '2021-11-11', 'monitor', '600');")
print("Importing the file")
for row in csv_data:
    if(row):
        print(row)
        mycursor.execute("INSERT INTO products (product_number, date_of_purchase, product_type, Price) VALUES (%s, %s, %s, %s);", row)
mydb.commit()        
mycursor.close()
print("Done")

app =Flask(__name__)

@app.route('/')
def home():
    mycursor = mydb.cursor()
    
    mycursor.execute("SELECT * FROM products")

    myresult = mycursor.fetchall()
    return render_template('sample.html',data=myresult)

if __name__=='__main__':
    app.run(debug=True)
#for x in myresult:
  #print(x)










