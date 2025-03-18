from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from .base import Base

cocktail_ingredient_association = Table(
    "cocktail_ingredient",  # The name of the association table
    Base.metadata,
    Column("cocktail_id", Integer, ForeignKey("cocktail.id"), primary_key=True),
    Column("ingredient_id", Integer, ForeignKey("ingredient.id"), primary_key=True)
)

class Cocktail(Base):
    __tablename__ = 'cocktail'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    price = Column(Integer,nullable=False )

    # This relationship reflects that each cocktail has many ingredients through CocktailIngredient
    ingredients = relationship(
        "Ingredient", 
        secondary=cocktail_ingredient_association, 
        backref="cocktails"
    )

