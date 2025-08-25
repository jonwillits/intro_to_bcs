import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
import numpy as np

def create_df_from_data_directory(data_directory):
    csv_files = glob.glob(os.path.join(data_directory, "*.csv"))
    df_list = []

    for file in csv_files:
        df = pd.read_csv(file)
        df_list.append(df)

    # Concatenate all DataFrames in the list into a single DataFrame
    df = pd.concat(df_list, ignore_index=True)

    # Now 'all_data' contains all the data from the CSV files
    df['condition_label'] = df['condition'].replace({1: 'old', 0: 'new'})
    df['response_label'] = df['response'].replace({1: 'old', 0: 'new'})

    return df


import numpy as np
import matplotlib.pyplot as plt
import os

def plot_means(df, dv, factor1, factor2=None, figure_type="bar"):
    """
    Plots the means of a dependent variable (dv) as a function of one or two factors (factor1, factor2).
    Allows for either a bar or line plot based on the 'figure_type' parameter.

    Args:
    df (pd.DataFrame): DataFrame containing the data.
    factor1 (str): The first factor (used for grouping).
    factor2 (str, optional): The second factor (used for x-axis or grouping within x-axis).
                            If None, only factor1 is used. Defaults to None.
    dv (str): The dependent variable to plot (y-axis).
    figure_type (str): Type of plot to create ('bar' or 'line'). Defaults to 'bar'.
    """
    # If factor2 is None, group by only factor1
    if factor2 is None:
        grouped_data = df.groupby(factor1)[dv].agg(['mean', 'sem']).reset_index()

        # Create the figure and axes for the plot
        fig, ax = plt.subplots(figsize=(8, 6))

        # Plot based on figure_type
        if figure_type == "bar":
            ax.bar(grouped_data[factor1], grouped_data['mean'], yerr=grouped_data['sem'], capsize=5)
            ax.set_xlabel(factor1.capitalize())
            ax.set_ylabel(f'Mean {dv.capitalize()}')

        elif figure_type == "line":
            ax.errorbar(grouped_data[factor1], grouped_data['mean'], yerr=grouped_data['sem'],
                        marker='o', linestyle='-', capsize=5)
            ax.set_xlabel(factor1.capitalize())
            ax.set_ylabel(f'Mean {dv.capitalize()}')

        # Set the title
        ax.set_title(f'Mean {dv.capitalize()} by {factor1.capitalize()}')

    else:
        # Group by both factors and calculate mean and standard error of the dependent variable
        grouped_data = df.groupby([factor1, factor2])[dv].agg(['mean', 'sem']).reset_index()

        # Create the figure and axes for the plot
        fig, ax = plt.subplots(figsize=(8, 6))

        # Extract the unique values of factor1 and factor2
        factor1_positions = grouped_data[factor1].unique()
        factor2_positions = grouped_data[factor2].unique()

        # If the figure_type is 'bar', generate a bar plot
        if figure_type == "bar":
            bar_width = 0.35  # Width of the bars
            index = np.arange(len(factor1_positions))  # X-axis positions for each group of bars

            # Loop over each level of factor2 and create the corresponding bars
            for i, condition in enumerate(factor2_positions):
                condition_data = grouped_data[grouped_data[factor2] == condition]
                ax.bar(index + i * bar_width, condition_data['mean'], bar_width,
                       label=str(condition).capitalize(), yerr=condition_data['sem'], capsize=5)

            # Set the x-ticks to be in the middle of the bars
            ax.set_xticks(index + bar_width / 2)
            ax.set_xticklabels(factor1_positions)

        # If the figure_type is 'line', generate a line plot
        elif figure_type == "line":
            # Loop over each level of factor1 to create a separate line
            for i, level1 in enumerate(factor1_positions):
                level1_data = grouped_data[grouped_data[factor1] == level1]
                ax.errorbar(factor2_positions, level1_data['mean'], yerr=level1_data['sem'],
                            label=str(level1).capitalize(), marker='o', linestyle='-', capsize=5)

            # Set the x-ticks to be the levels of factor2
            ax.set_xticks(np.arange(len(factor2_positions)))
            ax.set_xticklabels(factor2_positions)

        # Set the labels, title, and legend
        ax.set_xlabel(factor2.capitalize())
        ax.set_ylabel(f'Mean {dv.capitalize()}')
        ax.set_title(f'Mean {dv.capitalize()} by {factor1.capitalize()} and {factor2.capitalize()}')
        ax.legend(title=factor1.capitalize())

    # Show the plot
    plt.tight_layout()

    # Save the figure to the 'figures' folder
    if not os.path.exists("figures"):
        os.makedirs("figures")

    # Generate the filename by concatenating the arguments
    filename = f"{factor1}_{factor2}_{dv}_{figure_type}.png" if factor2 else f"{factor1}_{dv}_{figure_type}.png"
    file_path = os.path.join("figures", filename)

    # Save the figure
    plt.savefig(file_path)



def main():
    data_dir = './data'
    df = create_df_from_data_directory(data_dir)
    print(df)
    plot_means(df, "correct", "stimulus_type", "old_trial_number", "line")


if __name__ == '__main__':
    main()


