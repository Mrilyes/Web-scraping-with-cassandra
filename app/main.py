from typing import List
from fastapi import FastAPI
from cassandra.cqlengine.management import sync_table

from . import  (
    db,
    crud,
    config,
    models,
    schema,
)

settings = config.get_settings()
Product = models.Product
ProductScrapeEvent = models.ProductScrapeEvent

app  = FastAPI()

session = None

@app.on_event("startup")
def on_startup():
    global session
    session = db.get_session()
    sync_table(Product)
    sync_table(ProductScrapeEvent)




@app.get("/")
def read_index():
    return {"hello": "world" , "name": settings.name}

# using schema pydantic
@app.get("/products" , response_model=List[schema.ProductListSchema])
def product_list_view():
    return list(Product.objects.all())
# using models cassandra driver
# @app.get("/products")
# def product_list_view():
#     return {"results": list(Product.objects.all())}

@app.post("/events/scrape")
def events_scrape_create_view(data:schema.ProductListSchema):
    product , _ = crud.add_scrape_event(data.dict())
    return product



@app.get("/products/{asin}" , )
def product_detail_view(asin):
    data =  dict(Product.objects.get(asin = asin))
    events = list(ProductScrapeEvent.objects().filter(asin=asin))
    events = [schema.ProductScrapeEventDetailSchema(**x) for x in events]
    data['events'] = events
    data['events_url'] = f"/products/{asin}/events"
    return data 


@app.get("/products/{asin}/events" , response_model=List[schema.ProductScrapeEventDetailSchema])
def product_scrape_list_view(asin):
    return list(ProductScrapeEvent.objects().filter(asin=asin).limit(5)) 
