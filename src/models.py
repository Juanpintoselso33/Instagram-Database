import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, ForeignKey('user.ID'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.ID'))
   
class User(Base):
    __tablename__ = 'user'
    ID = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250))

 
class Post(Base):
    __tablename__ = 'post'
    ID = Column(Integer, primary_key= True)
    user_id = Column(Integer, ForeignKey('user.ID'))

class Comment(Base):
    __tablename__ = 'comment'
    ID = Column(Integer, primary_key= True)
    post_id = Column(Integer, ForeignKey('post.ID'))

class Media(Base):
    __tablename__ = 'media'
    ID = Column(Integer, primary_key= True)
    post_id = Column(Integer, ForeignKey('post.ID'))
    media_type = Column(Enum('image', 'video'), nullable=False)
    url = Column(String(250))    

class Likes(Base):
    __tablename__ = 'likes'
    ID = Column(Integer, primary_key= True)    
    post_id = Column(Integer, ForeignKey('post.ID'))
    user_id = Column(Integer, ForeignKey('user.ID'))   
   

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
