import pandas as pd

filename = 'out/chuchle.csv'

try:
    df_old = pd.read_csv(filename, index_col=0, parse_dates=[0])    
except OSError:
    df_old = pd.DataFrame()

df_new = pd.read_html('http://hydro.chmi.cz/hpps/popup_hpps_prfdyn.php?seq=307225', 'Teplota', header=0)[1]
df_new['Datum a čas'] = pd.to_datetime(df_new['Datum a čas'], dayfirst=True)
df_new = df_new.set_index('Datum a čas')

# df.to_csv(filename)
df = pd.concat([df_old, df_new])
df = df[~df.index.duplicated(keep='first')]
df = df.sort_index()
df.to_csv(filename)

## import matplotlib.pylab as plt
#ax = df.filter(like='Teplota').plot()
#fig = ax.get_figure()
#fig.savefig('out/chart.png')

