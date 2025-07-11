import { useContext, useEffect, useState } from 'react';
import { AuthContext } from '../AuthContext';
import { sendMessage, getHistory } from '../api';

export default function Chat() {
  const { token } = useContext(AuthContext);
  const [history, setHistory] = useState([]);
  const [input, setInput] = useState('');

  useEffect(()=> {
    getHistory(token).then(r=>setHistory(r.data));
  }, [token]);

  const handleSend = async () => {
    if(!input) return;
    const res = await sendMessage(token, input);
    setHistory(h=>[...h, { role:'assistant', content:res.data.response }]);
    setInput('');
  };

  return (
    <div>
      <div className="chat-window">
        {history.map((m,i)=> (
          <div key={i} className={m.role}>{m.content}</div>
        ))}
      </div>
      <input value={input} onChange={e=>setInput(e.target.value)} />
      <button onClick={handleSend}>Enviar</button>
    </div>
  );
}
