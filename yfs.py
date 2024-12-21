from bs4 import BeautifulSoup
import pandas as pd

# HTML string (truncated for brevity in real implementation)
html_data = '''
<!-- Add your Yahoo Finance HTML content here -->
'''

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_data, 'html.parser')

# Extract the table
table = soup.find('table', {'class': 'table yf-j5d1ld noDl'})

# Extract headers and clean them
headers = [header.get_text(strip=True).replace('\n', ' ').replace('  ', '') for header in table.find_all('th')]

# Rename headers as per requirement
headers = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

# Extract table rows
rows = []
for row in table.find_all('tr')[1:]:  # Skip the header row
    cells = [cell.get_text(strip=True).replace(',', '') for cell in row.find_all('td')]
    if cells:  # Avoid appending empty rows
        rows.append(cells)

# Create DataFrame
data = pd.DataFrame(rows, columns=headers)

# Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'], format='%b %d %Y', errors='coerce')

# Convert numeric columns to appropriate types
data[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']] = data[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']].apply(pd.to_numeric, errors='coerce')

# Sort by date from oldest to latest
data = data.sort_values(by='Date')

# Save the DataFrame to a CSV file
data.to_csv('Stock.csv', index=False)

# Display success message
print("HTML table has been successfully converted and sorted by date to Stock.csv")
