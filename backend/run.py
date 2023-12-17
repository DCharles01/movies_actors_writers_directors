from settings import DB_USER, DB_NAME
from api import create_app


app = create_app(user = DB_USER, database = DB_NAME)

app.run(debug=True, port=5001)