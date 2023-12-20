import React, {useEffect, useState} from "react"
import { Container } from "@mui/material"
import { OwnersCard } from "./OwnersCard"

export function Owners() {

   const [owners, setOwners] =useState([])

   useEffect( () => {
      fetch('/owners')
      .then( (resp) => {
         if (resp.ok) {
            resp.json().then(setOwners)
         } else{
            console.log('not logged in')
         }
      })
   },[])

   return (
    <>
      <Container maxWidth='lg'>
         {owners.map( owner => <OwnersCard key = {owner.id} owners = {owner} />)}
      </Container>
    </>
   
   
   )

}