// src/App.js
import React, { useContext } from 'react';
import { Routes, Route, Navigate, useLocation } from 'react-router-dom';
import { AuthContext } from './AuthContext';
import Login from './pages/Login';
import Chat from './pages/Chat';

// Componente para rutas protegidas
function PrivateRoute({ children }) {
  const { token } = useContext(AuthContext);
  const location = useLocation();

  return token
    ? children
    : <Navigate to="/login" state={{ from: location }} replace />;
}

export default function App() {
  const { token } = useContext(AuthContext);

  return (
    <Routes>
      {/* Ruta raíz: redirige según token */}
      <Route
        path="/"
        element={
          token
            ? <Navigate to="/chat" replace />
            : <Navigate to="/login" replace />
        }
      />

      {/* Login */}
      <Route path="/login" element={<Login />} />

      {/* Chat protegido */}
      <Route
        path="/chat"
        element={
          <PrivateRoute>
            <Chat />
          </PrivateRoute>
        }
      />

      {/* Cualquier otra ruta vuelve a "/" */}
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
}
