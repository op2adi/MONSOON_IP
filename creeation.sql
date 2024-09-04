CREATE database Library_test;

CREATE TABLE Members (
    member_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15) UNIQUE NOT NULL,
    address TEXT NOT NULL,
    membership_start DATE NOT NULL,
    membership_end DATE NOT NULL
);

CREATE TABLE Books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100) NOT NULL,
    publisher VARCHAR(100),
    published_date DATE,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    copies INT NOT NULL CHECK (copies >= 0)
);

CREATE TABLE Loans (
    loan_id SERIAL PRIMARY KEY,
    member_id INT REFERENCES Members(member_id) ON DELETE CASCADE,
    book_id INT REFERENCES Books(book_id) ON DELETE CASCADE,
    issue_date DATE NOT NULL,
    return_date DATE,
    due_date DATE NOT NULL,
    fine_paid BOOLEAN DEFAULT FALSE,
    CONSTRAINT unique_loan UNIQUE (member_id, book_id, issue_date)
);

CREATE TABLE Complaints (
    complaint_id SERIAL PRIMARY KEY,
    member_id INT REFERENCES Members(member_id) ON DELETE CASCADE,
    complaint_date DATE NOT NULL,
    description TEXT NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending'
);

CREATE TABLE Fines (
    fine_id SERIAL PRIMARY KEY,
    loan_id INT REFERENCES Loans(loan_id) ON DELETE CASCADE,
    fine_amount NUMERIC(10, 2) NOT NULL CHECK (fine_amount >= 0),
    fine_date DATE NOT NULL,
    fine_status VARCHAR(20) DEFAULT 'Unpaid'
);
