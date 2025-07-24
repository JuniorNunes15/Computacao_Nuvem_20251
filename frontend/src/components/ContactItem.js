import React from 'react';

const ContactItem = ({ contact, onDelete }) => {
  return (
    <div className="contact-item">
      <strong>{contact.nome}</strong>
      <p>Email: {contact.email}</p>
      <p>Telefone: {contact.telefone}</p>
      <button onClick={() => onDelete(contact.id)}>Excluir</button>
    </div>
  );
};

export default ContactItem;