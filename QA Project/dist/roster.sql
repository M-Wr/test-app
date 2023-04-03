create TABLE employees (
    emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    emp_name VARCHAR(30),
    business_unit CHAR(3),
    emp_active BOOLEAN DEFAULT 1
)
