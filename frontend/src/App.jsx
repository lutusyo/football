import { useEffect, useState } from "react";
import { BrowserRouter, NavLink, Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login";
import ResourcePage from "./pages/ResourcePage";
import { getMe, logout } from "./api/auth";
import "./style.css";

import DashboardHome from "./pages/DashboardHome";

function Dashboard({ user, onLogout }) {
  const links = [
    ["Dashboard", "/"],
    ["Organizations", "/organizations"],
    ["Teams", "/teams"],
    ["Players", "/players"],
    ["Matches", "/matches"],
  ];

  return (
    <div className="app">
      <aside className="sidebar">
        <h2>Football Platform</h2>
        <nav>{links.map(([name, path]) => (
          <NavLink end={path === "/"} key={path} to={path}>{name}</NavLink>
        ))}</nav>
        <button className="logout" onClick={onLogout}>Logout</button>
      </aside>
      <main className="content">
        
        <header className="topbar">
          <span>Football Management</span>
          <span>{user.first_name || user.email}</span>
        </header>

        <Routes>
          <Route path="/" element={<DashboardHome user={user} />} />
          <Route path="/organizations" element={<ResourcePage type="organizations" />} />
          <Route path="/teams" element={<ResourcePage type="teams" />} />
          <Route path="/players" element={<ResourcePage type="players" />} />
          <Route path="/matches" element={<ResourcePage type="matches" />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>

      </main>
    </div>
  );
}

export default function App() {
  const [user, setUser] = useState(null);
  const [checking, setChecking] = useState(true);

  useEffect(() => {
    if (!localStorage.getItem("access_token")) {
      setChecking(false);
      return;
    }
    getMe().then(setUser).catch(() => logout()).finally(() => setChecking(false));
  }, []);

  const handleLogout = () => {
    logout();
    setUser(null);
  };

  return (
    <BrowserRouter>
      {checking ? <p>Loading...</p> : user ? (
        <Dashboard user={user} onLogout={handleLogout} />
      ) : (
        <Login onLogin={setUser} />
      )}
    </BrowserRouter>
  );
}