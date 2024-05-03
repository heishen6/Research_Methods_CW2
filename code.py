# Import necessary libraries
import pandas as pd
import plotly.express as px

file_path = 'Results_21Mar2022.csv'  # Make sure to update this with the actual path to your CSV file
data = pd.read_csv(file_path)

grouped_data = data.groupby(['diet_group', 'sex', 'age_group']).agg({
    'mean_ghgs': 'mean',  # Used for sizing: reflects greenhouse gas emissions
    'mean_land': 'mean',  # Used for coloring: reflects land use intensity
    'mean_watscar': 'mean',
    'mean_eut': 'mean',
    'n_participants': 'sum'
}).reset_index()


fig = px.treemap(grouped_data,
                 path=['diet_group', 'sex', 'age_group'],
                 values='mean_ghgs',
                 color='mean_land',
                 color_continuous_scale='RdYlGn_r',
                 hover_data={'mean_ghgs': True, 'mean_land': True,
                             'mean_watscar': True, 'mean_eut': True,
                             'n_participants': True}
                )

fig.update_layout(
    title='Environmental Impact of Different Diets Across Demographics'
)

fig.show()
fig.write_html('Environmental_Impact_Treemap.html')


