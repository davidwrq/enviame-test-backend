from app.models  import Enterprise
# Delete all entries of database.
Enterprise.delete().execute()
