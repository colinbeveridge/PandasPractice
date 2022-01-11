import pandas as pd

folder = 'KaggleFiles/'
file = 'chefmozaccepts.csv'

cuisines = pd.read_csv(folder+'chefmozcuisine.csv')
ratings = pd.read_csv(folder+'ratings.csv')
merged_ratings = ratings.merge(cuisines,how='inner',on='placeID')
merged_ratings.groupby([''])
payment_methods = pd.read_csv(folder+file)


