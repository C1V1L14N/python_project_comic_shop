
from db.run_sql import run_sql
from models.publisher import Publisher
from models.comic import Comic

def save(publisher):
    sql = "INSERT INTO publishers (name) VALUES (%s) RETURNING *"
    values = [publisher.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    publisher.id = id
    return publisher


def select_all():
    publishers = []


def select(id):


def delete_all():


def delete(id):


def update(publisher):




