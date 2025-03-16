from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from wtforms import StringField, SelectMultipleField
from flask_wtf import FlaskForm
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.booze import Base, Cocktail, Ingredient, cocktail_ingredient_association

# Flask App Setup
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Required for Flask-Admin

# SQLite Database Setup
DATABASE_URL = "sqlite:///booze.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)
session = Session()

# Initialize Flask-Admin
admin = Admin(app, name='Cocktail Admin', template_mode='bootstrap3')

# Cocktail and Ingredient Models (already defined above)


class CocktailView(ModelView):
    
    # Display columns for the Cocktail view
    column_list = ('name', 'ingredients')  # Show cocktail name and its ingredients in the list view
    
    # Custom form handling for cocktails
    form_columns = ['name', 'ingredients']
    

        
        
class IngredientView(ModelView):
    column_list = ('name', 'amount','unit')

# Add the view to Flask-Admin
admin.add_view(CocktailView(Cocktail, session))
admin.add_view(IngredientView(Ingredient, session))
Base.metadata.create_all(engine)
if __name__ == '__main__':
    app.run(debug=True)
