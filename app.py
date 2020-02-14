
import os
from flask import Flask, render_template,jsonify
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import *
from flask_cors import CORS, cross_origin

db_url ='postgresql://vjceebhreyputc:b737986d4390ebd9bcb804b66ecb4a19c90669e445168c7ce07c8a16725f448e@ec2-23-21-156-171.compute-1.amazonaws.com/dbd23rm4jgm5s1'
engine = create_engine(db_url)
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save reference to the table
m_1990 = Base.classes.median_data_1990
m_1995 = Base.classes.median_data_1995
m_2000 = Base.classes.median_data_2000
m_2005 = Base.classes.median_data_2005
m_2010 = Base.classes.median_data_2010
m_2015 = Base.classes.median_data_2015
US_health = Base.classes.us_healthcare_costs_percapita


app = Flask(__name__)
@app.route("/")
def home():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/US_healthcare_cost<br/>"
        f"/api/v1.0/fooddata/<countryname><br/>"
        f"/api/v1.0/countrynames<br/>"
        f"/api/v1.0/foodindex<br/>"
    ) 

@app.route("/api/v1.0/US_healthcare_cost")
def healthcare():
    session = Session(engine)  
    data = session.query(US_health.year_cost,US_health.percapitacost).all()
    session.close()
    healthcare_data = []
    for y,d in data:
        healthcare_data.append({
            "Year": y[1::],
            "Data" : int(d)
        })
    return jsonify(list(healthcare_data))

@app.route("/api/v1.0/fooddata/<countryName>")
def foodbyCountry(countryName):
    session = Session(engine)
    sel = [m_1990.countryname,m_1990.fruit_consumption,m_1990.nonstarchy_vegetable_consumption,m_1990.beans_and_legumes,m_1990.nuts_and_seeds,m_1990.unprocessed_red_meat,m_1990.sugarsweetened_beverages,m_1990.fruit_juices,m_1990.protein,m_1990.calcium_milligrams,m_1990.potassium_milligrams,m_1990.total_milk]
    data1990 = session.query(*sel).filter(func.lower(m_1990.countryname) == func.lower(countryName)).all()
    session.close()
    foodCountryData1990 = []
    for row in data1990:
        foodCountryData1990.append({
            'countryName': row[0],
            'Fruit': row[1],
            'Vegetable': row[2],
            'Beans': row[3],
            'nuts': row[4],
            'redMeat': row[5],
            'bev': row[6],
            'fruitJuice': row[7],
            'protein': row[8],
            'total milk': row[11]
        })

    session = Session(engine)
    sel = [m_1995.countryname,m_1995.fruit_consumption,m_1995.nonstarchy_vegetable_consumption,m_1995.beans_and_legumes,m_1995.nuts_and_seeds,m_1995.unprocessed_red_meat,m_1995.sugarsweetened_beverages,m_1995.fruit_juices,m_1995.protein,m_1995.calcium_milligrams,m_1995.potassium_milligrams,m_1995.total_milk]
    data1995 = session.query(*sel).filter(func.lower(m_1995.countryname) == func.lower(countryName)).all()
    session.close()
    foodCountryData1995 = []
    for row in data1995:
        foodCountryData1995.append({
            'countryName': row[0],
            'Fruit': row[1],
            'Vegetable': row[2],
            'Beans': row[3],
            'nuts': row[4],
            'redMeat': row[5],
            'bev': row[6],
            'fruitJuice': row[7],
            'protein': row[8],
            'total milk': row[11]
        })
    
    session = Session(engine)
    sel = [m_2000.countryname,m_2000.fruit_consumption,m_2000.nonstarchy_vegetable_consumption,m_2000.beans_and_legumes,m_2000.nuts_and_seeds,m_2000.unprocessed_red_meat,m_2000.sugarsweetened_beverages,m_2000.fruit_juices,m_2000.protein,m_2000.calcium_milligrams,m_2000.potassium_milligrams,m_2000.total_milk]
    data2000 = session.query(*sel).filter(func.lower(m_2000.countryname) == func.lower(countryName)).all()
    session.close()
    foodCountryData2000 = []
    for row in data2000:
        foodCountryData2000.append({
            'countryName': row[0],
            'Fruit': row[1],
            'Vegetable': row[2],
            'Beans': row[3],
            'nuts': row[4],
            'redMeat': row[5],
            'bev': row[6],
            'fruitJuice': row[7],
            'protein': row[8],
            'total milk': row[11]
        })

    session = Session(engine)
    sel = [m_2005.countryname,m_2005.fruit_consumption,m_2005.nonstarchy_vegetable_consumption,m_2005.beans_and_legumes,m_2005.nuts_and_seeds,m_2005.unprocessed_red_meat,m_2005.sugarsweetened_beverages,m_2005.fruit_juices,m_2005.protein,m_2005.calcium_milligrams,m_2005.potassium_milligrams,m_2005.total_milk]
    data2005 = session.query(*sel).filter(func.lower(m_2005.countryname) == func.lower(countryName)).all()
    session.close()
    foodCountryData2005 = []
    for row in data2005:
        foodCountryData2005.append({
            'countryName': row[0],
            'Fruit': row[1],
            'Vegetable': row[2],
            'Beans': row[3],
            'nuts': row[4],
            'redMeat': row[5],
            'bev': row[6],
            'fruitJuice': row[7],
            'protein': row[8],
            'total milk': row[11]
        })

    session = Session(engine)
    sel = [m_2010.countryname,m_2010.fruit_consumption,m_2010.nonstarchy_vegetable_consumption,m_2010.beans_and_legumes,m_2010.nuts_and_seeds,m_2010.unprocessed_red_meat,m_2010.sugarsweetened_beverages,m_2010.fruit_juices,m_2010.protein,m_2010.calcium_milligrams,m_2010.potassium_milligrams,m_2010.total_milk]
    data2010 = session.query(*sel).filter(func.lower(m_2010.countryname) == func.lower(countryName)).all()
    session.close()
    foodCountryData2010 = []
    for row in data2010:
        foodCountryData2010.append({
            'countryName': row[0],
            'Fruit': row[1],
            'Vegetable': row[2],
            'Beans': row[3],
            'nuts': row[4],
            'redMeat': row[5],
            'bev': row[6],
            'fruitJuice': row[7],
            'protein': row[8],
            'total milk': row[11]
        })

    session = Session(engine)
    sel = [m_2015.countryname,m_2015.fruit_consumption,m_2015.nonstarchy_vegetable_consumption,m_2015.beans_and_legumes,m_2015.nuts_and_seeds,m_2015.unprocessed_red_meat,m_2015.sugarsweetened_beverages,m_2015.fruit_juices,m_2015.protein,m_2015.calcium_milligrams,m_2015.potassium_milligrams,m_2015.total_milk]
    data2015 = session.query(*sel).filter(func.lower(m_2015.countryname) == func.lower(countryName)).all()
    session.close()
    foodCountryData2015 = []
    for row in data2015:
        foodCountryData2015.append({
            'countryName': row[0],
            'Fruit': row[1],
            'Vegetable': row[2],
            'Beans': row[3],
            'nuts': row[4],
            'redMeat': row[5],
            'bev': row[6],
            'fruitJuice': row[7],
            'protein': row[8],
            'total milk': row[11]
        })    

    countryFood = {
        "1990": foodCountryData1990,
        "1995": foodCountryData1995,
        "2000": foodCountryData2000,
        "2005": foodCountryData2005,
        "2010": foodCountryData2010,
        "2015": foodCountryData2015
    }

    return jsonify(list(countryFood))

@app.route("/api/v1.0/countrynames")
def countries():
    session = Session(engine)  
    data = session.query(m_1990.countryname).all()
    session.close()
    countryNames = []
    for n in data:
        countryNames.append(n[0])

    return jsonify(list(countryNames))

@app.route("/api/v1.0/foodindex")
def healthindex():
    metadata = MetaData()
    metadata.reflect(engine)
    tbl = Table('median_data_1990', metadata)
    foodIndex = []
    for column in tbl.c:
        foodIndex.append(column.name)


    return jsonify(list(foodIndex[1:]))



if __name__ == "__main__":
    app.run(debug=True)