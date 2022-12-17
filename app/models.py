from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

data = {
    "asin": "TESTING123D",
    "title": "Mark 1adsf"
}


# List View -> Detail View
class Product(Model): # -> table
    __keyspace__ = "web_scrape" #
    asin = columns.Text(primary_key=True, required=True)
    title = columns.Text()
    brand = columns.Text()
    price_str = columns.Text(default="-100")
    country_of_origin = columns.Text() 
    screen_size = columns.Text() 
    color= columns.Text() 
    hard_disk_size= columns.Text() 
    cpu_model= columns.Text() 
    ram_memory_installed_size= columns.Text() 
    operating_system= columns.Text() 
    card_description= columns.Text() 
    graphics_coprocessor= columns.Text() 
    cpu_speed= columns.Text() 
    standing_screen_display_size= columns.Text() 
    max_screen_resolution= columns.Text() 
    processor= columns.Text() 
    ram = columns.Text() 
    hard_drive= columns.Text() 
    chipset_brand= columns.Text() 
    item_model_number= columns.Text() 
    hardware_platform= columns.Text() 
    item_weight= columns.Text() 
    product_dimensions= columns.Text() 
    item_dimensions_lxwxh= columns.Text() 
    processor_brand= columns.Text() 
    processor_count= columns.Text() 
    computer_memory_type= columns.Text() 
    hard_drive_interface= columns.Text() 
    batteries= columns.Text() 


# Detail View for asin
class ProductScrapeEvent(Model): # -> table
    __keyspace__ = "web_scrape" #
    uuid = columns.UUID(primary_key=True) # uuid.uuid1() -> #time
    asin = columns.Text(index=True)
    title = columns.Text()
    brand = columns.Text()
    country_of_origin = columns.Text() 
    screen_size = columns.Text()
    price_str = columns.Text(default="-100")
    color= columns.Text() 
    hard_disk_size= columns.Text() 
    cpu_model= columns.Text() 
    ram_memory_installed_size= columns.Text() 
    operating_system= columns.Text() 
    card_description= columns.Text() 
    graphics_coprocessor= columns.Text() 
    cpu_speed= columns.Text() 
    standing_screen_display_size= columns.Text() 
    max_screen_resolution= columns.Text() 
    processor= columns.Text() 
    ram = columns.Text() 
    hard_drive= columns.Text() 
    chipset_brand= columns.Text() 
    item_model_number= columns.Text() 
    hardware_platform= columns.Text() 
    item_weight= columns.Text() 
    product_dimensions= columns.Text() 
    item_dimensions_lxwxh= columns.Text() 
    processor_brand= columns.Text() 
    processor_count= columns.Text() 
    computer_memory_type= columns.Text() 
    hard_drive_interface= columns.Text() 
    batteries= columns.Text() 

# def this -> ProductScrapeEvent.objects().filter(asin="AMZNIDNUMBER")

# not this -> Product.objects().filter(title="Mark 1")