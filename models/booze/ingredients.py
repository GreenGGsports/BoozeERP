from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from .base import Base
from .cocktail import cocktail_ingredient_association

class Ingredient(Base):
    __tablename__ = 'ingredient'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)

    # One-to-Many Relationship with Amount
    amount_id = Column(Integer, ForeignKey("amounts.id"), nullable=False)
    amounts = relationship("Amount", back_populates="ingredient")


    def __repr__(self):
        return f"{self.name}"