__author__ = 'rafael'

from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)

# Declare a mapping
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password)

print(User.__table__)


# Create a schema
Base.metadata.create_all(engine)

# Create a session
from sqlalchemy.orm import sessionmaker
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# Adding and updating objects
ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
session.add(ed_user)

# Query

our_user = session.query(User).filter_by(name='ed').first()

print(our_user)

print(ed_user is our_user)

session.add_all([
    User(name='wendy', fullname='Wendy Williams', password='foobar'),
    User(name='mary', fullname='Mary Contrary', password='xxg527'),
    User(name='fred', fullname='Fred Flinstone', password='blah')])

# Change record field
ed_user.password = 'f8s7ccs'
# A non-committed change
print(session.dirty)

# Records not commited
print(session.new)

# Get the IDfro a particular record
print(ed_user.id)

session.commit()

# No non-committed changes after commit()
print(session.dirty)