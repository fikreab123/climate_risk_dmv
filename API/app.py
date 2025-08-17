# make a website app using flask
from flask import Flask, jsonify, request
import sqlite3, os, sys

# start the app
app = Flask(__name__)
app.config.update(
    JSONIFY_PRETTYPRINT_REGULAR=True,
    JSON_SORT_KEYS=False
)
print("MARKER: STARTING app.py FROM:", __file__)
print("MARKER: CWD IS:", os.getcwd())

# path to our database
DATABASE = r"C:\Users\fikda\OneDrive\Desktop\climate_risk_dmv\sql\dmv_banks.db"
SQL_DIR  = r"C:\Users\fikda\OneDrive\Desktop\climate_risk_dmv\sql"
print("MARKER: DB PATH EXISTS?", os.path.exists(DATABASE))
print("MARKER: SQL DIR EXISTS?", os.path.exists(SQL_DIR))

# helper to run a query file
def run_query(sql_file):
    sql_path = os.path.join(SQL_DIR, sql_file)
    conn = sqlite3.connect(f"file:{DATABASE}?mode=ro", uri=True)
    cur = conn.cursor()
    query = open(sql_path, "r", encoding="utf-8").read()
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return rows

# route 1 - top 10 risky counties
@app.route('/top_10_risk_counties')
def top_10_risk_counties():
    rows = run_query('top_10_risk_counties.sql')
    data = [{"county": r[0], "state": r[1], "avg_risk": r[2]} for r in rows]
    return jsonify(data)

# route 2 - top banks in risky areas
@app.route('/top_banks_in_risky_areas')
def top_banks_in_risky_areas():
    rows = run_query('top_banks_in_risky_areas.sql')
    data = [{"bank_name": r[0], "total_deposits": f"${int(r[1]):,}"} for r in rows]
    return jsonify(data)

# route 3 - total deposits in high risk areas
@app.route('/total_deposits_high_risk')
def total_deposits_high_risk():
    rows = run_query('total_deposits_high_risk.sql')
    value = rows[0][0] if rows else 0
    formatted = f"${value:,.0f}"
    return jsonify([{"total_deposits": formatted}])

# route 4 - sample branches
@app.route('/branches_sample')
def branches_sample():
    limit = request.args.get('limit', default=25, type=int)
    limit = 1 if limit < 1 else (200 if limit > 200 else limit)

    conn = sqlite3.connect(f"file:{DATABASE}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    cur = conn.execute("SELECT * FROM all_branches LIMIT ?", (limit,))
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return jsonify(rows)

# route 0 - index
@app.route('/')
def index():
    return """
    <h1>Climate Risk API</h1>
    <ul>
      <li><a href="/top_10_risk_counties">Top 10 Risk Counties</a></li>
      <li><a href="/top_banks_in_risky_areas">Top Banks in Risky Areas</a></li>
      <li><a href="/total_deposits_high_risk">Total Deposits in High Risk Areas</a></li>
      <li><a href="/branches_sample">Sample Branches (add ?limit=50)</a></li>
    </ul>
    """

# run the app
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
