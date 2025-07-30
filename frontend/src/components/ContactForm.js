import React, { useState } from 'react';
import axios from 'axios';

const ContactForm = ({ onAddContact }) => {
  const [contact, setContact] = useState({ nome: '', email: '', telefone: '' });

  const handleChange = (e) => {
    setContact({ ...contact, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http:localhost:5000/contatos', contact);
      onAddContact(response.data);
      setContact({ nome: '', email: '', telefone: '' });
    } catch (err) {
      console.error('Erro ao adicionar contato:', err);
    }
  };

  return (
    <form class="contact-form" onSubmit={handleSubmit}>
      <input name="nome" placeholder="Nome" value={contact.nome} onChange={handleChange} required />
      <input name="email" placeholder="Email" value={contact.email} onChange={handleChange} required />
      <input name="telefone" placeholder="Telefone" value={contact.telefone} onChange={handleChange} required />
      <button type="submit">Adicionar Contato</button>
    </form>
  );
};

export default ContactForm;
