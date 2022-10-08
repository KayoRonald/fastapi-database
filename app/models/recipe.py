from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.base_class import Base

class Recipe(Base):  # 1
  id: Column(Integer, primary = True, index = True)
  label = Column(String(256), nullable=False)
  url = Column(String(256), index=True, nullable=True)
  source = Column(String(256), nullable=True)
  submitter_id = Column(String(10), ForeignKey("user.id"), nullable=True)
  submitter = relationship("User", back_populates="recipes")
