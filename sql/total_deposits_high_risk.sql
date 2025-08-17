-- What is the total amount of bank deposits at branches with a risk score of 80 or more? 
SELECT
  SUM(deposit) AS total_deposits_in_high_risk_areas
FROM all_branches
WHERE risk_score >= 80;