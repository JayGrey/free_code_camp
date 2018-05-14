from random import randrange

from django.db import models

class QuoteManager(models.Manager):
    def random(self):
        query_set = super(QuoteManager, self).get_queryset()
        min_quote = query_set.earliest('id')
        max_quote = query_set.latest('id')
        random_row = randrange(min_quote.id, max_quote.id + 1)
        return query_set.get(id=random_row)


class Quote(models.Model):
    author =  models.CharField(max_length=64)
    text =  models.CharField(max_length=128)

    quotes = QuoteManager()
