import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from common import class_abbreviations, data_folder

#Save the charts here
out_folder = '../charts'

resampling_methods = ['absolute', 'relative']

plt.rcParams["font.family"] = "Times New Roman"

for resampling_method in resampling_methods:
    src_file = (f'{data_folder}/corr_table_{resampling_method}.csv')
    
    df = pd.read_csv(filepath_or_buffer=src_file)
    
    #Drop the volume record
    df = df[df["Feature"].str.contains("IBSI:RNU0")==False]
    
    #Get the class names
    df['Class'] = df['Feature'].str.split('_').str[0]
    
    #Add the class abbreviation
    df['Class_abbrv'] = df['Class'].map(class_abbreviations)
    
    #Get the significant results
    df = df[df['Significant']]
    
    #---------- Create and save the plot -----------
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    
    #sns.boxplot(data=df, y='rho', x='Class_abbrv', hue='Class_abbrv', 
                #showfliers=False, boxprops={'alpha':0.4}, ax=ax,
                #legend=False)    
    
    sns.stripplot(data=df, y='rho', x='Class_abbrv', 
                  hue='Class_abbrv', jitter=0.1, 
                  linewidth=1, ax=ax, alpha=0.5, legend=False)
        
    
    ax.grid(visible=True, which='major', axis='y', linestyle='--',
            linewidth=0.5)
    
    ax.set_yticks(ticks=[-1.0, -0.9, -0.7, -0.4, -0.1, 
                          0.1,  0.4,  0.7,  0.9,  1.0])
    
    textprops = {'x':-0.3, 'va':'center', 'ha': 'left', 'alpha': 0.4}
    ax.text(y=-0.95, s='Very strong neg.', **textprops)
    ax.text(y=-0.80, s='Strong neg.', **textprops)
    ax.text(y=-0.55, s='Moderate neg.', **textprops)
    ax.text(y=-0.25, s='Weak neg.', **textprops)
    ax.text(y=0.0, s='Negligible', **textprops)
    ax.text(y=0.25, s='Weak pos.', **textprops)
    ax.text(y=0.55, s='Moderate pos.', **textprops)
    ax.text(y=0.80, s='Strong pos.', **textprops)
    ax.text(y=0.95, s='Very strong pos.', **textprops)
    
    ax.set_xlabel(xlabel=None)
    ax.set_ylabel(ylabel="Spearman's $\\rho$")
    ax.set_title(label=f'Resampling method: {resampling_method}',
                 fontsize=14)
    
    dst = f'{out_folder}/{resampling_method}-plot.png'
    fig.savefig(dst, dpi=300, bbox_inches='tight')
    
    #----------------------------------------------
    
    
    
    a = 0