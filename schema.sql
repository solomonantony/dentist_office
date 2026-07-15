CREATE TABLE IF NOT EXISTS Provider (
    providerID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    role TEXT NOT NULL  -- 'dentist' or 'hygienist'
);

CREATE TABLE IF NOT EXISTS Room (
    roomID INTEGER PRIMARY KEY AUTOINCREMENT,
    roomType TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Patient (
    patientID INTEGER PRIMARY KEY AUTOINCREMENT,
    fullName TEXT NOT NULL,
    address TEXT,
    phone TEXT,
    emergencyContact TEXT,
    medicalHistory TEXT,
    recordStatus TEXT NOT NULL DEFAULT 'incomplete'  -- 'incomplete' or 'complete'
);

CREATE TABLE IF NOT EXISTS Appointment (
    appointmentID INTEGER PRIMARY KEY AUTOINCREMENT,
    patientID INTEGER NOT NULL,
    providerID INTEGER NOT NULL,
    roomID INTEGER NOT NULL,
    apptDate TEXT NOT NULL,
    apptTime TEXT NOT NULL,
    duration INTEGER NOT NULL,
    visitReason TEXT,
    reminderSentFlag INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (patientID) REFERENCES Patient (patientID),
    FOREIGN KEY (providerID) REFERENCES Provider (providerID),
    FOREIGN KEY (roomID) REFERENCES Room (roomID)
);