import React, { useEffect, useState } from 'react';
import axios from 'axios';
import ContactForm from './ContactForm';
import ContactItem from './ContactItem';

const ContactList = () => {
  const [contacts, setContacts] = useState([]);

  useEffect(() => {
    fetchContacts();
  }, []);

  const fetchContacts = async () => {
    try {
      const response = await axios.get('http://ec2-54-209-75-88.compute-1.amazonaws.com/contatos');
      setContacts(response.data);
    } catch (error) {
      console.error('Erro ao carregar contatos:', error);
    }
  };

  const handleDelete = async (id) => {
    try {
      await axios.delete(`http://ec2-54-209-75-88.compute-1.amazonaws.com/contatos/${id}`);
      setContacts(contacts.filter(contact => contact.id !== id));
    } catch (error) {
      console.error('Erro ao excluir contato:', error);
    }
  };

  const addContact = (newContact) => {
    setContacts([...contacts, newContact]);
  };

  return (
    <div>
      <ContactForm onAddContact={addContact} />
      <div className="contact-list">
        {contacts.map(contact => (
          <ContactItem 
            key={contact.id} 
            contact={contact} 
            onDelete={handleDelete} 
          />
        ))}
      </div>
    </div>
  );
};

export default ContactList;
