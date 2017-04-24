
# coding: utf-8

# In[73]:

import pandas as pd
star_wars = pd.read_csv("star_wars.csv", encoding="ISO-8859-1")

star_wars.head(2)


# In[74]:

star_wars = star_wars[pd.notnull(star_wars["RespondentID"])]
star_wars.head(2)


# In[75]:

yes_no = {
    "Yes": True,
    "No": False
}
for col in [
    "Have you seen any of the 6 films in the Star Wars franchise?",
    "Do you consider yourself to be a fan of the Star Wars film franchise?"
    ]:
    star_wars[col] = star_wars[col].map(yes_no)

star_wars["Do you consider yourself to be a fan of the Star Wars film franchise?"].value_counts()


# In[76]:

import numpy as np

movie_mapping = {
    "Star Wars: Episode I  The Phantom Menace": True,
    np.nan: False,
    "Star Wars: Episode II  Attack of the Clones": True,
    "Star Wars: Episode III  Revenge of the Sith": True,
    "Star Wars: Episode IV  A New Hope": True,
    "Star Wars: Episode V The Empire Strikes Back": True,
    "Star Wars: Episode VI Return of the Jedi": True
}

for col in star_wars.columns[3:9]:
    star_wars[col] = star_wars[col].map(movie_mapping)


# In[77]:

star_wars = star_wars.rename(columns={
    "Which of the following Star Wars films have you seen? Please select all that apply.": "Episode I  The Phantom Menace - seen", 
    "Unnamed: 4": "Episode II  Attack of the Clones - seen",
    "Unnamed: 5": "Episode III  Revenge of the Sith - seen",
    "Unnamed: 6": "Episode IV  A New Hope - seen",
    "Unnamed: 7": "Episode V The Empire Strikes Back - seen",
    "Unnamed: 8": "Episode VI Return of the Jedi - seen"
})

star_wars.head()
    


# In[78]:

star_wars[star_wars.columns[9:15]] = star_wars[star_wars.columns[9:15]].astype(float)
star_wars = star_wars.rename(columns={
    "Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.": "Episode I  The Phantom Menace - ranked", 
    "Unnamed: 10": "Episode II  Attack of the Clones - ranked",
    "Unnamed: 11": "Episode III  Revenge of the Sith - ranked",
    "Unnamed: 12": "Episode IV  A New Hope - ranked",
    "Unnamed: 13": "Episode V The Empire Strikes Back - ranked",
    "Unnamed: 14": "Episode VI Return of the Jedi - ranked"
})

star_wars.ix[1:5,9:15]


# In[79]:

star_wars[star_wars.columns[9:15]] = star_wars[star_wars.columns[9:15]].astype(float)
star_wars[star_wars.columns[9:15]].mean()


# In[80]:

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt

plt.bar(range(6), star_wars[star_wars.columns[9:15]].mean())


# # Originals are better, Revenge of the Sith is the worst?
# 
# The Empire Strikes Back is generally considered by the sample to be the best Star Wars film. This is congruous with FiveThirtyEight's original question. Surprisingly, Revenge of the Sith is generally assessed as being the worst of the films.

# In[81]:

star_wars[star_wars.columns[3:9]].sum()


# In[82]:

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt

plt.bar(range(6), star_wars[star_wars.columns[3:9]].sum())


# # Most Seen Findings
# It appears that the original movies were seen by more respondents than the newer movies. This reinforces what we saw in the rankings, where the earlier movies seem to be more popular.

# In[83]:

males = star_wars[star_wars["Gender"] == "Male"]
females = star_wars[star_wars["Gender"] == "Female"]


# In[84]:

males[males.columns[9:15]] = males[males.columns[9:15]].astype(float)
males[males.columns[9:15]].mean()


# In[85]:

females[females.columns[9:15]] = females[females.columns[9:15]].astype(float)
females[females.columns[9:15]].mean()


# # Star Wars Film Preferences by Sex
# 
# While male respondents are generally dismissive of the prequels, female respondents express belief of a significant drop-off within the prequel trilogy, with Revenge of the Sith by far being the least popular.
# 
# Female viewers had a averaged preferred ranking of Episode 1 to the original film, which is heresy.

# In[ ]:



