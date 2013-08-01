import sqlite3 as sqlite

class DBHelper(object):
    """Helper class for SQLite DB access"""

    _instance = None

    def __new__(cls, db=':memory:', *args, **kwargs):
        """Override __new__ to implement singleton pattern"""

        if not cls._instance:
            cls._instance = super(DBHelper, cls).__new__(cls, *args, **kwargs)
            cls._instance._conn = None
            cls._instance.set_db(db)
        return cls._instance

    def __del__(self):
        """Destructor"""

        self._conn.close()

    @staticmethod
    def _row_factory(cursor, row):
        """Dict row factory function"""

        data = {}
        for key, col in enumerate(cursor.description):
            data[col[0]] = row[key]
        return data

    def get_connection(self):
        """Retrive current SQLite connection"""
        return self._conn

    def set_db(self, db):
        """Set SQLite DB filename"""

        if self._conn is not None:
            self._conn.close()

        if db is None:
            self._conn = None
        else:
            self._conn = sqlite.connect(db)
            self._conn.row_factory = DBHelper._row_factory
            self._conn.text_factory = str
            self._conn.cursor().execute('PRAGMA foreign_keys = ON')

        return self
