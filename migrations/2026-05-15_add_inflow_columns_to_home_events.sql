ALTER TABLE home_events
ADD COLUMN utm_source VARCHAR(100) NULL AFTER page_path,
ADD COLUMN utm_medium VARCHAR(100) NULL AFTER utm_source,
ADD COLUMN referrer VARCHAR(2000) NULL AFTER utm_medium;
