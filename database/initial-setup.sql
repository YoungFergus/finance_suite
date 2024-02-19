CREATE TABLE IF NOT EXISTS investment (
    investment_id INTEGER PRIMARY KEY AUTOINCREMENT
    , ticker TEXT
    , created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    , updated_date TIMESTAMP
);

CREATE TABLE IF NOT EXISTS transactions (
    unique_id TEXT -- Unique_Id
    , ticker TEXT -- Symbol
    , position_date DATE -- Date
    , action TEXT -- Action
    , quantity NUMERIC -- Quantity
    , price NUMERIC -- Price
    , fees NUMERIC -- Fees & Comm
);

