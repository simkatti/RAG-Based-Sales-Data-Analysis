import pandas as pd


def read_file():
    df = pd.read_csv(
        'data/Sample - Superstore.csv',
        usecols=[
            'Order ID',
            'Order Date',
            'Ship Date',
            'Customer ID',
            'Customer Name',
            'Segment',
            'Category',
            'Sub-Category',
            'Product Name',
            'Sales',
            'Quantity',
            'Discount',
            'Profit',
            'Region',
            'State',
            'City'],
        encoding='ISO-8859-1')
    return df


def write_document(data, filename):
    with open(filename, "w") as f:
        for line in data:
            f.write(line)
    return


def convert_rows(df):
    df = df.sort_values(by='Segment')
    strings = (
        df['Segment'] +
        ' ' +
        df['Customer Name'] +
        ' from ' +
        df['City'] +
        ", " +
        df['State'] +
        ", " +
        df['Region'] +
        ' ordered ' +
        df['Quantity'].astype(str) +
        ' pcs of ' +
        df['Product Name'] +
        ", " +
        df['Category'] +
        ", " +
        df['Sub-Category'] +
        ' for ' +
        df['Sales'].astype(str) +
        ' $, order was placed on ' +
        df['Order Date'].astype(str) +
        ' and shipped on ' +
        df['Ship Date'].astype(str) +
        ', ' +
        df['Segment'] +
        ' recieved ' +
        df['Discount'].astype(str) +
        ' $ discount, Company made ' +
        df['Profit'].astype(str) +
        ' $ profit. \n').tolist()

    return strings


def sales_over_time(df):
    df = df.sort_values(by='Order Date')
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    monthly_performance = df.groupby(df['Order Date'].dt.to_period('M'))[
        ['Sales', 'Profit']].sum()
    monthly_performance['Profit Margin'] = (
        monthly_performance['Profit'] / monthly_performance['Sales']) * 100

    yearly_performance = df.groupby(df['Order Date'].dt.to_period('Y'))[
        ['Sales', 'Profit']].sum()
    yearly_performance['Profit Margin'] = (
        yearly_performance['Profit'] / yearly_performance['Sales']) * 100

    result = []
    for year, month in monthly_performance.groupby(
            monthly_performance.index.year):
        for period, row in month.iterrows():
            result.append(
                f"In {period.to_timestamp().strftime('%B %Y')} company made {row['Sales'].round(2)} $ in sales and {row['Profit'].round(2)} $ in profit, having a profit margin of: {row['Profit Margin'].round(2)} %.\n"
            )
        year_row = yearly_performance.loc[str(year)]
        result.append(
            f"Annually in {year} company made {year_row['Sales'].round(2)} $ in sales and {year_row['Profit'].round(2)} $ in profit, having a profit margin of: {year_row['Profit Margin'].round(2)} %.\n"
        )

    return result


def category_performance(df):
    df = df.sort_values(by='Category')
    category = df.groupby(['Category', 'Sub-Category']
                          )[['Sales', 'Profit', 'Discount']].sum()
    category['Profit Margin'] = (category['Profit'] / category['Sales']) * 100
    max_category = category['Profit Margin'].idxmax()
    max_discout = category['Discount'].idxmax()
    category = category.round(2).reset_index()

    result = []
    for i, row in category.iterrows():
        result.append(
            f"Items in sub-category {row['Sub-Category']} (main category: {row['Category']}) made {row['Sales']} $ in sales and {row['Profit']} $ profit, while the total discount given was {row['Discount']} $, total profit margin: {row['Profit Margin']} % \n"
        )

    result.append(
        f"Items in sub-category {max_category[1]} (main category: {max_category[0]}) had highest profit margin of  {category['Profit Margin'].max().round(2)} % \n")
    result.append(
        f"Items in sub-category {max_discout[1]} (main category: {max_discout[0]}) had highest discount of {category['Discount'].max().round(2)} $")

    return result


def regional_performance(df):
    df = df.sort_values(by='Region')
    regional = df.groupby(['Region', 'State', 'City'])[
        ['Sales', 'Profit']].sum()
    regional['Profit Margin'] = (regional['Profit'] / regional['Sales']) * 100
    city_region = regional['Profit Margin'].idxmax()
    regional = regional.round(2).reset_index()

    region = df.groupby('Region')[['Sales', 'Profit']].sum()
    region['Profit Margin'] = (region['Profit'] / region['Sales']) * 100
    max_region = region['Profit Margin'].idxmax()

    result = []
    for i, row in regional.iterrows():
        result.append(
            f"City {row['City']} in state {row['State']} in region {row['Region']} made {row['Sales']} $ in sales resulting in {row['Profit']} $ profit with profit margin of {row['Profit Margin']} % \n"
        )
    result.append(
        f"Best performin region was {max_region} making total of {region['Sales']['West'].round(2)} $ sales and {region['Profit']['West'].round(2)} $ profit with profit margin of {region['Profit Margin'].max().round(2)} %")

    return result


def initialise():
    print("Reading file")
    df = read_file()
    print("Converting rows to text")
    row_data = convert_rows(df)
    print("Writing a document")
    write_document(row_data, "row_descriptions.txt")
    print("Performing sales analysis")
    sales_data = sales_over_time(df)
    print("Writing a document of annual sales analysis")
    write_document(sales_data, "trend_analysis.txt")
    print("Performin category analysis")
    cat_data = category_performance(df)
    print("Writing a document of category analysis")
    write_document(cat_data, "category_analysis.txt")
    print("Performing regional analysis")
    region_data = regional_performance(df)
    print("Writing a document")
    write_document(region_data, "region_analysis.txt")
    print("All done!")


# if __name__ == "__main__":
#     df = read_file()
#     initialise()
#     print(get_metadata())
