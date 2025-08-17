--Which banks hold the most total deposits at branches with a risk score of 80 or more?
SELECT
  bank_name,
  SUM(deposit) AS total_deposits_in_risky_areas
FROM all_branches
WHERE risk_score >= 80
GROUP BY bank_name
ORDER BY total_deposits_in_risky_areas DESC
LIMIT 10;