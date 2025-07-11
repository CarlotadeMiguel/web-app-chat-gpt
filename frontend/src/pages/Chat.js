import { useContext, useEffect, useState } from 'react';
import { AuthContext } from '../AuthContext';
import { sendMessage, getHistory } from '../api';

export default function Chat() {
  const { token, logout } = useContext(AuthContext);
  const [history, setHistory] = useState([]);
  const [input, setInput] = useState('');

  useEffect(() => {
    if (!token) return;
    getHistory(token).then(r => setHistory(r.data))
      .catch(e => console.error('Historial:', e.response?.data));
  }, [token]);

  const handleSend = async () => {
    if (!input) return;
    const res = await sendMessage(token, input);
    setHistory(h => [...h, { role: 'assistant', content: res.data.response }]);
    setInput('');
  };

  return (
    <div className="chat-container">
      <header className="chat-header">
        <h2>ChatGPT</h2>
        <button className="logout-btn" onClick={logout}>Cerrar sesión</button>
      </header>
      <div className="chat-window">
        {history.map((m, i) => (
          <div key={i} className={`msg ${m.role}`}>{m.content}</div>
        ))}
      </div>
      <div className="chat-input">
        <input
          value={input}
          onChange={e => setInput(e.target.value)}
          placeholder="Escribe tu mensaje..."
        />
        <button onClick={handleSend}>Enviar</button>
      </div>
    </div>
  );
}
