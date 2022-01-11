# goodreads exercise
import pandas as pd

folder = 'KaggleFiles/'
books = pd.read_csv(folder+'books.csv')


books.isbn.fillna('0000000000',inplace=True)
print(type(books.isbn.iloc[1001]))

print(books[books.isbn13.isna()])


books.isbn13.fillna('0000000000000',inplace=True)
booksnew = books.isbn13.astype('string')

print(booksnew.info())
# for loop to convert isbn13 into dashed number
piece = ''
dash = '-'
# print(type(books.isbn13.iloc[1]))
# for count,num in enumerate(books.isbn13):
#     piece = num[0:3]
#     piece += dash
#     piece += num[3]
#     piece += dash
#     piece += num[4:9]
#     piece += dash
#     piece += num[9:12]
#     piece += dash
#     piece += num[-1]
#     books.isbn13.iloc[count]
# print(books.isbn13)


