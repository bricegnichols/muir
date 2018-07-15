# Produce a list of top rated products from Amazon
# require weights, price, ratings

from amazon.api import AmazonAP
amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)

# Using library from yoavaviram: https://github.com/yoavaviram/python-amazon-simple-product-api


# Test access
keyword='backpacking+test+lightweight'
products = amazon.search(Keywords=keyword, SearchIndex='all')
for i, product in enumerate(products):
	print "{0}. '{1}'".format(i, product.title)

# Export a finite list of responses -> top 10 for now
# Sort by reviews/price?
# Filter?

# Parse for price
# weight
# review weight
# number of reviews -> compute a weighted avg based on number of reviews?
# Repeat for a number of items

# Export for LP analysis
# minimize weight
# subject to budgetary constraints? or minimize cost and weight?
# ID categories (e.g., tents, backpacks) with best marginal benefits of $/weight saved