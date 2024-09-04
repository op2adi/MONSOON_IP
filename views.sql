-- View to see all members and their borrowed books
CREATE VIEW MemberLoans AS
SELECT 
    m.member_id, 
    m.name, 
    m.email, 
    b.book_id, 
    b.title, 
    l.issue_date, 
    l.due_date, 
    l.return_date, 
    CASE 
        WHEN l.return_date IS NULL AND CURRENT_DATE > l.due_date THEN 'Overdue'
        WHEN l.return_date IS NOT NULL THEN 'Returned'
        ELSE 'In Progress'
    END AS loan_status
FROM 
    Members m
    JOIN Loans l ON m.member_id = l.member_id
    JOIN Books b ON l.book_id = b.book_id;

-- View to see all overdue loans
CREATE VIEW OverdueLoans AS
SELECT 
    m.member_id, 
    m.name, 
    b.book_id, 
    b.title, 
    l.issue_date, 
    l.due_date
FROM 
    Members m
    JOIN Loans l ON m.member_id = l.member_id
    JOIN Books b ON l.book_id = b.book_id
WHERE 
    l.return_date IS NULL AND CURRENT_DATE > l.due_date;

-- View to see all complaints with their status
CREATE VIEW MemberComplaints AS
SELECT 
    c.complaint_id, 
    m.name, 
    c.complaint_date, 
    c.description, 
    c.status
FROM 
    Complaints c
    JOIN Members m ON c.member_id = m.member_id;

-- View to see fines that are unpaid
CREATE VIEW UnpaidFines AS
SELECT 
    f.fine_id, 
    m.name, 
    b.title, 
    f.fine_amount, 
    f.fine_date, 
    f.fine_status
FROM 
    Fines f
    JOIN Loans l ON f.loan_id = l.loan_id
    JOIN Members m ON l.member_id = m.member_id
    JOIN Books b ON l.book_id = b.book_id
WHERE 
    f.fine_status = 'Unpaid';
