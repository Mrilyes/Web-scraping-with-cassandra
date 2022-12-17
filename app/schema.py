# schema using pydantic for data validation and cleaning
# why not using only models cassandra driver?
# cassandra driver can validate data as schema with pydantic but it dosen't work directly with fast api  
# fast api is designed to use pedantic as a validation tool in any given response .

from uuid import UUID
from typing import Optional, Any
from pydantic import BaseModel, root_validator

from . import utils

class ProductSchema(BaseModel):
    asin: str
    title: Optional[str]


class ProductListSchema(BaseModel):
    asin: str
    title: Optional[str]
    price_str: Optional[str]
    brand: Optional[str]
    country_of_origin: Optional[str]
    screen_size: Optional[str]
    color: Optional[str]
    hard_disk_size: Optional[str]
    cpu_model: Optional[str]
    ram_memory_installed_size: Optional[str]
    operating_system: Optional[str]
    card_description: Optional[str]
    graphics_coprocessor: Optional[str]
    cpu_speed: Optional[str]
    standing_screen_display_size: Optional[str]
    max_screen_resolution: Optional[str]
    processor: Optional[str]
    ram : Optional[str]
    hard_drive: Optional[str]
    chipset_brand: Optional[str]
    item_model_number: Optional[str]
    hardware_platform: Optional[str]
    item_weight: Optional[str]
    product_dimensions: Optional[str]
    item_dimensions_lxwxh: Optional[str]
    processor_brand: Optional[str]
    processor_count: Optional[str]
    computer_memory_type: Optional[str]
    hard_drive_interface: Optional[str]
    batteries: Optional[str]


class ProductScrapeEventSchema(BaseModel):
    uuid: UUID
    asin: str
    title: Optional[str]
    price_str: Optional[str]


class ProductScrapeEventDetailSchema(BaseModel):
    uuid: UUID
    asin: str
    title: Optional[str]
    price_str: Optional[str]
    created: Optional[Any] = None
    brand: Optional[str]
    country_of_origin: Optional[str]
    screen_size: Optional[str]
    color: Optional[str]
    hard_disk_size: Optional[str]
    cpu_model: Optional[str]
    ram_memory_installed_size: Optional[str]
    operating_system: Optional[str]
    card_description: Optional[str]
    graphics_coprocessor: Optional[str]
    cpu_speed: Optional[str]
    standing_screen_display_size: Optional[str]
    max_screen_resolution: Optional[str]
    processor: Optional[str]
    ram : Optional[str]
    hard_drive: Optional[str]
    chipset_brand: Optional[str]
    item_model_number: Optional[str]
    hardware_platform: Optional[str]
    item_weight: Optional[str]
    product_dimensions: Optional[str]
    item_dimensions_lxwxh: Optional[str]
    processor_brand: Optional[str]
    processor_count: Optional[str]
    computer_memory_type: Optional[str]
    hard_drive_interface: Optional[str]
    batteries: Optional[str]

    @root_validator(pre=True)
    def extra_create_time_from_uuid(cls, values):
        values['created'] = utils.uuid1_time_to_datetime(values['uuid'].time).timestamp()
        return values        