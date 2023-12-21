import { Container } from "@mui/material"
import React, {useState, useEffect} from "react"
import { PropertiesCard } from "./PropertiesCard"
import styles from './Property.module.css'



export function Properties() {
    const [properties, setProperties] = useState([])

    useEffect( () => {
        fetch('/properties')
        .then( (resp) => {
            if (resp.ok) {
                resp.json().then(setProperties)
            } else {
                console.log('not logged in')
            }
        })
    },[])

    return (
        <>
            <Container maxWidth='lg' className={styles.cardcomponent}>
                {properties.map(property => <PropertiesCard key={property.id} properties={property}/>)}
            </Container>
        
        </>
    )
        
}