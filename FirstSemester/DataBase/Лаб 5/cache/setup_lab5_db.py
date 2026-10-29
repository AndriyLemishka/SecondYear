import shutil
import os
import sqlite3

src_db = r"Лаб 4\cache\marketplace_3d.db"
dst_db = r"Лаб 5\cache\marketplace_3d.db"
shutil.copy(src_db, dst_db)

conn = sqlite3.connect(dst_db)
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [t[0] for t in cursor.fetchall()]
print("Tables in DB:", tables)
for t in ['seller', 'buyer', 'category', 'license', 'model_3d', 'model_file', 'cart', 'cart_item', 'review']:
    cnt = cursor.execute(f"SELECT count(*) FROM {t};").fetchone()[0]
    print(f"  {t}: {cnt} rows")

conn.close()
