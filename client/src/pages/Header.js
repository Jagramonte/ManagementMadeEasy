import React from "react";
import { Link } from "react-router-dom";
import {useState, useEffect} from "react"
import { Signup } from "./Signup";
import { Button, Container } from "@mui/material"
import { useNavigate } from "react-router-dom";


export function Header({setUser}) {
 
  const navigate = useNavigate()

 function handleLogout() {
  fetch('/logout', {
    method: 'DELETE'
  }).then((resp) => {
    if (resp.ok) {
      setUser(null)
      navigate('/login')
    }
  })
 }

 
 
    return (
    <nav className = 'header'>
        <h1> Managment Made Easy</h1>
          
        <><Link to="/">Home</Link></>
        <><Link to="/owners">Owners</Link></>
        <><Link to="/properties">Properties</Link></>
        <><Link to="/apartments">Apartments</Link></>
        <><Link to="/tenants">Tenants</Link></> 
        <Button variant = 'contained' onClick = {handleLogout}>Logout</Button> 
     </nav>
    )
}

