from sqlalchemy import Column, ForeignKey, Integer, String, SmallInteger, Date
# from sqlalchemy import Text, DateTime, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
# from datetime import datetime

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(155))
    dob = Column(Date())
    gender = Column(String(55))
    address = Column(String(255))

    section_id = Column(Integer, ForeignKey('section.id'))
    class_id = Column(Integer, ForeignKey('classes.id'))

    classes = relationship("Classes", back_populates="student")
    section = relationship("Section", back_populates="student")


class Classes(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True)
    name = Column(String(155))

    student = relationship("Student", back_populates="classes")


class Section(object):
    __tablename__ = "section"

    id = Column(Integer, primary_key=True)
    name = Column(String(55))

    student = relationship("Student", back_populates="section")
