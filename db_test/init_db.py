from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

user1 = "superpower"
pw1 = "mecha75"
ip1 = "192.168.0.10"
db1 = "flask_web"
mysql_url = f"mysql+pymysql://{user1}:{pw1}@{ip1}/{db1}?charset=utf8"
print mysql_url
# engine = create_engine(mysql_url, echo=true, convert_unicode=True)
# # Declare & create Session
# db_session = scoped_session(sessionmaker(
#     autocommit=False, autoflush=False, bind=engine
# ))
# # Create Sqlalchemy Base Instance
# Base = declarative_base()
# Base.query = db_session.query_property()

# def init_database():
#     Base.metadata.create_all(bind=engine)

