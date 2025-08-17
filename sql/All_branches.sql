-- Drop the old version of the combined table
DROP TABLE IF EXISTS all_branches;

-- Rebuild the table with everything from MD, DC, and VA
CREATE TABLE all_branches AS
SELECT * FROM md_branches
UNION ALL
SELECT * FROM dc_branches
UNION ALL
SELECT * FROM va_branches;

-- Add a branch_id column
ALTER TABLE all_branches ADD COLUMN branch_id INTEGER;

-- Fill it in using row numbers
UPDATE all_branches SET branch_id = ROWID;



-- Check row counts
SELECT COUNT(*) FROM all_branches;

SELECT COUNT(*) FROM dc_branches;
SELECT COUNT(*) FROM va_branches;
SELECT COUNT(*) FROM md_branches;


-- View sample rows
SELECT * FROM all_branches LIMIT 3;


-- Index for county
CREATE INDEX IF NOT EXISTS idx_county ON all_branches(county);

-- Index for bank name
CREATE INDEX IF NOT EXISTS idx_bank_name ON all_branches(bank_name);

-- Index for risk score
CREATE INDEX IF NOT EXISTS idx_risk_score ON all_branches(risk_score);


-- What is the total amount of bank deposits at branches with a risk score of 80 or more?($586,593,653)
SELECT
  SUM(deposit) AS total_deposits_in_high_risk_areas
FROM all_branches
WHERE risk_score >= 80;


--Which counties have the highest average risk scores, and in which state are they?
SELECT
  county,
  state,
  ROUND(AVG(risk_score), 2) AS avg_risk_score
FROM all_branches
GROUP BY county, state
ORDER BY avg_risk_score DESC
LIMIT 10;

--Which banks hold the most total deposits at branches with a risk score of 80 or more?
SELECT
  bank_name,
  SUM(deposit) AS total_deposits_in_risky_areas
FROM all_branches
WHERE risk_score >= 80
GROUP BY bank_name
ORDER BY total_deposits_in_risky_areas DESC
LIMIT 10;

--What is the average risk score for each county and state in the region?
SELECT
  county,
  state,
  ROUND(AVG(risk_score), 2) AS avg_risk_score
FROM all_branches
GROUP BY county, state
ORDER BY avg_risk_score DESC;

 




