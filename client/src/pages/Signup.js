import React from 'react';
import { useState} from 'react'
import { Button, TextField, Box, Container } from '@mui/material';
import{ useFormik } from "formik"
import * as yup from "yup"
import { useOutletContext } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';


export function Signup( ) {

    const [ signup, setSignup ] = useState(true)
    const {user, setUser} = useOutletContext()
    const navigate = useNavigate()

    const signUpSchema = yup.object().shape({
        username: yup.string().min(6, 'Username must be 6 characters').max(15, 'Username can not exceed 15 characters').required('Required!'),
        email: yup.string().email('Must be a valid email address').required('Required!'),
        password: yup.string().min(8, 'Password must be at least 8 characters.').max(20, 'Password can not exceed 20 characters!').required('Required!')
    })

    const loginSchema = yup.object().shape({
        username: yup.string().required('username required'),
        password: yup.string().required('password required')
    })

    const formik = useFormik({
        initialValues: {
            username: '',
            email: '',
            password: '',

        },
        validationSchema: signup ? signUpSchema : loginSchema,
        onSubmit: (values) => {
            const endpoint = signup ? '/users' : '/login'
          fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(values)
          }).then((resp) => {
            if(resp.ok) {
                resp.json().then( ({user}) => {
                    setUser(user)
                    navigate('/owners')
                }).catch((error) => {
                    console.error('Fetch error', error)
                })
                
                
            } else {
                console.log('errors? handle them!')
                resp.json().then((data) => console.log(data))
                
            }
          })
        }
    })

    function toggleSignup() {
        setSignup((currentSignup) => !currentSignup)
    }

 

    // console.log(formik.values)
    return (

        <Container maxwidth='sm'className='container'>

            <div className='title'>
                <h3> Management Starts With MME</h3>
            </div>
            <Button onClick = {toggleSignup}>{signup ? 'Login instead' : 'Register for an account'}</Button>
            <form onSubmit={formik.handleSubmit} className='form'>
                <TextField 
                    id="username" 
                    label="Username" 
                    variant="outlined"
                    error={!!formik.errors.username}
                    helperText={formik.errors.username}
                    required
                    value={formik.values.username}
                    onChange={formik.handleChange}
                />
                <Box>
                    {signup && <TextField 
                        id="email" 
                        label="Email"
                        variant="outlined"
                        error={!!formik.errors.email}
                        helperText={formik.errors.email}
                        required
                        value={formik.values.email}
                        onChange={formik.handleChange}
                    />}
                </Box>
                <Box>
                    <TextField 
                        id="password" 
                        label="Password"
                        type='password'
                        variant="outlined"
                        error={!!formik.errors.password}
                        helperText={formik.errors.password}
                        required
                        value={formik.values.password}
                        onChange={formik.handleChange}
                    />
                </Box>

                <Button 
                    variant="contained" type ="submit">Submit</Button>
            
            </form>
        </Container>
    )
}
