from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from .base import Base
from .cocktail import cocktail_ingredient_association

class Ingredient(Base):
    __tablename__ = 'ingredient'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    amount = Column(Float, nullable=False)  # Amount of ingredient in the cocktail
    unit = Column(String(50), nullable=False)  # Unit of measurement (e.g., ml, oz)

    # Relationship to cocktail_ingredient, automatically created by the 'backref' in Cocktail
    #cocktails = relationship('Cocktail', secondary=cocktail_ingredient_association, backref='ingredients')

    def __repr__(self):
        return f"{self.amount} {self.unit} {self.name}"