import pandas
from sqlalchemy import create_engine

hostname="127.0.0.1"
uname="root"
pwd=""
dbname="zip"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
            .format(host=hostname, db=dbname, user=uname, pw=pwd))

tables = pandas.read_csv(r"C:\Users\mosawark\Downloads\zip_code_database.csv")



connection=engine.connect()
connection.close()
print(tables)
