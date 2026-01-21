import numpy as np
import matplotlib.pyplot as plt

# Create a figure with multiple subplots
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('NumPy Data Visualization Examples', fontsize=16, fontweight='bold')

# 1. Line Plot - Sine and Cosine waves
ax1 = axes[0, 0]
x = np.linspace(0, 2*np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)
ax1.plot(x, y_sin, label='sin(x)', linewidth=2)
ax1.plot(x, y_cos, label='cos(x)', linewidth=2)
ax1.set_title('Sine and Cosine Waves')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.legend()
ax1.grid(True, alpha=0.3)

# 2. Bar Chart - Random data
ax2 = axes[0, 1]
categories = ['A', 'B', 'C', 'D', 'E']
values = np.random.randint(10, 100, 5)
colors = np.random.rand(5, 3)  # Random RGB colors
ax2.bar(categories, values, color=colors)
ax2.set_title('Bar Chart - Random Values')
ax2.set_ylabel('Values')
for i, v in enumerate(values):
    ax2.text(i, v + 2, str(v), ha='center')

# 3. Histogram - Normal Distribution
ax3 = axes[0, 2]
data = np.random.normal(loc=100, scale=15, size=1000)
ax3.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
ax3.set_title('Histogram - Normal Distribution')
ax3.set_xlabel('Values')
ax3.set_ylabel('Frequency')
ax3.axvline(np.mean(data), color='red', linestyle='--', linewidth=2, label=f'Mean: {np.mean(data):.1f}')
ax3.legend()

# 4. Scatter Plot - Random points
ax4 = axes[1, 0]
x_scatter = np.random.randn(100)
y_scatter = np.random.randn(100)
sizes = np.random.randint(20, 200, 100)
colors_scatter = np.random.rand(100)
scatter = ax4.scatter(x_scatter, y_scatter, s=sizes, c=colors_scatter, cmap='viridis', alpha=0.6)
ax4.set_title('Scatter Plot - Random Points')
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
plt.colorbar(scatter, ax=ax4)

# 5. Pie Chart - Distribution
ax5 = axes[1, 1]
sizes_pie = np.array([30, 25, 20, 15, 10])
labels_pie = ['Category A', 'Category B', 'Category C', 'Category D', 'Others']
colors_pie = plt.cm.Set3(np.linspace(0, 1, len(sizes_pie)))
wedges, texts, autotexts = ax5.pie(sizes_pie, labels=labels_pie, autopct='%1.1f%%',
                                     colors=colors_pie, startangle=90)
ax5.set_title('Pie Chart - Data Distribution')
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontweight('bold')

# 6. 3D Surface Plot data (2D heatmap)
ax6 = axes[1, 2]
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))
heatmap = ax6.contourf(X, Y, Z, levels=20, cmap='twilight')
ax6.set_title('Contour Plot - 2D Surface')
ax6.set_xlabel('X')
ax6.set_ylabel('Y')
plt.colorbar(heatmap, ax=ax6, label='Z values')

plt.tight_layout()
plt.show()
