from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import select

# The line below is used to connect to the database and send the query's
print ("""

##########
# ENGINE #
##########

""")


engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

# We set the declarative_base as Base
Base = declarative_base()

# Here we create the Authors table and add it to the database.
# We add 2 columns to the Table, id and name, where the id is the id of the Author that
# we would use in the next table, and the name is the name of the Author itself.

print ("""

######################
# Create the classes #
######################

""")
class Authors(Base):
  __tablename__ = "authors"

  id = Column(Integer, primary_key=True)
  name = Column(String(30))

  # This line specifies the relation to the other table that we would use in the
  # next class.
    # "Books" is the table that we are going to use.
    # "back_populates" --->
    # https://docs.sqlalchemy.org/en/14/orm/relationship_api.html#sqlalchemy.orm.relationship.params.back_populates
  books = relationship(
    "Books", back_populates="authors", cascade="all, delete-orphan"
  )
  def __repr__(self):
    return f"Authors(id={self.id!r}, name={self.name!r})"

class Books(Base):
  __tablename__ = "book"

  id = Column(Integer, primary_key=True)
  name = Column(String(50))
  author_id = Column(String, ForeignKey("authors.id"), nullable=False)
  authors = relationship(
    "Authors", back_populates="books"
  )

  def __repr__(self):
    return f"Books(id={self.id!r}, name={self.name!r})"

Base.metadata.create_all(engine)

# Insert data to the database
#  we use the Session from the sqlalchemy.orm to do this task
print ("""

##########
# INSERT #
##########

""")

with Session(engine) as session:
  # User sina with 2 Books
  sina = Authors(
    name="sina",
    books=[
      Books(name="sina_book"),
      Books(name="sina_book2")
    ]
  )

  # User test1 with 1 Books
  test1 = Authors(
    name = "test1",
    books=[
      Books(name="test1-books"),
    ]
  )

  # User test2 with 0 Books
  test2 = Authors(
    name = "test2",
  )
  session.add_all([sina, test1])
  session.commit()

# SELECT
print ("""

############
#  SELECT  #
############

""")

session = Session(engine)

stmt = select(Authors).where(Authors.name.in_(["sina"]))

for auth in session.scalars(stmt):
  print(auth)
print ("""

####################
# SELECT with JOIN #
####################

""")
stmt = (
  select(Books)
  .join(Books.authors)
  .where(Authors.name == "sina")
  .where(Books.name == "sina_book")
)

sina_book = session.scalars(stmt).one()
sina_book


print ("""

###################
#   Make Changes  #
###################

""")








# DELETE
print ("""

##########
# DELETE #
##########

""")
sina = session.get(Authors, 1)
sina.books.remove(sina_book)
session.flush()
