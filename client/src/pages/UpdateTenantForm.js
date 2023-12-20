import React, { useState, useEffect } from "react";
import { TenantForm } from "./TenantForm";
import { useNavigate } from "react-router-dom";
import { useOutletContext } from "react-router-dom";


export function UpdateTenantForm({  onUpdate, apartmentId}) {
  const [name, setName] = useState("");
  const [contactInfo, setContactInfo] = useState("");
  const navigate = useNavigate()
  const {tenant, setTenant} =useOutletContext()
  const tenantId = tenant ? tenant.id : ''
  console.log(tenant)
  useEffect(() => {
    setName(tenant.name);
    setContactInfo(tenant.contact_info);
  }, [tenant]);

  const handleSubmit = (e) => {
    e.preventDefault();

    fetch(`/tenants/${tenantId}/update`, 
    {method : 'PATCH', 
    body : JSON.stringify({name, contact_info:contactInfo}),
      headers: {"Content-Type" : 'application/json'}})
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
      <button type="submit">Update Tenant</button>
    </form>
  );
}
