INSERT INTO Members (name, email, phone, address, membership_start, membership_end)
VALUES
('John Doe', 'john.doe@example.com', '1234567890', '123 Elm Street, Springfield', '2024-01-01', '2024-12-31'),
('Jane Smith', 'jane.smith@example.com', '0987654321', '456 Oak Street, Springfield', '2024-02-01', '2024-12-31');
INSERT INTO Books (title, author, publisher, published_date, isbn, copies)
VALUES
('The Great Gatsby', 'F. Scott Fitzgerald', 'Scribner', '1925-04-10', '9780743273565', 5),
('To Kill a Mockingbird', 'Harper Lee', 'J.B. Lippincott & Co.', '1960-07-11', '9780061120084', 3);
INSERT INTO Loans (member_id, book_id, issue_date, return_date, due_date, fine_paid)
VALUES
(1, 1, '2024-09-01', NULL, '2024-09-15', FALSE),
(2, 2, '2024-09-01', '2024-09-10', '2024-09-15', TRUE);
INSERT INTO Loans (member_id, book_id, issue_date, return_date, due_date, fine_paid)
VALUES
(1, 1, '2024-09-01', NULL, '2024-09-15', FALSE),
(2, 2, '2024-09-01', '2024-09-10', '2024-09-15', TRUE);
INSERT INTO Complaints (member_id, complaint_date, description, status)
VALUES
(1, '2024-09-02', 'Book was damaged when received.', 'Resolved'),
(2, '2024-09-03', 'Late fee was charged incorrectly.', 'Pending');
INSERT INTO Fines (loan_id, fine_amount, fine_date, fine_status)
VALUES
(2, 5.00, '2024-09-11', 'Paid'),
(1, 10.00, '2024-09-16', 'Unpaid');
