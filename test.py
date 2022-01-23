import sqlite3
conn = sqlite3.connect("Pasha.db")
cursor = conn.cursor()#объект, который получает за получение данных из бд

cursor.executescript('''
    CREATE TABLE "Курсы" (
	"id_courses"	INTEGER,
	"name_courses"	TEXT,
	"id_lesson"	INTEGER,
	"id_teacher"	INTEGER,
	FOREIGN KEY("id_teacher") REFERENCES "Учителя"("id_teacher"),
	FOREIGN KEY("id_lesson") REFERENCES "Уроки"("id_lesson"),
	PRIMARY KEY("id_courses" AUTOINCREMENT)
        )

    INSERT INTO "main"."Курсы"
    ("id_courses", "name_courses", "id_lesson", "id_teacher")
    VALUES (1, '2', 3, 4);

    UPDATE id_courses SET name = 'Joye' WHERE name = 'Johnny';
    UPDATE students SET lastname = 'Chesnokov' WHERE lastname = 'Pcanov';
    '''
)


conn.commit()
