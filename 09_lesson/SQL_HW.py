from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://postgres:Gravel@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_insert():
    sviaz = db.connect()
    transaction = sviaz.begin()
    sql_nadpis = text("insert into subject("
                      "\"subject_title\") values (:new_title)")
    new_data = {"new_title": "Scottish"}
    otvet = sviaz.execute(sql_nadpis, new_data)
    transaction.commit()
    print(otvet)
    sviaz.close()


def test_update():
    sviaz = db.connect()
    transaction = sviaz.begin()
    sql_nadpis = text("UPDATE subject SET subject_id = "
                      ":new_id WHERE subject_title = :new_title")
    new_data = {"new_id": "17", "new_title": "Scottish"}
    otvet = sviaz.execute(sql_nadpis, new_data)
    transaction.commit()
    print(otvet)
    sviaz.close()


def test_delete():
    sviaz = db.connect()
    transaction = sviaz.begin()

    sql = text("DELETE FROM subject WHERE subject_id = :id")
    sviaz.execute(sql, {"id": 17})

    transaction.commit()
    sviaz.close()
