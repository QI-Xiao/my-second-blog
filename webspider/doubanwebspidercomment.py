import sqlite3

conn = sqlite3.connect('..\db.sqlite3')
c = conn.cursor()

c.execute("SELECT * FROM blog_commentmovie")
col_name_list = [tuple[0] for tuple in c.description]
print(col_name_list)