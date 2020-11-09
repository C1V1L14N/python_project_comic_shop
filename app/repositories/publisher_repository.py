
from db.run_sql import run_sql
from models.publisher import Publisher
from models.comic import Comic

import repositories.comic_repository as comic_repository

def save(publisher):
    sql = "INSERT INTO publishers (name) VALUES (%s) RETURNING *"
    values = [publisher.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    publisher.id = id
    return publisher


def select_all():
    publishers = []

    sql = "SELECT * FROM publishers"
    results = run_sql(sql)
    
    for row in results:
        publisher = Publisher(row['name'], row['id'])        
        publishers.append(publisher)
    return publishers


def select(id):
    publisher = None
    sql = "SELECT * FROM publishers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        publisher = Publisher(result['name'], result['id'])
    return publisher


def delete_all():
    sql = "DELETE  FROM publishers"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM publishers WHERE id = %s"
    values = id
    run_sql(sql, values)


def update(publisher):
    sql = "UPDATE publishers SET (name) = (%s) WHERE id = %s"
    values = [publisher.name, publisher.id]
    run_sql(sql, values)

def comics(publisher):
    comics = []

    sql = "SELECT * FROM publishers WHERE comic_id = %s"
    values = [publisher.id]
    results = run_sql(sql, values)

    for row in results:
        comic = Comic(row['name'], row ['author'], row['genre'], row['wholesale_price'], row['markup'], row['stock_count'], row['min_count'], row['out_of_stock'], row['publisher'])
        comics.append(publisher)

# def select_by_name():




