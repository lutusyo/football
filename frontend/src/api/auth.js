import api from "./axios";

export const login = async (email, password) => {
  const { data } = await api.post("auth/login/", { email, password });
  localStorage.setItem("access_token", data.access);
  localStorage.setItem("refresh_token", data.refresh);
  return data;
};

export const getMe = async () => (await api.get("auth/me/")).data;

export const logout = () => {
  localStorage.removeItem("access_token");
  localStorage.removeItem("refresh_token");
};