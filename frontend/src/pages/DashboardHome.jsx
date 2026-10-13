import { useEffect, useState } from "react";
import api from "../api/axios";

const resources = [
  ["Organizations", "organizations", "/organizations"],
  ["Teams", "teams", "/teams"],
  ["Players", "players", "/players"],
  ["Matches", "matches", "/matches"],
];

export default function DashboardHome({ user }) {
  const [counts, setCounts] = useState({});
  const [error, setError] = useState("");

  useEffect(() => {
    Promise.all(
      resources.map(async ([label, endpoint]) => {
        const { data } = await api.get(`${endpoint}/`);
        const rows = Array.isArray(data) ? data : data.results;
        return [label, data.count ?? rows?.length ?? 0];
      })
    )
      .then(results => setCounts(Object.fromEntries(results)))
      .catch(() => setError("Could not load all statistics. Check your API permissions."));
  }, []);

  return (
    <section>

      <h1>Dashboard</h1>
      <p>Welcome, {user.first_name || user.email}</p>
      {error && <p className="error">{error}</p>}
      <div className="cards">
        {resources.map(([label]) => (
          <article key={label}>
            <h3>{label}</h3>
            <p style={{ fontSize: 28, fontWeight: "bold" }}>
              {counts[label] ?? "—"}
            </p>
          </article>
        ))}
      </div>
      <h2>My Organizations</h2>
      {user.organizations.map(org => (
        <p key={org.id}>{org.name} — {org.role}</p>
      ))}
      {!user.organizations.length && <p>No organization membership found.</p>}

    </section>
  );
}