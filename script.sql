CREATE TABLE IF NOT EXISTS regions
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    region_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS cities
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    region_id INTEGER,
    city_name TEXT NOT NULL,
    FOREIGN KEY (region_id) REFERENCES regions (id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS users
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    second_name TEXT NOT NULL,
    first_name TEXT NOT NULL,
    patronymic TEXT DEFAULT NULL,
    region_id INTEGER,
    city_id INTEGER,
    phone TEXT DEFAULT NULL,
    email TEXT DEFAULT NULL,
    FOREIGN KEY (region_id) REFERENCES regions (id) ON DELETE SET NULL,
    FOREIGN KEY (city_id) REFERENCES cities (id) ON DELETE SET NULL
);

INSERT INTO regions (id, region_name) VALUES
	(0, 'Краснодарский край'),
	(NULL, 'Ростовская область'),
	(NULL, 'Ставропольский край');
    
INSERT INTO cities (id, region_id, city_name) VALUES
    (0, 0, 'Краснодар'),
    (NULL, 0, 'Кропоткин'),
    (NULL, 0, 'Славянск'),
    (NULL, 1, 'Ростов'),
    (NULL, 1, 'Шахты'),
    (NULL, 1, 'Батайск'),
    (NULL, 2, 'Ставрополь'),
    (NULL, 2, 'Пятигорск'),
    (NULL, 2, 'Кисловодск');

INSERT INTO users (id, second_name, first_name, patronymic, region_id, city_id, phone, email) VALUES
    (0, 'Иванов', 'Иван', 'Иванович', 0, 0, '+71234567890', 'ivanov.i.i@mail.ru'),
    (NULL, 'Петров', 'Петр', NULL, 1, 1, '+79876543210', 'petrov.p@yandex.ru');