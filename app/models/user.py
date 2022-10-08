from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship
from database.base_class import Base

class User(Base):
  id: Column(Integer, primary_key=True, index=True)
  first_name: Column(String(255), nullable=True)
  surname: Column(String(255), nulltable=True)
  email: Column(String, index=True, nullable=False)
  is_superuser = Column(Boolean, default=False)
  recipes = relationship(
    "Recipe",
      cascade="all,delete-orphan",
      back_populates="submitter",
      uselist=True,
  )