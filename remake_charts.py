import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd

# Shared style 
plt.rcParams.update({
    'font.family': 'Georgia',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.spines.left': False,
    'figure.facecolor': '#f5f0e8',
    'axes.facecolor': '#f5f0e8',
})

INK = '#1a1208'
PAPER = '#f5f0e8'
ACCENT = '#c0392b'
MUTED = '#6b5e4a'

# Chart 1 — Regional median bar chart

regions = pd.DataFrame({
    'region': [
        'North America',
        'Europe & Central Asia',
        'Middle East & N. Africa',
        'East Asia & Pacific',
        'Latin America & Carib.',
        'South Asia',
        'Sub-Saharan Africa',
    ],
    'median': [95.6, 88.2, 89.9, 83.9, 72.0, 49.6, 33.0],
    'color': ['#2c3e50', '#2c3e50', '#2c3e50', '#2c3e50', '#2c3e50', '#2c3e50', '#2c3e50'],
}).sort_values('median', ascending=True)

fig, ax = plt.subplots(figsize=(8, 4.5))
fig.patch.set_facecolor(PAPER)

bars = ax.barh(regions['region'], regions['median'],
               color=regions['color'], height=0.6,
               alpha=0.88, edgecolor='none')

# Value labels
for bar, val in zip(bars, regions['median']):
    ax.text(val + 1.5, bar.get_y() + bar.get_height() / 2,
            f'{val}%', va='center', fontsize=9.5,
            color=bar.get_facecolor(), fontweight='bold')

ax.set_xlim(0, 115)
ax.set_xlabel('Internet penetration rate (%)', fontsize=9, color=MUTED)
ax.tick_params(axis='y', labelsize=10, color=INK)
ax.tick_params(axis='x', labelsize=9, color=MUTED)
ax.set_title('Median internet access by region, 2022',
             fontsize=13, fontweight='bold', color=INK, pad=12,
             fontfamily='Georgia')
ax.set_facecolor(PAPER)

plt.tight_layout()
plt.savefig('Internet/chart1_regional_medians.jpg', dpi=150, bbox_inches='tight',
            facecolor=PAPER)
plt.close()
print("✓ Saved chart1_regional_medians.jpg")


# CHART 2 — Sub-Saharan Africa detail

africa = pd.DataFrame({
    'country': [
        'South Africa', 'Seychelles', 'Nigeria', 'Ghana',
        'Senegal', 'Rwanda', 'Cameroon', 'Kenya',
        'Tanzania', 'Uganda', 'Mozambique', 'Ethiopia',
        'Mali', 'Chad', 'Guinea', 'Niger',
        'C. African Rep.', 'Eritrea',
    ],
    'pct': [72.35, 64.27, 55.40, 53.96, 46.14, 36.04, 36.46, 40.01,
            29.27, 26.18, 24.18, 24.46, 23.08, 21.48, 17.28, 16.67,
            14.93, 9.00],
}).sort_values('pct', ascending=True)

colors = [ACCENT if p <= 25 else '#8e6d40' for p in africa['pct']]

fig, ax = plt.subplots(figsize=(8, 6.5))
fig.patch.set_facecolor(PAPER)

bars = ax.barh(africa['country'], africa['pct'],
               color=colors, height=0.65, alpha=0.9)

# Value labels
for bar, val, color in zip(bars, africa['pct'], colors):
    ax.text(val + 0.8, bar.get_y() + bar.get_height() / 2,
            f'{val:.1f}%', va='center', fontsize=8.5,
            color=color, fontweight='bold')


plt.tight_layout()
plt.savefig('Internet/chart2_africa_detail.jpg', dpi=150, bbox_inches='tight',
            facecolor=PAPER)
plt.close()




# Chart 3 — Top 10 & Bottom 10


top10 = pd.DataFrame({
    'country': ['Saudi Arabia', 'UAE', 'Qatar', 'Bahrain', 'Kuwait',
                'Brunei', 'Monaco', 'Luxembourg', 'Denmark', 'Liechtenstein'],
    'pct': [100.0, 100.0, 100.0, 100.0, 99.84, 98.97, 98.38, 98.24, 97.86, 96.80],
}).sort_values('pct', ascending=False)

bottom10 = pd.DataFrame({
    'country': ['Eritrea', 'C. African Rep.', 'Niger', 'Guinea', 'Yemen',
                'Chad', 'Mozambique', 'Ethiopia', 'Pakistan', 'Tajikistan'],
    'pct': [9.00, 14.93, 16.67, 17.28, 17.69, 21.48, 24.18, 24.46, 32.95, 36.09],
}).sort_values('pct', ascending=True)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5.5),
                                 gridspec_kw={'wspace': 0.05})
fig.patch.set_facecolor(PAPER)

# LEFT: top 10
ax1.barh(top10['country'], top10['pct'], color='#2c3e50', height=0.65,
         alpha=0.87, edgecolor='none')
for i, (val, country) in enumerate(zip(top10['pct'], top10['country'])):
    ax1.text(val - 1, i, f'{val:.1f}%', va='center', ha='right',
             fontsize=8.5, color='white', fontweight='bold')
ax1.set_xlim(0, 112)
ax1.invert_xaxis()
ax1.set_title('TOP 10 — Highest access', fontsize=11, fontweight='bold',
              color='#2c3e50', pad=8)
ax1.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
ax1.tick_params(axis='y', labelsize=9.5)
ax1.tick_params(axis='x', labelsize=8.5)
ax1.spines['bottom'].set_color('#c8bba8')
ax1.set_facecolor(PAPER)
ax1.xaxis.grid(True, color='#c8bba8', linewidth=0.5, alpha=0.6)
ax1.set_axisbelow(True)
for spine in ['top', 'right', 'left']:
    ax1.spines[spine].set_visible(False)

# RIGHT: bottom 10
ax2.barh(bottom10['country'], bottom10['pct'], color=ACCENT, height=0.65,
         alpha=0.87, edgecolor='none')
for i, val in enumerate(bottom10['pct']):
    ax2.text(val + 0.5, i, f'{val:.1f}%', va='center',
             fontsize=8.5, color=ACCENT, fontweight='bold')
ax2.set_xlim(0, 55)
ax2.set_title('BOTTOM 10 — Lowest access', fontsize=11, fontweight='bold',
              color=ACCENT, pad=8)
ax2.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
ax2.tick_params(axis='y', labelsize=9.5)
ax2.tick_params(axis='x', labelsize=8.5)
ax2.spines['bottom'].set_color('#c8bba8')
ax2.set_facecolor(PAPER)
ax2.xaxis.grid(True, color='#c8bba8', linewidth=0.5, alpha=0.6)



plt.tight_layout()
plt.savefig('Internet/chart3_top_bottom.jpg', dpi=150, bbox_inches='tight',
            facecolor=PAPER)
plt.close()



