import cx_Oracle

connection = cx_Oracle.connect("SYSTEM", "enryca1379", "localhost/eCommerce")

cursor = connection.cursor()
cursor.execute("""
SELECT EMAIL, TELEPHONE_NUM, ADDRESS, CITY, ZIP_CODE FROM RECIPIENT
WHERE EMAIL NOT IN (SELECT DISTINCT EMAIL FROM ORDERS)
AND EMAIL LIKE '%gmail%'
ORDER BY EMAIL
""")

for row in cursor:
    print(row)
