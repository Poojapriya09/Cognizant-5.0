class DatabaseConnection:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            print("Creating Database Connection...")
            cls.__instance = super(DatabaseConnection, cls).__new__(cls)
            cls.__instance.connection = "Connected to PostgreSQL"
        return cls.__instance

    def get_connection(self):
        return self.connection


# Testing
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1.get_connection())

print("db1 ID:", id(db1))
print("db2 ID:", id(db2))

if db1 is db2:
    print("Singleton works! Both objects are the same.")
else:
    print("Singleton failed.")