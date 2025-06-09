# Wahaj Al Obid
# CNE 370
# 06.20.2025
# Database Sharding: Leveraging horizontal sharding and Docker to build a scalable and efficient database architecture.

from mysql.connector import connect
from tabulate import tabulate

db = connect(host="127.0.0.1", port=4000, user="maxuser", password="maxpwd")
cursor = db.cursor()

# 1. Largest zipcode in zipcodes_one
print('The largest zipcode in zipcodes_one:')
cursor.execute("SELECT Zipcode FROM zipcodes_one.zipcodes_one ORDER BY Zipcode DESC LIMIT 1;")
print(cursor.fetchone())

# 2. All zipcodes where state = KY
print('\nAll zipcodes where state = KY:')
zipcodes_ky = []

for schema in ['zipcodes_one', 'zipcodes_two']:
    cursor.execute(f"SELECT Zipcode FROM {schema}.{schema} WHERE State = 'KY';")
    zipcodes_ky += [row[0] for row in cursor.fetchall() if row[0]]

print(tabulate([zipcodes_ky[i:i+10] for i in range(0, len(zipcodes_ky), 10)], tablefmt='grid'))

# 3. All zipcodes between 40000 and 41000
print('\nAll zipcodes between 40000 and 41000:')
zipcodes_range = []

for schema in ['zipcodes_one', 'zipcodes_two']:
    cursor.execute(f"SELECT Zipcode FROM {schema}.{schema} WHERE Zipcode BETWEEN 40000 AND 41000;")
    zipcodes_range += [row[0] for row in cursor.fetchall() if row[0]]

print(tabulate([zipcodes_range[i:i+10] for i in range(0, len(zipcodes_range), 10)], tablefmt='grid'))

# 4. TotalWages where state = PA
print('\nTotalWages where state = PA:')
total_wages = []

for schema in ['zipcodes_one', 'zipcodes_two']:
    cursor.execute(f"SELECT TotalWages FROM {schema}.{schema} WHERE State = 'PA';")
    total_wages += [row[0] for row in cursor.fetchall() if row[0]]

print(tabulate([total_wages[i:i+10] for i in range(0, len(total_wages), 10)], tablefmt='grid'))
