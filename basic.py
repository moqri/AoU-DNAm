import pandas as pd
import matplotlib.pyplot as plt
import re

df = dataset_91684454_survey_df

l = [c for c in df['question'].value_counts().index if 'Disability: ' in c] + ['Living Situation: Stable House Concern']
counts = []
for q in l:
    value_counts = df[df['question'] == q]['answer'].value_counts()
    if len(value_counts) > 1:
        counts.append(value_counts.iloc[1])
    else:
        counts.append(0)
ind=[re.sub(r'\bDisability: \b', '', c) for c in l]
ind=[re.sub(r'\bLiving Situation: \b', '', c) for c in ind]

plot_df = pd.DataFrame({'Count': counts}, index=ind)

plot_df.index = [label.replace('Disabilit', 'Disability').replace(': ', ':\n') for label in plot_df.index]

plt.style.use('seaborn-v0_8-whitegrid')

fig, ax = plt.subplots(figsize=(8, 4 + len(l) * 0.3))
plot_df['Count'].plot(kind='bar', color='royalblue', edgecolor='black', ax=ax, width=0.7)

ax.set_title('Disabilities or Adversaries', fontsize=16, weight='bold', pad=15)
ax.set_xlabel('Question', fontsize=13)
ax.set_ylabel('Answer Count', fontsize=13)
ax.tick_params(axis='x', labelsize=11, rotation=25)
for label in ax.get_xticklabels():
    label.set_horizontalalignment('right')
ax.tick_params(axis='y', labelsize=12)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

for p in ax.patches:
    ax.annotate(
        f'{int(p.get_height())}',
        (p.get_x() + p.get_width() / 2, p.get_height()),
        ha='center', va='bottom', fontsize=11
    )

plt.tight_layout()
plt.show()
