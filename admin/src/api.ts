export const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export function authFetch(url: string, options: RequestInit = {}) {
  const token = localStorage.getItem("token");
  const headers = new Headers(options.headers || {});
  if (token) headers.set("Authorization", `Bearer ${token}`);
  return fetch(url, { ...options, headers });
}

export const authProvider = {
  login: async ({ username, password }: any) => {
    const body = new URLSearchParams();
    body.set("username", username);
    body.set("password", password);

    const res = await fetch(`${API_URL}/auth/login`, {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body
    });

    if (!res.ok) throw new Error("Login inválido");
    const json = await res.json();
    localStorage.setItem("token", json.access_token);
  },
  logout: async () => { localStorage.removeItem("token"); },
  checkAuth: async () => {
    const t = localStorage.getItem("token");
    if (!t) throw new Error("not auth");
  },
  checkError: async () => Promise.resolve(),
  getPermissions: async () => Promise.resolve()
};
