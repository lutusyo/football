import { useState } from "react";
import { login, getMe } from "../api/auth";

export default function Login({ onLogin }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleLogin = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      await login(email, password);
      onLogin(await getMe());
    } catch (err) {
      setError(
        err.response?.data?.detail ||
        JSON.stringify(err.response?.data) ||
        "Could not connect to the server."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <main style={{ maxWidth: 380, margin: "80px auto", padding: 24 }}>
      <h1>Football Platform</h1>
      <p>Sign in to your account</p>
      <form onSubmit={handleLogin}>
        <input type="email" placeholder="Email" value={email}
          onChange={e => setEmail(e.target.value)} required />
        <br /><br />
        <input type="password" placeholder="Password" value={password}
          onChange={e => setPassword(e.target.value)} required />
        <br /><br />
        <button disabled={loading}>
          {loading ? "Signing in..." : "Login"}
        </button>
      </form>
      {error && <p style={{ color: "red" }}>{error}</p>}
    </main>
  );
}