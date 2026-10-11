import { useEffect, useState } from "react";
import api from "../api/axios";

const fields = {
  organizations: ["id", "name"],
  teams: ["id", "name", "short_name", "category", "age_group"],
  players: ["id", "person", "preferred_foot", "jersey_name"],
  matches: ["id", "home_team", "away_team", "kickoff", "status", "home_score", "away_score"],
};

const label = (key) => key.replaceAll("_", " ").replace(/\b\w/g, c => c.toUpperCase());
const value = (v) => v == null ? "—" : typeof v === "object" ? v.name || v.full_name || JSON.stringify(v) : String(v);

export default function ResourcePage({ type }) {
  const [rows, setRows] = useState([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get(`${type}/`)
      .then(({ data }) => setRows(Array.isArray(data) ? data : data.results || []))
      .catch(err => setError(err.response?.data?.detail || `Could not load ${type}.`))
      .finally(() => setLoading(false));
  }, [type]);

  const columns = fields[type];

  return (
    <section>
      <h1>{label(type)}</h1>
      {loading && <p>Loading...</p>}
      {error && <p className="error">{error}</p>}
      {!loading && !error && (
        rows.length ? (
          <div className="table-wrap">
            <table>
              <thead><tr>{columns.map(k => <th key={k}>{label(k)}</th>)}</tr></thead>
              <tbody>
                {rows.map((row, i) => (
                  <tr key={row.id ?? i}>
                    {columns.map(k => <td key={k}>{value(row[k])}</td>)}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : <p>No {type} found for your account.</p>
      )}
    </section>
  );
}