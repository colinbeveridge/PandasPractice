import pandas as pd
print(pd.__version__)
folder = 'KaggleFiles/'
books = pd.read_csv(folder+'books.csv')
print(type(books))
print(len(books))
print(books.shape)
print(books.columns)
print(books.info())
books = books[['title','authors','average_rating']]
print(books.head())
print(books.authors.value_counts())
print(books[books.authors == 'Stephen King'].head())
most_popular_books = books.average_rating.nlargest()
print(most_popular_books)
for axis_value in most_popular_books.axes:
    print(books.iloc[axis_value].title)

booksCollection = books[['title','authors','average_rating']]
booksCollection = booksCollection.set_index('title')
print(booksCollection.index)
print(booksCollection.nlargest(5,'average_rating').axes)