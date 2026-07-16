from database import get_connection
def seed_database():
    """Inserts sample providers, rooms, and a patient for testing."""
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Provider (name, role) VALUES (?, ?)",
        ("Dr. Alicia Chen", "dentist")
    )
    cursor.execute("INSERT INTO Provider (name, role) VALUES (?, ?)", ("Devon Patel", "hygienist"))
    cursor.execute("INSERT INTO Room (roomType) VALUES (?)",("cleaning",))
    cursor.execute("INSERT INTO Room (roomType) VALUES (?)",("procedure",))
    
    cursor.execute(
        "INSERT INTO Patient (fullName, address, phone, emergencyContact, medicalHistory, recordStatus) VALUES (?, ?, ?, ?, ?, ?)",
        ("Jordan Ramirez", "123 Maple St, Springfield", "555-019-2231", "Sam Ramirez, 555-019-9981", "No known allergies", "complete")
    )
    connection.commit()
    connection.close()
    print("Sample data inserted.")
if __name__ == "__main__":
    seed_database()
    