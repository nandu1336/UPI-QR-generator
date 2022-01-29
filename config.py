import urllib.parse

DB_NAME="upi_qr_generator"
DB_USERNAME="anandkulkarni91"
DB_PASSWORD="Anand@7097"

DB_CONNECTION_STRING = f"mongodb+srv://{urllib.parse.quote(DB_USERNAME)}:{urllib.parse.quote(DB_PASSWORD)}@cluster0.pvcf8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

