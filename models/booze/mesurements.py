from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from .base import Base  # Assuming your Base is defined in src.database

class Unit(Base):
    __tablename__ = "units"

    id = Column(Integer, primary_key=True, autoincrement=True)
    unit_name = Column(String(50), nullable=False)
    unit_symbol = Column(String(10), unique=True, nullable=False)
    base_unit_id = Column(Integer, ForeignKey("units.id"), nullable=True)  # Self-referential ForeignKey
    conversion_factor = Column(DECIMAL(10, 6), nullable=False)

    base_unit = relationship("Unit", remote_side=[id], back_populates="derived_units")
    derived_units = relationship("Unit", back_populates="base_unit", cascade="all, delete-orphan")

    def convert_value(self, value: float, target_unit):
        """ Convert value to another unit using conversion factor. """
        return value * self.conversion_factor / target_unit.conversion_factor
    
    
    def __repr__(self):
        return self.unit_name


class Amount(Base):
    __tablename__ = "amounts"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(DECIMAL(10, 2), nullable=False)
    unit_id = Column(Integer, ForeignKey("units.id"), nullable=False)  # Missing ForeignKey

    ingredient = relationship("Ingredient", back_populates="amounts")


    unit = relationship("Unit")  # Relationship to Unit
    
    def __repr__(self):
        return f"{self.amount} {self.unit.unit_name}"
