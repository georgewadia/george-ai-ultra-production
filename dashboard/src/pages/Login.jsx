import { useState, useContext } from "react";

import { useNavigate } from "react-router-dom";

import API from "../services/api";

import { AuthContext }
from "../context/AuthContext";

export default function Login() {

  const navigate = useNavigate();

  const { login } =
    useContext(AuthContext);

  const [formData, setFormData] =
    useState({
      username: "",
      password: "",
    });

  const [loading, setLoading] =
    useState(false);

  const [error, setError] =
    useState("");

  const handleLogin = async (e) => {

    e.preventDefault();

    try {

      setLoading(true);

      setError("");

      const form = new FormData();

      form.append(
        "username",
        formData.username
      );

      form.append(
        "password",
        formData.password
      );

      const res = await API.post(
        "/auth/login",
        form
      );

      login(res.data.access_token);

      navigate("/");

    } catch (err) {

      setError(
        "Invalid username or password"
      );

    } finally {

      setLoading(false);
    }
  };

  return (

    <div className="min-h-screen flex items-center justify-center bg-gray-100">

      <div className="bg-white p-10 rounded-2xl shadow-xl w-full max-w-md">

        <h1 className="text-3xl font-bold mb-6 text-center">
          George AI Dashboard
        </h1>

        <form
          onSubmit={handleLogin}
          className="space-y-4"
        >

          <input
            type="text"
            placeholder="Username"
            className="w-full border p-3 rounded-lg"
            value={formData.username}
            onChange={(e) =>
              setFormData({
                ...formData,
                username: e.target.value,
              })
            }
          />

          <input
            type="password"
            placeholder="Password"
            className="w-full border p-3 rounded-lg"
            value={formData.password}
            onChange={(e) =>
              setFormData({
                ...formData,
                password: e.target.value,
              })
            }
          />

          {error && (

            <div className="text-red-500 text-sm">
              {error}
            </div>

          )}

          <button
            type="submit"
            disabled={loading}
            className="w-full bg-black text-white p-3 rounded-lg hover:bg-gray-800"
          >

            {loading
              ? "Loading..."
              : "Login"}

          </button>

        </form>

      </div>

    </div>
  );
}