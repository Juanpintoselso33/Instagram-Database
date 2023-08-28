import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    ID = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250))
    
    followed_by = relationship('Follower', foreign_keys='Follower.user_to_id', back_populates='followed')
    following = relationship('Follower', foreign_keys='Follower.user_from_id', back_populates='follower')
    likes = relationship("Likes", back_populates="user")
    posts = relationship("Posts", back_populates="posted_by")
    comments = relationship("Comment", back_populates="user")

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, ForeignKey('user.ID'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.ID'), primary_key=True)
    
    follower = relationship('User', foreign_keys=[user_from_id], back_populates='following')
    followed = relationship('User', foreign_keys=[user_to_id], back_populates='followed_by')


class Post(Base):
    __tablename__ = 'post'
    ID = Column(Integer, primary_key= True)
    user_id = Column(Integer, ForeignKey('user.ID'))

    posted_by = relationship("User", back_populates="posts") 
    comments= relationship("Comment", back_populates="post")
    media = relationship("Media", back_populates="post")
    likes = relationship("Likes", back_populates="post")

class Comment(Base):
    __tablename__ = 'comment'
    ID = Column(Integer, primary_key= True)
    user_id = Column(Integer, ForeignKey('user.ID'))
    post_id = Column(Integer, ForeignKey('post.ID'))

    user = relationship("User", back_populates="comments")
    post= relationship("Post", back_populates="comments")

class Media(Base):
    __tablename__ = 'media'
    ID = Column(Integer, primary_key= True)
    post_id = Column(Integer, ForeignKey('post.ID'))
    media_type = Column(Enum('image', 'video'), nullable=False)
    url = Column(String(250))    

    post= relationship("Post", back_populates="media")



class Likes(Base):
    __tablename__ = 'likes'
    ID = Column(Integer, primary_key= True)    
    post_id = Column(Integer, ForeignKey('post.ID'))
    user_id = Column(Integer, ForeignKey('user.ID'))   

    user = relationship("User", back_populates="likes")
    post = relationship("Post", back_populates="likes")
   

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
