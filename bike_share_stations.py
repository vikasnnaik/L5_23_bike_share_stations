
"""Manage bike-share stations using an in-memory SQLite database."""

import random
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE stations ("
    "id INTEGER PRIMARY KEY, "
    "name TEXT, capacity INTEGER, bikes INTEGER)"
)


def add_station(name, capacity, bikes, log=None):
    """Add a station and append its name to the supplied log."""
    if log is None:
        log = []

    conn.execute(
        "INSERT INTO stations (name, capacity, bikes) VALUES "
        "('" + name + "', " + str(capacity) + ", " + str(bikes) + ")"
    )
    log.append(name)
    return log


def rent_bike(station_id):
    """Rent a bike if the station exists and has bikes available."""
    row = conn.execute(
        "SELECT bikes FROM stations WHERE id = ?", (station_id,)
    ).fetchone()

    if row and row[0] > 0:
        conn.execute(
            "UPDATE stations SET bikes = bikes - 1 WHERE id = ?",
            (station_id,),
        )
        return True

    return False


def unlock_pin():
    """Generate a four-digit station unlock PIN."""
    return random.randint(1000, 9999)


def full_stations():
    """Return names of stations where all bike slots are occupied."""
    stations = conn.execute(
        "SELECT name FROM stations WHERE bikes = capacity"
    ).fetchall()
    return [station[0] for station in stations]


def reset_station(station_id):
    """Reset the bike count for a station."""
    try:
        conn.execute(
            "UPDATE stations SET bikes = 0 WHERE id = ?", (station_id,)
        )
    except Exception:
        pass


def has_bikes(station_id):
    """Check whether a station has bikes available."""
    row = conn.execute(
        "SELECT bikes FROM stations WHERE id = ?", (station_id,)
    ).fetchone()

    if row is None or row[0] is None:
        return False

    return row[0] > 0


def main():
    """Run a short demonstration of the bike-share operations."""
    add_station("Central Park", 10, 10)
    add_station("Metro Gate", 8, 2)
    print(rent_bike(2), rent_bike(9) is False)
    print(unlock_pin(), full_stations(), has_bikes(2))
    reset_station(1)


if __name__ == "__main__":
    main()
