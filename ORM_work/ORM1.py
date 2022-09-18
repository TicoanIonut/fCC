import pandas as pd
import sqlite3


database = sqlite3.connect('database.sqlite')
match_data = pd.read_sql_query("""select C.name as Country_name,
L.name as League_name,
M.season as Season,
M.date as Match_date,
home_team.team_long_name as Home_team_name,
away_team.team_long_name as Away_team_name,
M.Home_team_goal as home_team_goal,
M.away_team_goal as away_team_goal,
M.match_api_id as match_id
from Match M
INNER JOIN
Country as C ON
M.country_id = C.id
Inner join
League as L ON
M.league_id = L.id
left join
Team as home_team
on
home_team.team_api_id = M.home_team_api_id
left join
Team as away_team
on
away_team.team_api_id = M.away_team_api_id;""", database)
print(match_data.head(10))


