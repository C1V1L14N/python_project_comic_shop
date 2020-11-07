
from db.run_sql import run_sql
from models.comic import Comic
from models.publisher import Publisher

def save(comic):
    sql = "INSERT INTO comics (name, author, genre, wholesale_price, markup, stock_count, min_count, out_of_stock, publisher)\
         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,) RETURNING id"
    values = [comic.name, comic.author, comic.genre, comic.wholesale_price,\ 
    comic.markup, comic.stock_count, comic.min_count, comic.out_of_stock, comic.publisher.id]
    results = run_sql(sql, values)
    comic.id = results[0]['id']
