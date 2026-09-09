from src.core.database import engine
from sqlalchemy import text

sql = '''
INSERT INTO forecasts (
    commodity, variety, data_source, etl_cadence, price_movement_wow, 
    forecast_date, forecast_price_low, forecast_price_high, generated_at
) VALUES
('Tomato', 'Native', 'DA-AMAD', 'Weekly', 2.5, '2026-09-01', 35.00, 50.00, NOW()),
('Tomato', 'Native', 'DA-AMAD', 'Weekly', 1.2, '2026-10-01', 40.00, 55.00, NOW()),
('Tomato', 'Native', 'DA-AMAD', 'Weekly', -0.8, '2026-11-01', 38.00, 52.00, NOW()),
('Squash fruit', 'Suprema', 'DA-AMAD', 'Weekly', 0.0, '2026-09-01', 25.00, 38.00, NOW()),
('Squash fruit', 'Suprema', 'DA-AMAD', 'Weekly', 3.1, '2026-10-01', 28.00, 42.00, NOW()),
('Squash fruit', 'Suprema', 'DA-AMAD', 'Weekly', 1.5, '2026-11-01', 30.00, 45.00, NOW()),
('Red Onion', 'Medium', 'DA-AMAD', 'Weekly', 5.0, '2026-09-01', 90.00, 130.00, NOW()),
('Red Onion', 'Medium', 'DA-AMAD', 'Weekly', 2.0, '2026-10-01', 95.00, 140.00, NOW()),
('White Onion', 'Imported', 'DA-AMAD', 'Weekly', -1.0, '2026-09-01', 85.00, 120.00, NOW()),
('White Onion', 'Imported', 'DA-AMAD', 'Weekly', 0.5, '2026-10-01', 88.00, 125.00, NOW());
'''

with engine.begin() as conn:
    conn.execute(text(sql))

print('Forecast data populated successfully!')
