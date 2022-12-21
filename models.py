import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from db_config import DSN

engine = create_async_engine(DSN)
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base(bind=engine)



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=True)
    password = Column(String, nullable=False)
    #advertisements = relationship("Advertisement", back_populates='user')

    def __str__(self):
        return '{} {} {}'.format(self.id, self.email, self.password)


class Advertisement(Base):
    __tablename__ = 'Advertisements'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(length=50), nullable=False)
    description = Column(String(length=100), nullable=False)
    created = Column(DateTime, default=datetime.datetime.now())
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship(User, backref='advertisements')
    #user = relationship(User, back_populates='advertisements')

#
# def create_tables():
#     Base.metadata.drop_all()
#     Base.metadata.create_all()
#
#
# create_tables()
