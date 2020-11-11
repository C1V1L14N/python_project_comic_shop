
from db.run_sql import run_sql
from models.comic import Comic
from models.publisher import Publisher

import repositories.publisher_repository as publisher_repository

def save(comic):
     sql = "INSERT INTO comics (name, author, genre, wholesale_price, markup, stock_count, min_count, out_of_stock, publisher_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
     values = [comic.name, comic.author, comic.genre, comic.wholesale_price, comic.markup, comic.stock_count, comic.min_count, comic.out_of_stock, comic.publisher.id]
     results = run_sql(sql, values)
     id = results[0]['id']
     comic.id = id
     return comic

def select_all():
     comics = []

     sql = "SELECT * FROM comics"
     results = run_sql(sql)

     for row in results:
          publisher = publisher_repository.select(row['publisher_id'])
          comic = Comic(row['name'], row ['author'], row['genre'], row['wholesale_price'], row['markup'], row['stock_count'], row['min_count'], row['out_of_stock'], publisher, row['id'])
          comics.append(comic)
     return comics


def select(id):
     comic = None
     sql = "SELECT * FROM comics WHERE id = %s"
     values = [id]
     result = run_sql(sql, values)[0]

     if result is not None:
          publisher = publisher_repository.select(result['publisher_id'])
          comic = Comic(result['name'], result['author'], result['genre'], result['wholesale_price'], result['markup'], result['stock_count'], result['min_count'], result['out_of_stock'], publisher, result['id'])
     return comic


def delete_all():
     sql = "DELETE  FROM comics"
     run_sql(sql)


def delete(id):
     sql = "DELETE  FROM comics WHERE id = %s"
     values = [id]
     run_sql(sql, values)


def update(comic):
     sql = "UPDATE comics SET (name, author, genre, wholesale_price, markup, stock_count, min_count, out_of_stock, publisher_id) = (%s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
     values = [comic.name, comic.author, comic.genre, comic.wholesale_price, comic.markup, comic.stock_count, comic.min_count, comic.out_of_stock, comic.publisher.id, comic.id]
     result = run_sql(sql, values)


def publisher(comic):
     sql = "SELECT * FROM comics WHERE publisher_id = %s"
     values = [comic.id]
     result = run_sql(sql, values)

     for row in result:
          publisher = Publisher(row['name'], row['id'])
     return publisher


def find_single_comic(name):
     comic = None
     sql = "SELECT * FROM comics WHERE name = %s"
     values = [name]
     result = run_sql(sql, values)[0]

     if result is not None:
          publisher = publisher_repository.select(result['publisher_id'])
          comic = Comic(result['name'], result ['author'], result['genre'], result['wholesale_price'], result['markup'], result['stock_count'], result['min_count'], result['out_of_stock'], publisher, result['id'])
          return comic

def find_comics_by_publisher(publisher_name):
     comics = []
     sql = "SELECT comics.* FROM comics INNER JOIN publishers ON comics.publisher_id = publishers.id WHERE publishers.name = %s"
     values = [publisher_name]
     results = run_sql(sql, values)

     for row in results:
          publisher = publisher_repository.select(row['publisher_id'])
          comic = Comic(row['name'], row['author'], row['genre'], row['wholesale_price'], row['markup'], row['stock_count'], row['min_count'], row['out_of_stock'], publisher, row['id'])

          comics.append(comic)
     return comics








