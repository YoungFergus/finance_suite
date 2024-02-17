CREATE TABLE IF NOT EXISTS investment (
    investment_id INTEGER PRIMARY KEY AUTOINCREMENT
    , investment_symbol TEXT
    , created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    , updated_date TIMESTAMP
);