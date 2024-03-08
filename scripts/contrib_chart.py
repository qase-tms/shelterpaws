"""Simple Python script, that receives data from GitHub-API and creates a picture with chart of Contributors
doc: https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-repository-contributors--parameters"""

import io

import requests
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import seaborn as sns
import pandas as pd
from PIL import Image
import numpy as np

# use your credentials
from credentials import GIT_HUB_TOKEN

Y_TICKS_STEP = 5

url = ' https://api.github.com/repos/qase-tms/shelterpaws/contributors'
"""Lists contributors to the specified repository and sorts them by the number of commits per contributor in 
descending order"""

headers = {'Accept': 'application/vnd.github+json',
           'Authorization': f'Bearer {GIT_HUB_TOKEN}',
           'X-GitHub-Api-Version': '2022-11-28'}

parameters = {
    'anon': 'false'  # Set to '1' or 'true' to include anonymous contributors in results.
}

response = requests.get(url, headers=headers, params=parameters)

assert response.status_code == 200, f'Check github doc, code :{response}'

# use resize for same picture size
avatars = [np.array(Image.open(io.BytesIO(requests.get(contributor['avatar_url']).content)).resize((600, 600)))
           for contributor in response.json()]

data = {"contributor": [contributor['login'] for contributor in response.json()],
        "contributions": [contributor['contributions'] for contributor in response.json()]}

df = pd.DataFrame(data)

# make it a little prettier :)
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
plt.rc('font', family='monospace', size=16)
plt.xlabel(' ')  # remove x-line label
plt.grid(False)
plt.gca().set_yticks([i for i in range(response.json()[0]['contributions']) if i % Y_TICKS_STEP == 0 and i != 0])
for spine in plt.gca().spines.values():  # remove edges
    spine.set_visible(False)

# create chart
chart = sns.barplot(x="contributor", y="contributions", data=df, color='#382C56')

# add avatars to chart
for i, contr_img in enumerate(avatars):
    image = OffsetImage(contr_img, zoom=0.1)
    AB = AnnotationBbox(image,
                        (chart.patches[i].get_x() + chart.patches[i].get_width() / 2,
                         chart.patches[i].get_y() + chart.patches[i].get_height()),
                        frameon=False)
    plt.gca().add_artist(AB)

plt.savefig("../assets/contrib_chart.png", transparent=True)
