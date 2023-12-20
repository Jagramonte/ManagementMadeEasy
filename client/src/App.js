import React, { useState, useEffect } from "react";
import { Route, Routes, Link, Outlet, useNavigate } from "react-router-dom";
import { Button, Container } from "@mui/material"

import {Signup} from "./pages/Signup"
import {Properties} from "./pages/Properties"
import {Owners} from "./pages/Owners"
import {Tenants} from "./pages/Tenants"
import {Home} from "./pages/Home"
import {Header} from "./pages/Header"
import { Apartments } from "./pages/Apartments";

function App() {
  const [user, setUser] = useState(null)
  const navigate = useNavigate()

 const [selectedApartment, setSelectedApartment] = useState('')

 const [tenant, setTenant] = useState('')

 useEffect( () => {
  fetch('/authorized')
  .then((resp) => {
    if (resp.ok) {
      resp.json().then((user) => setUser(user))
    } else {
      navigate('/login')
    }
  })
},[])

 const context = {
   selectedApartment,
   setSelectedApartment,
   tenant,
   setTenant,
   user,
   setUser
 }

 return (
  <>
    {user&&
      <Container>
        <Header user={user} setUser={setUser}/>
      </Container>
    }

    <Container >

      <Home />
      <Outlet context = {context}/>

    </Container>
    
  </>
  
   )}
 


export default App;
