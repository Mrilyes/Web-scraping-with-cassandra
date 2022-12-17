import uuid
import copy
from .models import Product , ProductScrapeEvent


def create_entry(data:dict):
    # The ** is directly used for packing and sending a dictionary as a function argument.
    return Product.create(**data)

def create_scrape_entry(data:dict):
    data['uuid'] = uuid.uuid1() # includes a timestamp
    return ProductScrapeEvent.create(**data)

def add_scrape_event(data:dict , fresh = False):
    if fresh:
        data = copy.deepcopy(data)
    product = create_entry(data)
    scrape_obj = create_scrape_entry(data)
    return product , scrape_obj