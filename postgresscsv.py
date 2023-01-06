import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
connection_url = URL.create(
    "postgresql+psycopg2",
    username="consultants",
    password="WelcomeItc@2022",
    host="ec2-13-40-49-105.eu-west-2.compute.amazonaws.com",
    port=5432,
    database="testdb"
)

engine = create_engine(connection_url)
df = pd.read_csv('C:\\Users\\Consultants\\Documents\\Warehouse\\payments.csv')

df.to_sql('payments123', con=engine, if_exists='replace')
print(df.head())