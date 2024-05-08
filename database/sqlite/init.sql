CREATE TABLE IF NOT EXISTS main.Employee (
    emplid integer PRIMARY KEY AUTOINCREMENT,
    firstname nvarchar(15) NOT NULL,
    lastname nvarchar(15) NOT NULL,
    surname nvarchar(15) NOT NULL,
    parperhour float NOT NULL,
    empstartdate date NOT NULL DEFAULT CURRENT_TIMESTAMP,
    dismissdate date DEFAULT NULL,
    empstatus boolean DEFAULT TRUE,
    pass_id NOT NULL CHECK (regex('\d{3}-\d{3}')) UNIQUE,  /* Функция regex из внешнего модуля sqlite-regex  https://github.com/asg017/sqlite-regex*/
    CONSTRAINT check_emp_date CHECK (empstartdate <= dismissdate),
    CONSTRAINT check_payment CHECK (parperhour > 0)
    );


CREATE TABLE IF NOT EXISTS main.Bookkeeping (
    id integer PRIMARY KEY AUTOINCREMENT,
    ndfltax float,
    tax float,
    yearindexpercently integer,
    CONSTRAINT positive_ndfl CHECK (ndfltax > 0),
    CONSTRAINT positive_other_tax CHECK (tax > 0),
    CONSTRAINT positive_year_index CHECK (yearindexpercently > 0)
);


CREATE TABLE IF NOT EXISTS main.Sallary (
    sid blob DEFAULT (randomblob(16)) PRIMARY KEY,
    emplid integer,
    nid integer,
    totalhour integer,
    date_ date,
    FOREIGN KEY (emplid) REFERENCES Employee (emplid) ON DELETE NO ACTION ON UPDATE RESTRICT,
    FOREIGN KEY (nid) REFERENCES Bookkeeping (id) ON DELETE NO ACTION ON UPDATE RESTRICT,
    CONSTRAINT positive_h CHECK (totalhour BETWEEN 0 AND 744)
);


/* Нельзя выдать зарплату без информации о налогах */
CREATE TRIGGER IF NOT EXISTS main.check_exists_bookkeeping
BEFORE INSERT ON Sallary
BEGIN
    SELECT 1 AS counter,
    CASE WHEN counter == 0 THEN RAISE(ABORT, 'Сначала нужно добавить бухгалтерскую информацию в таблицу Bookkeeping') END
    FROM Bookkeeping;
END;


/* Зарплата выдаётся за месяц работы: если за конкретный месяц зарплата уже была выдана, то нельзя допустить повторной выдачи */
CREATE TRIGGER IF NOT EXISTS main.check_one_sallary_per_month
BEFORE UPDATE ON Sallary
BEGIN
    SELECT 1 AS counter,
    IIF(counter = 1, RAISE(ABORT, 'test'))
    FROM Sallary
    WHERE date_('%Y') = STRFTIME('%Y', DATE('now')) AND date_('%m') = STRFTIME('%m', DATE('now'));
END;


CREATE TRIGGER IF NOT EXISTS main.sallary_immutable
BEFORE UPDATE ON Sallary
BEGIN
    SELECT RAISE(ROLLBACK, 'Выданная зарплата редактированию не подлежит');
END;
