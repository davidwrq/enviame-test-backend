from sqlfaker.database import Database

# add database
my_db = Database(db_name="test.db")

my_db.add_table(table_name="enterprise", n_rows=10)

my_db.generate_data()
my_db.export_sql("db/init.sql")
