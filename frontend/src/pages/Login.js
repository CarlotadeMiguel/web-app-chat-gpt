// src/pages/Login.js
import { useState, useContext } from 'react';
import { login as apiLogin, register as apiRegister } from '../api';
import { AuthContext } from '../AuthContext';

function Login() {
  const { login } = useContext(AuthContext);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [mode, setMode] = useState('login');

  const handle = async () => {
    try {
      if (mode === 'login') {
        const res = await apiLogin({ email, password });
        login(res.data.access_token);
      } else {
        if (password.length < 8) {
          return alert('La contraseña debe tener al menos 8 caracteres');
        }
        await apiRegister({ email, password });
        const loginRes = await apiLogin({ email, password });
        login(loginRes.data.access_token);
      }
    } catch (e) {
      console.error(e.response?.data);
      alert(e.response?.data.error || 'Error de autenticación');
    }
  };

  return (
    <div className="auth-container">
      <h2>{mode === 'login' ? 'Iniciar sesión' : 'Registro'}</h2>
      <form
        className="auth-form"
        onSubmit={e => { e.preventDefault(); handle(); }}
        autoComplete="off"
      >
        <input
          className="auth-input"
          type="email"
          placeholder="Email"
          value={email}
          onChange={e => setEmail(e.target.value)}
        />
        <input
          className="auth-input"
          type="password"
          placeholder="Contraseña"
          value={password}
          onChange={e => setPassword(e.target.value)}
        />
        <button className="auth-btn" type="submit">
          {mode === 'login' ? 'Entrar' : 'Registrar'}
        </button>
      </form>
      <button
        className="auth-toggle"
        onClick={() => setMode(mode === 'login' ? 'register' : 'login')}
      >
        {mode === 'login' ? '¿Crear cuenta?' : '¿Ya tienes cuenta?'}
      </button>
    </div>
  );
}

export default Login;
