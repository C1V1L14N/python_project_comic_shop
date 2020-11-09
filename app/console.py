import pdb
from models.comic import Comic
from models.publisher import Publisher

import repositories.comic_repository as comic_repository
import repositories.publisher_repository as publisher_repository

comic_repository.delete_all()
publisher_repository.delete_all()


publisher1 = Publisher("Image")
publisher_repository.save(publisher1)

publisher2 = Publisher("Marvel")
publisher_repository.save(publisher2)

publisher3 = Publisher("Vertigo")
publisher_repository.save(publisher3)

comic1 = Comic(name="Goners",author="Jacob Semahn", genre="mystery", wholesale_price=500, markup=5, stock_count=4, min_count=2, out_of_stock=False, publisher=publisher1)
comic_repository.save(comic1)

comic2 = Comic("Planet Hulk","Pak", "super hero", 700, 5, 2, 1, False, publisher2)
comic_repository.save(comic2)

comic3 = Comic("Preacher","Garth Ennis", "drama", 500, 5, 3, 1, False, publisher3)
comic_repository.save(comic3)




pdb.set_trace()
