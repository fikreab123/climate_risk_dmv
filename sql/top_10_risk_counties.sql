--Which counties have the highest average risk scores, and in which state are they?
SELECT
  county,
  state,
  ROUND(AVG(risk_score), 2) AS avg_risk_score
FROM all_branches
GROUP BY county, state
ORDER BY avg_risk_score DESC
LIMIT 10;