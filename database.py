from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from models.booze import Base, Unit

DATABASE_URL = "sqlite:///booze.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionFactory = sessionmaker(bind=engine)
Session = SessionFactory

Base.metadata.create_all(engine)


if __name__ == '__main__':
    session = Session()

    # Define units
    units = [
        Unit(unit_name="Liter", unit_symbol="L", base_unit_id=None, conversion_factor=1.0),
        Unit(unit_name="Centiliter", unit_symbol="cl", base_unit_id=None, conversion_factor=0.01),
        Unit(unit_name="Darab", unit_symbol="darab", base_unit_id=None, conversion_factor=1.0)
    ]

    try:
        # Check if units already exist to avoid duplicates
        existing_units = session.query(Unit.unit_symbol).all()
        existing_symbols = {symbol[0] for symbol in existing_units}

        new_units = [unit for unit in units if unit.unit_symbol not in existing_symbols]

        if new_units:
            session.add_all(new_units)
            session.commit()
            print("Units added successfully!")
        else:
            print("Units already exist in the database.")

    except Exception as e:
        session.rollback()
        print(f"Error: {e}")

    finally:
        session.close()