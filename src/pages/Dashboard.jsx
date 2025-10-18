import React, {useEffect, useState} from "react";
import { chatQuery } from "../services/api";

export default function Dashboard({tenant_id}) {
  const [events, setEvents] = useState([]);
  const [chatResp, setChatResp] = useState(null);

  useEffect(() => {
    const es = new EventSource("http://localhost:8000/events");
    es.onmessage = e => {
      try {
        const data = JSON.parse(e.data);
        setEvents(prev => [data, ...prev].slice(0,50));
      } catch(e){}
    };
    return () => es.close();
  }, []);

  async function pergunta(){
    const r = await chatQuery("quantas sacas de cimento tenho na obra X?", tenant_id);
    setChatResp(r);
  }

  return <div>
    <h2>Dashboard</h2>
    <button onClick={pergunta}>Perguntar ao sistema (exemplo)</button>
    {chatResp && <pre>{chatResp.text}</pre>}
    <h3>Últimos eventos</h3>
    <ul>
      {events.map((ev,i)=><li key={i}>{JSON.stringify(ev)}</li>)}
    </ul>
  </div>;
}
