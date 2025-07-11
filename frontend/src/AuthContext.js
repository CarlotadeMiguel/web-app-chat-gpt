// src/AuthContext.js
import React, { createContext, useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

export const AuthContext = createContext();

export function AuthProvider({ children }) {
  const navigate = useNavigate();
  const [token, setToken] = useState(null);

  // Al montar, recupera token si existe
  useEffect(() => {
    const tok = localStorage.getItem('token');
    if (tok) {
      setToken(tok);
      navigate('/chat', { replace: true });
    }
  }, [navigate]);

  const login = tok => {
    localStorage.setItem('token', tok);
    setToken(tok);
    navigate('/chat', { replace: true });       
  };

  const logout = () => {
    localStorage.removeItem('token');
    setToken(null);
    navigate('/login', { replace: true });
  };

  return (
    <AuthContext.Provider value={{ token, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}
