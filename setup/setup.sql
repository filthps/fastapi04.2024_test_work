DROP TABLE sqlite_db.Employee
DROP TABLE sqlite_db.Bookkeeping
DROP TABLE sqlite_db.Sallary


CREATE TABLE IF NOT EXISTS sqlite_db.Employee (
    emplid integer PRIMARY KEY AUTOINCREMENT,
    firstname nvarchar(15),
    lastname nvarchar(15),
    surname nvarchar(15),
    parperhour float,
    empstartdate date,
    dismissdate date
    )


CREATE TABLE IF NOT EXISTS sqlite_db.Bookkeeping (
    id integer PRIMARY KEY AUTOINCREMENT,
    ndfltax float,
    tax float,
    yearindexpercently integer
)


CREATE TABLE IF NOT EXISTS sqlite_db.Sallary (
    sid blob default lower(hex(randomblob(16))) PRIMARY KEY,
    emplid integer,
    nid integer,
    totalhour integer,
    date_ date,
    FOREIGN KEY (emplid) REFERENCES sqlite_db.Employee (emplid) ON DELETE NO ACTION ON UPDATE RESTRICT,
    FOREIGN KEY (nid) REFERENCES sqlite_db.Bookkeeping (id) ON DELETE NO ACTION ON UPDATE RESTRICT
)
