from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from environment import config

Base = declarative_base()

engine = create_engine(f"redis:///?Server={config['server']};Port={config['port']}&Password={config['password']}")

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  name = Column(String(20))
  email = Column(String(50))
  user_name = Column(String(50))
  domain = Column(String(50))
  Infra = Column(String(50))
  def __repr__(self):
    return f"User(id=({self.id!r}), name=({self.name!r}), email=({self.email!r}), domain=({self.domain!r}), infra=({self.infra!r}))"


