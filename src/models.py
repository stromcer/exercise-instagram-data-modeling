import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class MediaEnum(enum.Enum):
    avi = ".avi"
    mp4 = ".mp4"
    mp3 = ".mp3"

class Follower(Base):
    __tablename__ = 'follower'

    user_from_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'))

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250), primary_key=True )

class Media(Base):
    __tablename__ = 'media'

    id = Column(Integer, primary_key=True)
    type = Column(Enum(MediaEnum))
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

class Comment(Base):    
    __tablename__ = 'comment'
 
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(String(250), ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
