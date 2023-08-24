import mysql.connector

class DB:
    def __init__(self):
        # connect to the database
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',  # Use localhost or actual IP if MySQL is on a different machine
                user='root',
                password='',
                auth_plugin='mysql_native_password',  # Specify the authentication plugin if needed
                database='flights'
            )

            self.mycursor = self.conn.cursor()

            # Create a new database
            # mycursor.execute("CREATE DATABASE indigo") '#' ye ek bar database bana ke commnt kr diya

            print('Connection established and database created')

        except mysql.connector.Error as err:
            print('Connection error:', err)

    def fetch_city_names(self):

        city = []
        self.mycursor.execute("""
        SELECT DISTINCT(Destination) FROM flights.flights
        UNION
        SELECT DISTINCT(Source) FROM flights.flights""")

        data = self.mycursor.fetchall()

        print(data)

        for item in data:
            city.append(item[0])

        return city

    def fetch_all_flights(self,source,destination):

        self.mycursor.execute("""
        SELECT * FROM flights
        WHERE Source = '{}' AND Destination = '{}'
        """.format(source,destination))

        data = self.mycursor.fetchall()

        return data

    def fetch_airline_frequency(self):

        airline = []
        frequency = []

        self.mycursor.execute("""
        SELECT Airline,COUNT(*) FROM flights.flights
        GROUP BY Airline
        """)

        data = self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline, frequency

    def busy_airport(self):
        self.mycursor.execute("""SELECT Source,COUNT(*) FROM (SELECT Source FROM flights.flights
							 UNION ALL
							 SELECT Destination FROM flights.flights) AS t
                            GROUP BY t.Source
                            ORDER BY COUNT(*) DESC
                            """)

        data = self.mycursor.fetchall()

        city = []
        frequency = []

        for item in data:
            city.append(item[0])
            frequency.append(item[1])

        return city,frequency

    def daily_frequency(self):

        date = []
        frequency = []

        self.mycursor.execute("""
        SELECT Date_of_Journey,COUNT(*) FROM flights.flights
        GROUP BY Date_of_Journey
        """)

        data = self.mycursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency.append(item[1])


        return date, frequency













