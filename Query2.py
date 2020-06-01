import cx_Oracle

connection = cx_Oracle.connect("SYSTEM", "enryca1379", "localhost/eCommerce")

cursor = connection.cursor()
cursor.execute("""

SELECT DISTINCT PRODUCT.PRODUCT_CODE,
PRICE AS ORIGINAL_PRICE,
DISCOUNT,
(PRICE - (DISCOUNT*PRICE/100)) AS PRICE_AFTER_DISCOUNT
FROM PRODUCT INNER
JOIN OVEN ON PRODUCT.PRODUCT_CODE = OVEN.PRODUCT_CODE
WHERE OVEN.COLOUR = 'black'
AND OVEN.TYPE = 'gas'
AND OVEN.TIMER = 'no'
AND (PRICE - (DISCOUNT*PRICE/100)) < 350

""")

for row in cursor:
    print(row)
