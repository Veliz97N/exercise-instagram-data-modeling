import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime,Table
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

historia_visto = Table('historia_visto', Base.metadata,
    Column('id_usuario', ForeignKey('users.id_user'), nullable=False),
    Column('id_historia', ForeignKey('historias.id_historia'), nullable=False)
)

class User(Base):
    __tablename__ = 'users'
    id_user = Column(String(50), primary_key=True)
    email = Column(String(50), nullable=False, unique=True)
    descripcion = Column(Text)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    nickname = Column(String(50), nullable=False)
    created_at = Column(DateTime(), default=datetime.now())

class Publicacion(Base):
    __tablename__ = 'publicaciones'
    id_publicaciones = Column(Integer(), primary_key=True)
    contenido = Column(String(250))
    descripcion = Column(Text())
    created_at = Column(DateTime(), default=datetime.now())
    ubicacion = Column(String(150))
    id_usuario = Column(String(50), ForeignKey('users.id_user'), nullable=False)

class Comentario(Base):
    __tablename__ = 'comentarios'
    id_comentario = Column(Integer(), primary_key=True)
    id_usuario = Column(String(50), ForeignKey('users.id_user'), nullable=False)
    contenido = Column(Text())

class Like(Base):
    __tablename__ = 'likes'
    usuarios = Column(String(50), ForeignKey('users.id_user'), primary_key=True)
    id_comentario = Column(Integer(), ForeignKey('comentarios.id_comentario'), primary_key=True)
    id_publicaciones = Column(Integer(), ForeignKey('publicaciones.id_publicaciones'), primary_key=True)

class Historia(Base):
    __tablename__ = 'historias'
    id_historia = Column(Integer, primary_key=True)
    id_usuario = Column(String(50), ForeignKey('users.id_user'), nullable=False)
    media = Column(String(250), nullable=False)
    created_at = Column(DateTime(), default=datetime.now())
    historia_visto= relationship("User",secondary=historia_visto)

# class Visto(Base):
#     __tablename__ = 'vistos'
#     usuario = Column(String(50), ForeignKey('users.user_id'), primary_key=True)
#     historia = Column(Integer(), ForeignKey('historias.id_historias'), primary_key=True)


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e