#!/usr/bin/python3

import os
import sys
sys.path.append(os.pardir)

from amazon.api import AmazonAPI

from account import AMAZON_ASSOCIATE_TAG, AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_LOCALE


amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOCIATE_TAG, region=AMAZON_LOCALE)


def search(keyword, max_count, search_index):
    products = []
    for product in amazon.search_n(max_count, Keywords=keyword, SearchIndex=search_index):
        products.append({
            'asin': product.asin,
            'title': product.title,
            'author': product.author,
            'price': product.price_and_currency[0],
            'image_url': product.large_image_url,
            'publisher': product.get_attribute('Publisher'),
            'publication_date': product.get_attribute('PublicationDate'),
        })

    return products


def lookup(asin):
    product = amazon.lookup(ItemId=asin)

    return product
