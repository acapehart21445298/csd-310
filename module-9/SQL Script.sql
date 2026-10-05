USE outland_adventures;
CREATE TABLE customer (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Phone VARCHAR(20),
    Email VARCHAR(100)
);
SHOW TABLES;
DESCRIBE customer;
CREATE TABLE location (
    LocationID INT PRIMARY KEY,
    LocationName VARCHAR(100),
    Region VARCHAR(100)
);
CREATE TABLE trip (
    TripID INT PRIMARY KEY,
    TripName VARCHAR(100),
    LocationID INT,
    StartDate DATE,
    EndDate DATE,
    TripPrice DECIMAL(10,2),
    FOREIGN KEY (LocationID) REFERENCES location(LocationID)
);
CREATE TABLE booking (
    BookingID INT PRIMARY KEY,
    CustomerID INT,
    TripID INT,
    BookingDate DATE,
    FOREIGN KEY (CustomerID) REFERENCES customer(CustomerID),
    FOREIGN KEY (TripID) REFERENCES trip(TripID)
);
CREATE TABLE equipment (
    EquipmentID INT PRIMARY KEY,
    EquipmentName VARCHAR(100),
    EquipmentType VARCHAR(50),
    PurchaseDate DATE,
    InventoryStatus VARCHAR(50)
);
CREATE TABLE equipment_transaction (
    TransactionID INT PRIMARY KEY,
    CustomerID INT,
    EquipmentID INT,
    TransactionDate DATE,
    TransactionType VARCHAR(50),
    FOREIGN KEY (CustomerID) REFERENCES customer(CustomerID),
    FOREIGN KEY (EquipmentID) REFERENCES equipment(EquipmentID)
);