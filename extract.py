from config import logging, DB_SERVER, DB_NAME, DB_USER, DB_PASSWORD, OUTPUT_DIR
from sqlalchemy import create_engine, text
from datetime import datetime
import urllib
import pandas as pd

logger = logging.getLogger(__file__)

password = urllib.parse.quote_plus(DB_PASSWORD)

conn_url = (
    f'mssql+pyodbc://{DB_USER}:{password}@{DB_SERVER}/{DB_NAME}'
    '?driver=ODBC+Driver+18+for+SQL+Server'
    '&TrustServerCertificate=yes'
    '&Encrypt=yes'
)

engine = create_engine(conn_url, echo=True)

try:
    logger.info('--- Start fetching data from database ---')

    with engine.connect() as conn:

        stmt = text('''
                SELECT
                    p.product_id,
                    p.product_category,
                    p.product_name,
                    p.product_price,
                    p.unit_of_measure,
                    p.minimum_stock_required,
                    p.is_active,
                    i.stock_date,
                    i.stock_available
                FROM 
                    Sales.Products p
                JOIN 
                    Sales.Inventory i
                ON  p.product_id = i.product_id
                WHERE 
                    p.minimum_stock_required > i.stock_available
                ''')
        
        df = pd.read_sql(stmt, conn, parse_dates=['stock_date'])

        if df.empty:
            logger.warning('⚠️ No products found with low stock. Process stopped.')

        else:
            logger.info(f'✅ Successfully fetched {len(df)} rows.')

        for col in df.select_dtypes(include=['string']):
            df[col] = df[col].str.strip()

        logger.info('✅ Transformation (stripping whitespace) done.')

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S %p')
        file_path = str(OUTPUT_DIR / f'Inventory Report_{timestamp}.xlsx')

        df.to_excel(file_path, index=False)
        logger.info(f'📦 Report exported successfully to: {file_path}')

        print(df)

except Exception:
    logger.exception('❌ An unexpected error occurred during the DB process')

