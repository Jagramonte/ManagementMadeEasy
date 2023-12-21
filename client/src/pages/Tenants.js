import { Container } from "@mui/material"
import React, {useState, useEffect} from "react"
import {TenantsCard} from './TenantsCard'
import { useOutlet, useOutletContext } from "react-router-dom"
import styles from './Tenants.module.css'


export function Tenants() {
   const [tenants, setTenants] = useState([])
   // const { tenant, setTenants} =useOutletContext()

   useEffect( () => {
       fetch('/tenants')
       .then( (resp) => {
         if (resp.ok) {
            resp.json().then(setTenants)
          } else {
           console.log('not logged in')
          }
       })
   },[])
   return(
      <>
         <Container maxWidth='lg' className={styles.cardcomponent}>
            {tenants.map( tenant => <TenantsCard key={tenant.id} tenant={tenant}/>)}
         </Container>
      </>
   )
}


