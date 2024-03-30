CREATE TABLE IF NOT EXISTS students(
    ID VARCHAR(8) PRIMARY KEY,
    first_name VARCHAR(40) NOT NULL,
    middle_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(40) NOT NULL
);

INSERT INTO students (ID, first_name, middle_name, last_name) VALUES ('12БС2020', 'Оксана', 'Евгеньевна', 'Лапшина');
INSERT INTO students (ID, first_name, middle_name, last_name) VALUES ('13БС2020', 'Виктор', 'Николаевич', 'Сорокин');

