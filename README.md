# Running the endpoints

Make sure you have PostgreSQL setup in your system. Create the server and database using pgadmin4.

Open the directory and follow the steps:


1. Install all the requirements using the command: <br><br>
   `pip install -r requirements.txt`<br>

2. Create a .env file and add the following details : <br><br>
   `db_url = postgresql+asyncpg://[your-db-username]:[your-password]@[postgre-server-name]/[db-name]` <br>
   `limit = [Number-of-pokemon-characters-to-fetch]`

3. Create the table in database using the following command (make sure you are in the main directory) : <br><br>
   `py make_datab.py` <br><br>

4. Run the server : <br><br>
   `uvicorn main:app --reload`

5. Follow the hosting link, add '/docs' to it for the Swagger UI interface.

6. Use v1 version. Execute the queries as per your requirement !!
   
