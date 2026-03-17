import pandas as pd

def read_file():
    df = pd.read_csv('data/Sample - Superstore.csv', 
                     usecols=['Order ID','Order Date', 'Ship Date', 'Customer ID', 
                              'Customer Name', 'Segment', 'Category', 'Sub-Category',
                              'Product Name', 'Sales', 'Quantity', 'Discount', 'Profit',
                              'Region', 'State', 'City'], encoding='ISO-8859-1')
    return df

def convert_rows(df):
    strings = (
        df['Segment'] +' '+ df['Customer Name'] + ' from ' + df['City'] + ", " + df['State'] + ", " + df['Region'] + ' ordered ' + df['Quantity'].astype(str) + ' pcs of ' +
        df['Product Name'] + ", " + df['Category'] + ", " + df['Sub-Category'] + ' for ' + df['Sales'].astype(str) + ' $. Order was placed on ' +  df['Order Date'].astype(str) + ' and shipped on ' + df['Ship Date'].astype(str) +
        '. ' + df['Segment'] + ' recieved ' + df['Discount'].astype(str) + ' $ discount. Company made ' + df['Profit'].astype(str) + ' $ profit.'
    ).tolist()
    
    metadatas = df[['Order ID', 'Customer ID', 'Region', 'Category']].to_dict(orient='records')
    return strings,metadatas

def monthly_sales(df):
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    monthly_performance = df.groupby(df['Order Date'].dt.to_period('M'))[['Sales', 'Profit']].sum()
    monthly_performance['Profit Margin'] = (monthly_performance['Profit'] / monthly_performance['Sales']) * 100
    
    months = (
        "In " + monthly_performance.index.astype(str) + " company made " + monthly_performance['Sales'].astype(str) + " $ in sales and " + monthly_performance['Profit'].astype(str)+ " $ in profit. Profit margin: " + monthly_performance['Profit Margin'].astype(str)
    ).tolist()
    
    return months

def category_performance(df):
    category = df.groupby(df['Category'])[['Sales', 'Profit']].sum()
    category['Profit Margin'] = (category['Profit'] /category['Sales']) *100
    max_category = category['Profit Margin'].idxmax()
    
    categories = (
        "Items in category " + category.index.astype(str) + " made " + category['Sales'].astype(str) + " $ in sales and " + category['Profit'].astype(str) + " $ in profit. Profit Margin: " + category['Profit Margin'].astype(str)
    ).tolist()
    
    categories.append(f"category with highest profit margin: {max_category}")

    return categories

def regional_performance(df):
    regional = df.groupby(df['Region'])[['Sales', 'Profit']].sum()
    regional['Profit Margin'] = (regional['Profit'] / regional['Sales']) * 100
    max_region = regional['Profit Margin'].idxmax()
    
    cities = df.groupby(df['City'])[['Sales', 'Profit']].sum()
    cities['Profit Margin'] = (cities['Profit'] / cities['Sales']) * 100
    
    regions = (
        "Region " + regional.index.astype(str) + " made " + regional['Sales'].astype(str) + " $ in sales and " + regional['Profit'].astype(str) + " $  profit. Profit margin: " + regional['Profit Margin'].astype(str)
    ).tolist()
    
    regions.append(f"Region with the highest profit magin: {max_region}")
    
    cities_perfomance = (
        "City " + cities.index.astype(str) + " made " + cities['Sales'].astype(str) + " $ in sales and " + cities['Profit'].astype(str) + " $ profit. Profit margin: " + cities['Profit Margin'].astype(str)
    ).tolist()
    
    return regions, cities_perfomance

# if __name__ == "__main__":
#     df = read_file()
#     convert_rows(df)

    
    
