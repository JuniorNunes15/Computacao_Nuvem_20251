// src/App.js
import React from 'react';
import ContactList from './components/ContactList';
import './App.css';

function App() {
  return (
    <div className="app">
      <h1>Gerenciador de Contatos</h1>
      <ContactList />
    </div>
  );
}

export default App;