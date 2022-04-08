# Imports
from flask import Flask, request, Response
import mysql.connector as sqlc

from urllib.parse import urlparse

# Setup
app = Flask(__name__)

# Connection to MySQL Database
db = sqlc.connect(
        host = "localhost",
        user = "root",
        password = "",
        database= "Store"
    )

print('Connected to MySQL database.')
cur = db.cursor()

@app.route("/form-submit", methods=["POST"])
def submitForm():
    form = request.form
    name = form["Name"]
    email = form["Email"]
    club = form["Club_chapter"]
    position = form["Position"]
    update = form["Update"]

    # Save to DB
    try:
        cur.execute(f"INSERT into Information SET Name='{name}', Email='{email}',Clubs_Chapter='{club}',Position='{position}', Updates='{update}'")
        db.commit()
    except Exception as err:
        print(err)
        return Response("{\"status\": \"Error\"}", mimetype="application/json")

    # Return 200

    return Response("{\"status\": \"OK\"}", mimetype="application/json")

# on running python app.py
if __name__ == "__main__":
    app.run(debug=True)
