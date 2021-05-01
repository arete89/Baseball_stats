from pybaseball import playerid_lookup
from pybaseball import statcast_pitcher

playerid_lookup('ryu', 'hyun jin').key_mlbam
# Always use lowercase & last name goes first and then first name.
# His player ID is 547943. Let's make a DF based on this.
ryu_stats = statcast_pitcher('2019-04-01', '2019-09-01', 547943)
ryu_stats.head()
# Let's find out his fastest and slowest pitch speed.
ryu_stats.release_speed.sort_values()
# In case of exporting the data to Excel:
ryu_stats.to_excel(r'file location/MLB_Pitcher_Stats.xlsx', sheet_name = 'Ryu Hyun Jin', index = False)
