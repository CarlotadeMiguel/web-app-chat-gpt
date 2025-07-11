import { useState, useContext } from 'react';
import { login, register } from '../api';
import { AuthContext } from '../AuthContext';

function Login() {
  const { login: saveToken } = useContext(AuthContext);
  const [email, setEmail] = useState(''), [password, setPassword] = useState('');
  const [mode, setMode] = useState('login'); // or 'register'
  const handle = async () => {
    try {
      if (mode==='login') {
        const res = await login({ email, password });
        saveToken(res.data.access_token);
      } else {
        await register({ email, password });
        alert('Usuario creado');
        setMode('login');
      }
    } catch(e) { alert(e.response?.data.error || 'Error'); }
  };
  return (
    <div>
      <h2>{mode==='login'? 'Iniciar sesión' : 'Registro'}</h2>
      <input placeholder="Email" value={email} onChange={e=>setEmail(e.target.value)} />
      <input type="password" placeholder="Contraseña" value={password} onChange={e=>setPassword(e.target.value)} />
      <button onClick={handle}>{mode==='login'? 'Entrar' : 'Registrar'}</button>
      <button onClick={()=>setMode(mode==='login'?'register':'login')}>
        {mode==='login'? '¿Crear cuenta?' : '¿Ya tienes cuenta?'}
      </button>
    </div>
  );
}

export default Login;
