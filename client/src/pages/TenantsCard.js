import React, { useState, useEffect } from "react";
import { Card, Button } from "@mui/material";
import { TenantForm } from "./TenantForm";
import { UpdateTenantForm } from "./UpdateTenantForm";
import { useNavigate } from "react-router-dom";
import { useOutletContext } from "react-router-dom";

export function TenantsCard(props) {
//   const { id, name, contact_info, apartmentId} = props.tenants;
  const navigate = useNavigate();
  const [showAddForm, setShowAddForm] = useState(false);
  const [showUpdateForm, setShowUpdateForm] = useState(false);
  const {tenant, setTenant} = useOutletContext()

//   console.log('tenantinfo', props.tenants)
//   const tenantId = `${props.tenants.id}`
//   useEffect(() => {
//     setTenantData({ name, contact_info });
//   }, [name, contact_info]);

  const handleUpdateTenant = () => {
    setShowUpdateForm(true);
    navigate(`/tenants/${props.tenant.id}/update`)
    setTenant(props.tenant)
  };
  
  useEffect(() => {
    if (showUpdateForm) {
      navigate(`/tenants/update/${tenant.id}`);
    }
  }, [showUpdateForm, navigate, tenant.id]);
  

  const handleDeleteTenant = () => {
    fetch(`/tenants/${props.tenant.id}`, { method: "DELETE" })
    .then(() => console.log('Delete successful'))
    .catch(error => console.error('Error deleting tenant:', error));
    // navigate(`/properties/${tenant.id}/apartments`);
    navigate(0)
  };

  return (
    <Card key={props.tenant.id}>
      <div>
        <p>Tenant Name: {props.tenant.name}</p>
        <p>Contact Info: {props.tenant.contact_info}</p>
        <Button onClick={handleUpdateTenant}>Update Tenant</Button>
        <Button onClick={handleDeleteTenant}>Delete Tenant</Button>

        {/* {showAddForm && <TenantForm  setShowAddForm={setShowAddForm} />} */}
        {/* {showUpdateForm && <UpdateTenantForm tenant={props.tenant} onUpdate={() => setShowUpdateForm(false)} />} */}
      </div>
    </Card>
  );
}
