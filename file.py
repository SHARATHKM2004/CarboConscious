import pandas as pd

# Data for world champions
world_champions = {
    'Team': ['India', 'Australia', 'West Indies', 'Pakistan', 'Sri Lanka'],
    'ICC_rank': [2, 3, 7, 8, 4],
    'World_champions_Year': [2011, 2015, 1979, 1992, 1996],
    'Points': [874, 787, 753, 673, 855]
}

# Data for chokers
chokers = {
    'Team': ['South Africa', 'New Zealand', 'Zimbabwe'],
    'ICC_rank': [1, 5, 9],
    'Points': [895, 764, 656]
}

# Creating DataFrames
df1 = pd.DataFrame(world_champions)
df2 = pd.DataFrame(chokers)

# Concatenating DataFrames along columns (axis=1)
print(pd.concat([df1, df2], axis=1))