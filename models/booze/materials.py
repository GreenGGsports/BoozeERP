from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from .base import Base

class Material(Base):
    __tablename__ = 'ingredient'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    unit_price = Column(Integer)

    def __repr__(self):
        return f"{self.amount} {self.unit} {self.name}"