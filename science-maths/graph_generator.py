"""
Professional Graph Generator
Automatically selects and creates the best graph type for your data
Supports multiple professional styles: Academic, Presentation, Business

Usage:
    # Interactive mode
    python graph_generator.py
    
    # Programmatic usage
    from graph_generator import GraphGenerator
    generator = GraphGenerator(style='academic')
    generator.create_graph(data, title='My Graph')
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Union, Optional, Dict, List, Tuple
import warnings
from pathlib import Path
import json

warnings.filterwarnings('ignore')


class GraphGenerator:
    """
    Intelligent graph generator that automatically selects the best visualization
    type based on data characteristics and applies professional styling.
    
    Features:
    - Automatic graph type selection based on data analysis
    - Multiple professional styles (academic, presentation, business)
    - Works seamlessly with pandas DataFrames, Series, numpy arrays, and lists
    - Integrates with data analysis workflows
    """
    
    # Define professional style themes
    STYLES = {
        'academic': {
            'style': 'seaborn-v0_8-paper',
            'font_family': 'serif',
            'font_size': 11,
            'dpi': 300,
            'figure_size': (6, 4),
            'color_palette': 'Set2',
            'grid': True,
            'grid_alpha': 0.3,
            'spine_width': 1.5,
            'title_size': 14,
            'label_size': 12,
            'tick_size': 10,
            'legend_size': 10,
            'format': 'pdf'  # Preferred for academic papers
        },
        'presentation': {
            'style': 'seaborn-v0_8-whitegrid',
            'font_family': 'sans-serif',
            'font_size': 14,
            'dpi': 150,
            'figure_size': (10, 6),
            'color_palette': 'viridis',
            'grid': True,
            'grid_alpha': 0.2,
            'spine_width': 2,
            'title_size': 18,
            'label_size': 16,
            'tick_size': 14,
            'legend_size': 14,
            'format': 'png'  # Preferred for presentations
        },
        'business': {
            'style': 'seaborn-v0_8-darkgrid',
            'font_family': 'sans-serif',
            'font_size': 12,
            'dpi': 200,
            'figure_size': (8, 5),
            'color_palette': 'husl',
            'grid': True,
            'grid_alpha': 0.25,
            'spine_width': 1.5,
            'title_size': 16,
            'label_size': 14,
            'tick_size': 12,
            'legend_size': 12,
            'format': 'png'
        }
    }
    
    def __init__(self, style: str = 'academic'):
        """
        Initialise the graph generator with a specific style.
        
        Parameters:
        -----------
        style : str
            Style theme: 'academic', 'presentation', or 'business'
        """
        if style not in self.STYLES:
            raise ValueError(f"Style must be one of: {list(self.STYLES.keys())}")
        
        self.style = style
        self.style_config = self.STYLES[style]
        self._apply_style()
        
    def _apply_style(self):
        """Apply the selected style configuration to matplotlib."""
        plt.style.use(self.style_config['style'])
        plt.rcParams['font.family'] = self.style_config['font_family']
        plt.rcParams['font.size'] = self.style_config['font_size']
        plt.rcParams['figure.dpi'] = self.style_config['dpi']
        plt.rcParams['figure.figsize'] = self.style_config['figure_size']
        plt.rcParams['axes.grid'] = self.style_config['grid']
        plt.rcParams['grid.alpha'] = self.style_config['grid_alpha']
        plt.rcParams['axes.linewidth'] = self.style_config['spine_width']
        
    def _analyze_data(self, data: Union[pd.DataFrame, pd.Series, np.ndarray, List]) -> Dict:
        """
        Analyze data structure to determine the best graph type.
        
        Parameters:
        -----------
        data : DataFrame, Series, array, or list
            Input data to analyze
            
        Returns:
        --------
        tuple : (analysis dict, processed DataFrame)
        """
        analysis = {
            'data_type': None,
            'shape': None,
            'dtypes': None,
            'n_numeric': 0,
            'n_categorical': 0,
            'n_datetime': 0,
            'has_time_series': False,
            'recommended_graphs': []
        }
        
        # Convert to DataFrame if needed
        if isinstance(data, (list, np.ndarray)):
            if isinstance(data, list):
                data = np.array(data)
            if data.ndim == 1:
                data = pd.DataFrame({'value': data})
            else:
                data = pd.DataFrame(data)
        elif isinstance(data, pd.Series):
            data = data.to_frame()
        
        analysis['data_type'] = 'DataFrame'
        analysis['shape'] = data.shape
        analysis['dtypes'] = data.dtypes.to_dict()
        
        # Analyze columns
        for col in data.columns:
            dtype = str(data[col].dtype)
            
            if pd.api.types.is_numeric_dtype(data[col]):
                analysis['n_numeric'] += 1
            elif pd.api.types.is_datetime64_any_dtype(data[col]):
                analysis['n_datetime'] += 1
                analysis['has_time_series'] = True
            else:
                analysis['n_categorical'] += 1
        
        # Recommend graph types based on analysis
        n_cols = len(data.columns)
        n_rows = len(data)
        
        if analysis['has_time_series']:
            analysis['recommended_graphs'].append('line')
            analysis['recommended_graphs'].append('area')
        
        if analysis['n_categorical'] > 0 and analysis['n_numeric'] > 0:
            if n_cols == 2:
                analysis['recommended_graphs'].append('bar')
                analysis['recommended_graphs'].append('box')
                analysis['recommended_graphs'].append('violin')
            else:
                analysis['recommended_graphs'].append('bar')
                analysis['recommended_graphs'].append('heatmap')
        
        if analysis['n_numeric'] >= 2:
            analysis['recommended_graphs'].append('scatter')
            analysis['recommended_graphs'].append('regression')
        
        if analysis['n_numeric'] == 1 and n_cols == 1:
            analysis['recommended_graphs'].append('histogram')
            analysis['recommended_graphs'].append('density')
            analysis['recommended_graphs'].append('box')
        
        if n_cols > 2 and analysis['n_numeric'] > 1:
            analysis['recommended_graphs'].append('correlation')
            analysis['recommended_graphs'].append('pairplot')
        
        # Default to bar if no specific recommendations
        if not analysis['recommended_graphs']:
            analysis['recommended_graphs'] = ['bar', 'line']
        
        return analysis, data
    
    def _get_best_graph_type(self, analysis: Dict) -> str:
        """
        Select the best graph type from recommendations.
        
        Parameters:
        -----------
        analysis : dict
            Data analysis results
            
        Returns:
        --------
        str : Best graph type
        """
        # Priority order for graph types
        priority = ['line', 'scatter', 'bar', 'histogram', 'box', 'correlation', 
                   'heatmap', 'regression', 'density', 'violin', 'area', 'pairplot']
        
        for graph_type in priority:
            if graph_type in analysis['recommended_graphs']:
                return graph_type
        
        return 'bar'  # Default fallback
    
    def create_graph(self, 
                    data: Union[pd.DataFrame, pd.Series, np.ndarray, List],
                    graph_type: Optional[str] = None,
                    x: Optional[str] = None,
                    y: Optional[str] = None,
                    title: Optional[str] = None,
                    xlabel: Optional[str] = None,
                    ylabel: Optional[str] = None,
                    save_path: Optional[str] = None,
                    **kwargs) -> plt.Figure:
        """
        Create a professional graph with automatic type selection.
        
        Parameters:
        -----------
        data : DataFrame, Series, array, or list
            Data to visualize
        graph_type : str, optional
            Specific graph type to use. If None, automatically selects best type.
            Options: 'bar', 'line', 'scatter', 'histogram', 'box', 'violin',
                    'heatmap', 'correlation', 'regression', 'density', 'area', 'pairplot'
        x : str, optional
            Column name for x-axis
        y : str, optional
            Column name for y-axis
        title : str, optional
            Graph title
        xlabel : str, optional
            X-axis label
        ylabel : str, optional
            Y-axis label
        save_path : str, optional
            Path to save the figure
        **kwargs : additional arguments
            Additional arguments passed to specific graph creation methods
            
        Returns:
        --------
        matplotlib.figure.Figure : The created figure
        """
        # Analyze data
        analysis, df = self._analyze_data(data)
        
        # Auto-select graph type if not specified
        if graph_type is None:
            graph_type = self._get_best_graph_type(analysis)
        
        # Auto-select columns if not specified
        if x is None and len(df.columns) > 0:
            x = df.columns[0]
        if y is None and len(df.columns) > 1:
            y = df.columns[1]
        
        # Create the graph based on type
        fig, ax = plt.subplots(figsize=self.style_config['figure_size'])
        
        graph_methods = {
            'bar': self._create_bar,
            'line': self._create_line,
            'scatter': self._create_scatter,
            'histogram': self._create_histogram,
            'box': self._create_box,
            'violin': self._create_violin,
            'heatmap': self._create_heatmap,
            'correlation': self._create_correlation,
            'regression': self._create_regression,
            'density': self._create_density,
            'area': self._create_area,
            'pairplot': self._create_pairplot
        }
        
        if graph_type not in graph_methods:
            raise ValueError(f"Unknown graph type: {graph_type}. "
                           f"Available types: {list(graph_methods.keys())}")
        
        graph_methods[graph_type](ax, df, x, y, **kwargs)
        
        # Apply styling
        if title:
            ax.set_title(title, fontsize=self.style_config['title_size'], 
                        fontweight='bold', pad=15)
        if xlabel:
            ax.set_xlabel(xlabel, fontsize=self.style_config['label_size'], 
                         fontweight='bold')
        if ylabel:
            ax.set_ylabel(ylabel, fontsize=self.style_config['label_size'], 
                         fontweight='bold')
        
        ax.tick_params(labelsize=self.style_config['tick_size'])
        
        # Adjust layout
        plt.tight_layout()
        
        # Save if path provided
        if save_path:
            fig.savefig(save_path, format=self.style_config['format'], 
                       dpi=self.style_config['dpi'], bbox_inches='tight')
            print(f"Graph saved to: {save_path}")
        
        return fig
    
    def _create_bar(self, ax, df, x, y, **kwargs):
        """Create a bar chart."""
        if y and x:
            if pd.api.types.is_numeric_dtype(df[x]):
                # Group by x if numeric
                grouped = df.groupby(x)[y].mean() if y in df.columns else df.groupby(x).size()
                grouped.plot(kind='bar', ax=ax, color=sns.color_palette(self.style_config['color_palette']))
            else:
                # Categorical x-axis
                if y in df.columns:
                    df.plot(x=x, y=y, kind='bar', ax=ax, 
                           color=sns.color_palette(self.style_config['color_palette']))
                else:
                    df[x].value_counts().plot(kind='bar', ax=ax,
                                            color=sns.color_palette(self.style_config['color_palette']))
        else:
            # Single column
            df.iloc[:, 0].value_counts().plot(kind='bar', ax=ax,
                                             color=sns.color_palette(self.style_config['color_palette']))
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    
    def _create_line(self, ax, df, x, y, **kwargs):
        """Create a line chart."""
        if y and x:
            df.plot(x=x, y=y, kind='line', ax=ax, marker='o', linewidth=2,
                   color=sns.color_palette(self.style_config['color_palette'])[0])
        else:
            # Plot all numeric columns
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            for i, col in enumerate(numeric_cols):
                df[col].plot(ax=ax, marker='o', linewidth=2,
                           color=sns.color_palette(self.style_config['color_palette'])[i % 10],
                           label=col)
            if len(numeric_cols) > 1:
                ax.legend(fontsize=self.style_config['legend_size'])
    
    def _create_scatter(self, ax, df, x, y, **kwargs):
        """Create a scatter plot."""
        if y and x:
            ax.scatter(df[x], df[y], alpha=0.6, s=50,
                      c=sns.color_palette(self.style_config['color_palette'])[0])
        else:
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) >= 2:
                ax.scatter(df[numeric_cols[0]], df[numeric_cols[1]], alpha=0.6, s=50,
                          c=sns.color_palette(self.style_config['color_palette'])[0])
    
    def _create_histogram(self, ax, df, x, y, **kwargs):
        """Create a histogram."""
        if x and x in df.columns:
            data_to_plot = df[x]
        else:
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            data_to_plot = df[numeric_cols[0]] if len(numeric_cols) > 0 else df.iloc[:, 0]
        
        data_to_plot.hist(bins=30, ax=ax, alpha=0.7,
                         color=sns.color_palette(self.style_config['color_palette'])[0],
                         edgecolor='black', linewidth=1.2)
    
    def _create_box(self, ax, df, x, y, **kwargs):
        """Create a box plot."""
        if x and y:
            if x in df.columns and y in df.columns:
                df.boxplot(column=y, by=x, ax=ax)
            else:
                numeric_cols = df.select_dtypes(include=[np.number]).columns
                df[numeric_cols].boxplot(ax=ax)
        else:
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) > 0:
                df[numeric_cols].boxplot(ax=ax)
            else:
                df.iloc[:, 0].plot(kind='box', ax=ax)
    
    def _create_violin(self, ax, df, x, y, **kwargs):
        """Create a violin plot."""
        if x and y and x in df.columns and y in df.columns:
            sns.violinplot(data=df, x=x, y=y, ax=ax, palette=self.style_config['color_palette'])
        else:
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) > 0:
                sns.violinplot(data=df[numeric_cols], ax=ax, palette=self.style_config['color_palette'])
    
    def _create_heatmap(self, ax, df, x, y, **kwargs):
        """Create a heatmap."""
        if x and y:
            pivot = df.pivot_table(values=y, index=x, aggfunc='mean')
            sns.heatmap(pivot, annot=True, fmt='.2f', cmap='viridis', ax=ax, cbar_kws={'label': y})
        else:
            numeric_df = df.select_dtypes(include=[np.number])
            if len(numeric_df.columns) > 1:
                sns.heatmap(numeric_df.corr(), annot=True, fmt='.2f', cmap='coolwarm', 
                           center=0, ax=ax, square=True)
    
    def _create_correlation(self, ax, df, x, y, **kwargs):
        """Create a correlation heatmap."""
        numeric_df = df.select_dtypes(include=[np.number])
        if len(numeric_df.columns) > 1:
            corr = numeric_df.corr()
            sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0, 
                       ax=ax, square=True, cbar_kws={'label': 'Correlation'})
        else:
            raise ValueError("Need at least 2 numeric columns for correlation plot")
    
    def _create_regression(self, ax, df, x, y, **kwargs):
        """Create a regression plot."""
        if x and y and x in df.columns and y in df.columns:
            sns.regplot(data=df, x=x, y=y, ax=ax, 
                       color=sns.color_palette(self.style_config['color_palette'])[0])
        else:
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) >= 2:
                sns.regplot(data=df, x=numeric_cols[0], y=numeric_cols[1], ax=ax,
                           color=sns.color_palette(self.style_config['color_palette'])[0])
    
    def _create_density(self, ax, df, x, y, **kwargs):
        """Create a density plot."""
        if x and x in df.columns:
            data_to_plot = df[x]
        else:
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            data_to_plot = df[numeric_cols[0]] if len(numeric_cols) > 0 else df.iloc[:, 0]
        
        data_to_plot.plot(kind='density', ax=ax, linewidth=2,
                         color=sns.color_palette(self.style_config['color_palette'])[0])
        ax.fill_between(ax.lines[0].get_xdata(), 0, ax.lines[0].get_ydata(), alpha=0.3)
    
    def _create_area(self, ax, df, x, y, **kwargs):
        """Create an area chart."""
        if y and x:
            df.plot(x=x, y=y, kind='area', ax=ax, alpha=0.6,
                   color=sns.color_palette(self.style_config['color_palette'])[0])
        else:
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            df[numeric_cols].plot(kind='area', ax=ax, alpha=0.6,
                                color=sns.color_palette(self.style_config['color_palette']))
    
    def _create_pairplot(self, ax, df, x, y, **kwargs):
        """Create a pair plot (simplified version)."""
        numeric_df = df.select_dtypes(include=[np.number])
        if len(numeric_df.columns) >= 2:
            # Create a correlation plot as a simplified pairplot representation
            self._create_correlation(ax, df, x, y, **kwargs)
        else:
            raise ValueError("Need at least 2 numeric columns for pair plot")


def interactive_graph_creator():
    """
    Interactive function to create graphs with user input.
    Run this when executing the script directly.
    """
    print("=" * 60)
    print("Professional Graph Generator")
    print("=" * 60)
    print("\nAvailable styles:")
    print("1. Academic - For papers and publications (high DPI, PDF format)")
    print("2. Presentation - For slides and presentations (large fonts, PNG)")
    print("3. Business - For business reports (balanced style, PNG)")
    
    style_choice = input("\nSelect style (1-3) or press Enter for 'academic': ").strip()
    style_map = {'1': 'academic', '2': 'presentation', '3': 'business'}
    style = style_map.get(style_choice, 'academic')
    
    print(f"\nSelected style: {style}")
    print("\nData input options:")
    print("1. Load from CSV file")
    print("2. Enter data manually (simple example)")
    print("3. Use sample data")
    
    data_choice = input("\nSelect option (1-3) or press Enter for sample: ").strip()
    
    generator = GraphGenerator(style=style)
    
    if data_choice == '1':
        file_path = input("Enter CSV file path: ").strip()
        try:
            data = pd.read_csv(file_path)
            print(f"\nData loaded: {data.shape[0]} rows, {data.shape[1]} columns")
            print(f"Columns: {', '.join(data.columns)}")
        except Exception as e:
            print(f"Error loading file: {e}")
            return
    elif data_choice == '2':
        print("\nCreating sample data...")
        data = pd.DataFrame({
            'Category': ['A', 'B', 'C', 'D', 'E'],
            'Value': [23, 45, 56, 78, 32]
        })
    else:
        # Sample data
        np.random.seed(42)
        data = pd.DataFrame({
            'x': np.arange(1, 21),
            'y': np.random.randn(20).cumsum() + 10,
            'category': np.random.choice(['Group1', 'Group2', 'Group3'], 20)
        })
        print("\nUsing sample data")
    
    # Analyze and recommend
    analysis, _ = generator._analyze_data(data)
    best_type = generator._get_best_graph_type(analysis)
    
    print(f"\nData Analysis:")
    print(f"  Numeric columns: {analysis['n_numeric']}")
    print(f"  Categorical columns: {analysis['n_categorical']}")
    print(f"  Has time series: {analysis['has_time_series']}")
    print(f"  Recommended graph types: {', '.join(analysis['recommended_graphs'])}")
    print(f"  Best graph type: {best_type}")
    
    graph_type = input(f"\nEnter graph type (or press Enter for '{best_type}'): ").strip()
    if not graph_type:
        graph_type = best_type
    
    title = input("Enter title (or press Enter to skip): ").strip() or None
    x_col = input("Enter x-axis column name (or press Enter for auto): ").strip() or None
    y_col = input("Enter y-axis column name (or press Enter for auto): ").strip() or None
    
    save_path = input("Enter save path (or press Enter to display only): ").strip() or None
    
    # Create graph
    try:
        fig = generator.create_graph(
            data=data,
            graph_type=graph_type,
            x=x_col,
            y=y_col,
            title=title,
            save_path=save_path
        )
        plt.show()
        print("\nGraph created successfully!")
    except Exception as e:
        print(f"\nError creating graph: {e}")
        import traceback
        traceback.print_exc()


# Example usage functions for programmatic access
def example_usage():
    """
    Example usage demonstrating different graph types and styles.
    Uncomment and modify as needed for your data analysis workflow.
    """
    # Example 1: Simple bar chart with academic style
    print("Example 1: Academic bar chart")
    data1 = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D', 'E'],
        'Value': [23, 45, 56, 78, 32]
    })
    
    gen1 = GraphGenerator(style='academic')
    fig1 = gen1.create_graph(
        data1,
        graph_type='bar',
        x='Category',
        y='Value',
        title='Sample Bar Chart (Academic Style)',
        xlabel='Category',
        ylabel='Value',
        save_path='example_academic_bar.pdf'
    )
    print("Created: example_academic_bar.pdf\n")
    
    # Example 2: Time series line chart with presentation style
    print("Example 2: Presentation line chart")
    dates = pd.date_range('2023-01-01', periods=30, freq='D')
    data2 = pd.DataFrame({
        'Date': dates,
        'Sales': np.random.randn(30).cumsum() + 100,
        'Revenue': np.random.randn(30).cumsum() + 150
    })
    
    gen2 = GraphGenerator(style='presentation')
    fig2 = gen2.create_graph(
        data2,
        graph_type='line',
        x='Date',
        y='Sales',
        title='Sales Trend Over Time',
        xlabel='Date',
        ylabel='Sales',
        save_path='example_presentation_line.png'
    )
    print("Created: example_presentation_line.png\n")
    
    # Example 3: Automatic graph type selection
    print("Example 3: Automatic selection (histogram)")
    data3 = pd.Series(np.random.normal(100, 15, 1000))
    
    gen3 = GraphGenerator(style='academic')
    fig3 = gen3.create_graph(
        data3,
        title='Distribution of Values (Auto-selected: Histogram)',
        xlabel='Value',
        ylabel='Frequency',
        save_path='example_auto_histogram.pdf'
    )
    print("Created: example_auto_histogram.pdf\n")
    
    # Example 4: Correlation heatmap
    print("Example 4: Correlation heatmap")
    np.random.seed(42)
    data4 = pd.DataFrame({
        'Var1': np.random.randn(50),
        'Var2': np.random.randn(50),
        'Var3': np.random.randn(50),
        'Var4': np.random.randn(50)
    })
    
    gen4 = GraphGenerator(style='presentation')
    fig4 = gen4.create_graph(
        data4,
        graph_type='correlation',
        title='Variable Correlations',
        save_path='example_correlation.png'
    )
    print("Created: example_correlation.png\n")
    
    print("All examples completed!")


if __name__ == "__main__":
    # Run interactive mode by default
    interactive_graph_creator()
    
    # Uncomment to run examples instead:
    # example_usage()
