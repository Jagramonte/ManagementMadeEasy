import React, { useState } from "react";
import { useParams } from "react-router-dom";
import { useOutletContext } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import { PropertiesCard } from "./PropertiesCard";

export function TenantForm({ setShowAddForm }) {

  const [name, setName] = useState("");
  const [contactInfo, setContactInfo] = useState("");
  const params = useParams()
  const { selectedApartment, id } = useOutletContext()
  const navigate = useNavigate()


  console.log(selectedApartment)
  const handleSubmit = (e) => {
    e.preventDefault();

    fetch(`/tenants/${selectedApartment}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name, contact_info: contactInfo }),
    })
      .then((resp) => {
        console.log("Response:", resp);

        if (resp.ok) {
          return resp.json();
        } else {
          console.error("Failed to add tenant");
        }
      })
      .then((data) => {
        console.log("Data:", data);
        setName("");
        setContactInfo("");
        setShowAddForm(false)
      })
      .catch((error) => {
        console.error("Error:", error);
      });
    handleViewApartments()
  };

  const handleViewApartments = () => {
    navigate(`/properties/${id}/apartments`)
    navigate(0)
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Tenant Name:
        <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
      </label>
      <br />
      <label>
        Contact Info:
        <input type="text" value={contactInfo} onChange={(e) => setContactInfo(e.target.value)} />
      </label>
      <br />
      <button type="submit">Add Tenant</button>
    </form>
  );
}
