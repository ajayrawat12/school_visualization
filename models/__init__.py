from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import school_db

print('models sessions imported')

conn_engine = create_engine(school_db)

try:
    school = sessionmaker(bind=conn_engine)
    scl_session = school()
    # suppose the database has been restarted.
    scl_session.commit()
    scl_session.close()

except Exception as e:
    print('DB trying to reconnect')
    connect = sessionmaker(bind=conn_engine)
    scl_session = school()
