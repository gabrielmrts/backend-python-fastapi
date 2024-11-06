CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_number INT UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    cpf CHAR(11) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    balance NUMERIC(17, 2) DEFAULT 0
);

INSERT INTO users (
    account_number, 
    name, 
    cpf, 
    password
) VALUES (
    1, 
    'Test User', 
    '26323445220',
    '$2a$12$Umf4sI2rUt1cMYU5rNi5sODWlgceHWD/49Isjj/s3EAex2Gi07iFG' -- testpassword123
);