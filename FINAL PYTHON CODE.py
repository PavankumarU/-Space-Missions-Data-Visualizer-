import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Print current working directory for debugging
print(f"Current working directory: {os.getcwd()}")

# Load the dataset with encoding handling
print("Loading dataset...")
try:
    # First attempt with 'ISO-8859-1' encoding (Latin-1) which is more permissive
    file_path = '/Users/uppupavankumar/Documents/12308667/space_missions.csv'
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    print(f"Successfully loaded dataset with ISO-8859-1 encoding.")
except Exception as e:
    print(f"Error with ISO-8859-1 encoding: {e}")
    try:
        # Second attempt with 'latin1' encoding
        df = pd.read_csv(file_path, encoding='latin1')
        print(f"Successfully loaded dataset with latin1 encoding.")
    except Exception as e:
        print(f"Error with latin1 encoding: {e}")
        try:
            # Third attempt with error handling
            df = pd.read_csv(file_path, encoding='utf-8', errors='replace')
            print(f"Successfully loaded dataset with utf-8 and error replacement.")
        except Exception as e:
            print(f"Failed to load the dataset: {e}")
            # If all attempts fail, exit the script
            print("Please check the file path and format.")
            exit(1)

# Clean column names
df.columns = df.columns.str.strip()

# Display basic structure
print(f"Shape of the dataset: {df.shape}")

# Display data types of each column
print("\nData types:")
print(df.dtypes)

# Preview the first five rows
print("\nFirst 5 Rows:")
print(df.head())

# Check for duplicate records
duplicate_count = df.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicate_count}")

# Check for missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Visualize missing data using a heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Values Heatmap', fontsize=14)
plt.tight_layout()
plt.savefig('missing_values_heatmap.png')
plt.close()

# Data cleaning
# Drop rows with missing values (optional, based on requirement)
df_cleaned = df.dropna()
print(f"\nShape after removing missing values: {df_cleaned.shape}")

# VISUALIZATION 1: Top Companies by Number of Launches
# Use the original dataframe to keep all data
plt.figure(figsize=(12, 7))
top_companies = df['Company'].value_counts().head(10)
sns.barplot(x=top_companies.values, y=top_companies.index, palette='coolwarm')
plt.title("Top 10 Most Active Space Organizations", fontsize=16)
plt.xlabel("Number of Launches", fontsize=12)
plt.ylabel("Company Name", fontsize=12)
plt.tight_layout()
plt.savefig('top_companies.png')
plt.close()

# VISUALIZATION 2: Mission Status Distribution
# Pie Chart
if 'MissionStatus' in df.columns:
    plt.figure(figsize=(9, 9))
    status_counts = df['MissionStatus'].value_counts()
    colors = ['#2ecc71', '#e74c3c', '#f1c40f', '#95a5a6']  # Green, red, yellow, gray
    plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.title("Mission Outcome Distribution (Pie Chart)", fontsize=14)
    plt.axis('equal')  # Equal aspect ratio ensures the pie is circular
    plt.tight_layout()
    plt.savefig('mission_status_pie.png')
    plt.close()

    # Bar Plot for Mission Status
    plt.figure(figsize=(10, 6))
    sns.barplot(x=status_counts.index, y=status_counts.values, palette='pastel')
    plt.title("Mission Outcome Distribution (Bar Plot)", fontsize=14)
    plt.xlabel("Mission Status")
    plt.ylabel("Number of Missions")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('mission_status_bar.png')
    plt.close()
else:
    print("'MissionStatus' column not found in the dataset")

# VISUALIZATION 3: Year-wise Launch Frequency
# Convert 'Date' column to datetime if it exists
if 'Date' in df.columns:
    try:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        # Extract the year from the 'Date' column
        df['Year'] = df['Date'].dt.year
        
        # Count number of launches per year
        launches_per_year = df['Year'].value_counts().sort_index()
        
        # Line plot
        plt.figure(figsize=(14, 7))
        sns.lineplot(x=launches_per_year.index, y=launches_per_year.values, marker='o', linewidth=2.5, color='#3498db')
        plt.title("🚀 Year-wise Space Launch Frequency", fontsize=16)
        plt.xlabel("Year", fontsize=12)
        plt.ylabel("Number of Launches", fontsize=12)
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('yearly_launches.png')
        plt.close()
    except Exception as e:
        print(f"Error processing date column: {e}")
else:
    print("'Date' column not found in the dataset")

# VISUALIZATION 4: Mission Success Rate by Company (for top companies)
if 'MissionStatus' in df.columns and 'Company' in df.columns:
    # Filter for successful missions - adapt these based on your actual data values
    # Print unique values to help with debugging
    print("\nUnique mission status values:")
    print(df['MissionStatus'].unique())
    
    # Try to determine success status values based on what's in the data
    success_status = ['Success', 'Successful']
    # Add variations that might exist in the data
    for status in df['MissionStatus'].unique():
        if isinstance(status, str) and ('success' in status.lower() or 'succeed' in status.lower()):
            success_status.append(status)
    
    # Remove duplicates
    success_status = list(set(success_status))
    print(f"Using these values as success indicators: {success_status}")
    
    # Function to determine if a mission was successful
    def is_successful(status):
        if pd.isna(status):
            return False
        return any(success.lower() in str(status).lower() for success in success_status)
    
    # Apply the function to create a new column
    df['IsSuccessful'] = df['MissionStatus'].apply(is_successful)
    
    # Get top 8 companies by number of launches
    top_8_companies = df['Company'].value_counts().head(8).index
    
    # Filter the dataframe for these companies
    top_companies_df = df[df['Company'].isin(top_8_companies)]
    
    # Group by company and calculate success rate
    success_rate = top_companies_df.groupby('Company')['IsSuccessful'].mean().sort_values(ascending=False)
    
    # Plot
    plt.figure(figsize=(12, 7))
    sns.barplot(x=success_rate.values, y=success_rate.index, palette='viridis')
    plt.title("Success Rate by Space Organization", fontsize=16)
    plt.xlabel("Success Rate", fontsize=12)
    plt.ylabel("Company", fontsize=12)
    plt.xlim(0, 1)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('success_rate_by_company.png')
    plt.close()

# VISUALIZATION 5: Rocket Usage Frequency (if applicable)
if 'Rocket' in df.columns:
    top_rockets = df['Rocket'].value_counts().head(10)
    
    plt.figure(figsize=(12, 7))
    sns.barplot(x=top_rockets.values, y=top_rockets.index, palette='magma')
    plt.title("Top 10 Most Used Rockets", fontsize=16)
    plt.xlabel("Number of Launches", fontsize=12)
    plt.ylabel("Rocket Name", fontsize=12)
    plt.tight_layout()
    plt.savefig('top_rockets.png')
    plt.close()
else:
    print("'Rocket' column not found in the dataset")

print("Analysis complete! Visualization images saved.")
