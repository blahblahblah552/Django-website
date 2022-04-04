import datetime
from haystack import indexes
from catalog.models import Book, Author

class BookIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    summary = indexes.CharField(model_attr='summary')
#    genre = indexes.CharField(model_attr='genre')
#    pub_date = indexes.DateTimeField(model_attr='pub_date')


    def get_model(self):
        return Book

    def index_queryset(self, using=None):
        return self.get_model().objects

class AuthorIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='last_name')
    first_name = indexes.CharField(model_attr='first_name')
    last_name = indexes.CharField(model_attr='last_name')

    def get_model(self):
        return Author

    def index_queryset(self, using=None):
        return self.get_model().objects
    
