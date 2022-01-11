import pandas as pd
folder = 'KaggleFiles/'
file = 'wiki_movie_plots_deduped.csv'
movies = pd.read_csv(folder+file)

if __name__ == '__main__':
    # 1
    print(f'There are {len(movies)} movies in this dataset.')
    # 2
    print('Columns')
    print(movies.columns)
    # 3
    colnum = movies.shape[1]
    print(f'There are {colnum} columns in this dataset.')
    # 4
    print(movies.info())
    # 5
    length_to_exclude = len(movies) - 8
    print(movies[length_to_exclude:])
    # 6
    print(movies.tail(8))
    # 9
    print(movies.Genre.value_counts()[0:5])
    # 10
    print(movies.Director.value_counts()[0:5])
    # 11
    print(movies['Origin/Ethnicity'].value_counts())
    # 12
    print(movies.Title.value_counts())
    print('Yes, some titles are duplicated.')
    # 13
    print(movies['Release Year'].value_counts())