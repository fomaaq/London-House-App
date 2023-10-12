import sqlite3


class ConnectionSingleton:
    _connection = None

    def get_connection():
        if ConnectionSingleton._connection is None:
            ConnectionSingleton._connection = sqlite3.connect('london_houses.db')

        return ConnectionSingleton._connection
