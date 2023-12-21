import React from "react";
import { Link } from "react-router-dom";
import {useState, useEffect} from "react"
import { Signup } from "./Signup";
import { Button, Container } from "@mui/material"
import { useNavigate } from "react-router-dom";
import './Header.css'


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
        <h1> Management Made Easy</h1>
        <div>
          <><Link to="/owners">Owners</Link></>
          <><Link to="/properties">Properties</Link></>
          <><Link to="/apartments">Apartments</Link></>
          <><Link to="/tenants">Tenants</Link></> 
          <Button variant = 'contained' onClick = {handleLogout} className="custombutton">Logout</Button> 
        </div>

     </nav>
    )
}

