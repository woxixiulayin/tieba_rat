#!/usr/bin/env python
from sqlalchemy import Column, String, create_engine, ForeignKey, Integer, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import os


Base = declarative_base()


currdir = os.path.join(os.path.dirname(__file__), 'data.sql')
db_url = 'sqlite:///%s' % currdir

engine = create_engine(db_url)

DBsession = sessionmaker(bind=engine)


class Post(Base):
    __tablename__ = 'post'

    id = Column(String, primary_key=True, unique=True)
    tags = Column(String)
    title = Column(String)
    author = Column(String)
    url_link = Column(String, nullable=False)
    rep_num = Column(Integer)
    last_time = Column(String)
    body = Column(String,default='')
    
# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
