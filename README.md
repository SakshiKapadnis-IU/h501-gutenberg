# h501-gutenberg: Week 4 Coding Exercise

## Overview
A Python project demonstrating proper use of modules, pandas for data manipulation, and Seaborn for data visualization. This repository serves as a template for organized data science work following PEP-8 style guidelines.

## Project Structure

```
h501-gutenberg/
├── gutenberg.ipynb              # Main Jupyter notebook with exercises
├── data_utils/                  # Data manipulation module
│   └── __init__.py             # Contains data loading, cleaning, and aggregation functions
├── visualization/               # Data visualization module
│   └── __init__.py             # Contains Seaborn-based plotting functions
├── README.md                    # This file
└── .gitignore                   # Git configuration
```

## Features

### Data Utilities Module (`data_utils`)
- `load_data()` - Load CSV files into pandas DataFrames
- `clean_data()` - Remove duplicates and handle missing values
- `summarize_data()` - Generate summary statistics
- `filter_data()` - Filter DataFrames by column values
- `aggregate_data()` - Group and aggregate data
- `create_sample_data()` - Generate synthetic datasets for testing

### Visualization Module (`visualization`)
- `setup_style()` - Configure Seaborn styling
- `plot_distribution()` - Histogram with KDE plots
- `plot_scatter()` - Scatter plots with color encoding
- `plot_boxplot()` - Box plots for distribution by category
- `plot_heatmap()` - Correlation heatmaps
- `plot_categorical()` - Categorical count plots

## Installation

### Prerequisites
- Python 3.9+
- pip or conda

### Setup
```bash
# Clone the repository
git clone https://github.com/SakshiKapadnis-IU/h501-gutenberg.git
cd h501-gutenberg

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install ipykernel pandas seaborn numpy matplotlib jupyter
```

## Usage

### Running the Jupyter Notebook
```bash
jupyter notebook gutenberg.ipynb
```

### Using the Modules
```python
from data_utils import create_sample_data, clean_data, aggregate_data
from visualization import setup_style, plot_scatter

# Create and clean data
df = create_sample_data(n_rows=100)
df_clean = clean_data(df)

# Create visualizations
setup_style()
plot_scatter(df_clean, x='value', y='count', hue='category')
```

## Code Standards

### PEP-8 Compliance
- ✓ Function and variable names use `snake_case`
- ✓ Line length limited to 79 characters
- ✓ 4-space indentation throughout
- ✓ Comprehensive docstrings with Parameters, Returns, and Examples
- ✓ Proper spacing around operators and after commas
- ✓ Clear module-level documentation

### Best Practices
- **Modularity**: Code organized into focused, reusable modules
- **Documentation**: Every function includes detailed docstrings
- **Error Handling**: Input validation and meaningful error messages
- **Single Responsibility**: Each function has one clear purpose
- **Import Organization**: Stdlib → third-party → local imports

## Learning Outcomes

This project demonstrates:
1. **Python Modules**: How to organize code into reusable modules
2. **GitHub Repositories**: Proper repository structure and version control
3. **pandas**: Data loading, cleaning, manipulation, and aggregation
4. **Seaborn**: Professional data visualization techniques
5. **PEP-8**: Professional Python coding standards

## Requirements

- `ipykernel` (3.0+) - For Jupyter kernel support
- `pandas` (1.3+) - For data manipulation
- `seaborn` (0.11+) - For statistical visualization
- `numpy` - For numerical operations
- `matplotlib` - For plotting backend

## Author
Created for H501: Introduction to Data Science (Indiana University)

## License
Educational use only
