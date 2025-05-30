import pandas as pd
import sqlite3
import logging
from ingestion_db import ingest_db


logging.basicConfig(
    filename = 'logs/get_vendor_summary.logs',
    level = logging.DEBUG,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    filemode = 'a'
)

def create_vendor_summary(conn):
    '''this function will merge the differnet tables to get the overall vendor summary and adding new columns in the resultant data'''
    vendor_sales_summary = pd.read_sql_query("""with FreightSummary as (
    Select 
        VendorNumber,
        Sum(Freight) as FreightCost
    from vendor_invoice
    group by VendorNumber
    ),
    PurchaseSummary as (
        Select
            p.VendorNumber,
            p.VendorName,
            p.Brand,
            p.Description,
            p.PurchasePrice,
            pp.Price as ActualPrice,
            pp.Volume,
            sum(p.Quantity) as TotalPurchaseQuantity,
            sum(p.Dollars) as TotalPurchaseDollars
        from purchases p
        join purchase_prices pp
            on p.Brand = pp.Brand
        where p.PurchasePrice>0
        group by p.VendorNumber, p.Brand, p.Description, p.PurchasePrice, pp.Price, pp.Volume    
    ),
    SalesSummary as (
        Select
            VendorNo,
            Brand,
            Sum(SalesDollars) as TotalSalesDollars,
            Sum(SalesPrice) as TotalSalesPrice,
            Sum(SalesQuantity) as TotalSalesQuantity,
            Sum(ExciseTax) as TotalExciseTax
            from sales
            group by VendorNo, Brand
    )
    Select 
        ps.VendorNumber,
        ps.VendorName,
        ps.Description,
        ps.PurchasePrice,
        ps.ActualPrice,
        ps.Volume,
        ps.TotalPurchaseQuantity,
        ps.TotalPurchaseDollars,
        ss.TotalSalesQuantity,
        ss.TotalSalesDollars,
        ss.TotalExciseTax,
        fs.FreightCost
    from PurchaseSummary ps
    left join SalesSummary ss
        on ps.Brand=ss.Brand
    left join FreightSummary fs
        on ps.VendorNumber = fs.VendorNumber
    order by ps.TotalPurchaseDollars Desc
    """,conn)

    return vendor_sales_summary

def clean_data(df):
    '''this function will clean the data'''
    # change datatype to float
    vendor_sales_summary['Volume'] = vendor_sales_summary['Volume'].astype('float64')

    # filling missing value with 0
    vendor_sales_summary.fillna(0, inplace=True)

    # triming extra spaces
    vendor_sales_summary['VendorName'] = vendor_sales_summary['VendorName'].str.strip()
    vendor_sales_summary['Description'] = vendor_sales_summary['Description'].str.strip()

    # Creating new columns
    vendor_sales_summary['GrossProfit'] = vendor_sales_summary['TotalSalesDollars'] - vendor_sales_summary['TotalPurchaseDollars']
    vendor_sales_summary['ProfitMargin'] = (vendor_sales_summary['GrossProfit']/vendor_sales_summary['TotalSalesDollars'])*100
    vendor_sales_summary['StockTurnover'] = vendor_sales_summary['TotalSalesQuantity']/vendor_sales_summary['TotalPurchaseQuantity']
    vendor_sales_summary['SalesPurchaseRatio'] = vendor_sales_summary['TotalSalesDollars']/vendor_sales_summary['TotalPurchaseDollars']

    return df


if __name__ = "__main__"
    conn = sqlite3.connect("inventory.db")

    logging.info("Creating Vendor Summary Table....")
    summary_df = create_vendor_summary(conn)
    logging.info(summary_df.head())

    logging.info("Clean Data....")
    clean_df = clean_data(conn)
    logging.info(clean_df.head())    

    logging.info("Ingesting Data....")
    ingest_db(clean_df, 'vendor_sales_summary', conn)
    logging.info("completed")

