import { Button, TextField } from '@mui/material';
import{ useFormik } from "formik"
import * as yup from "yup"


function Signup() {

    const signUpSchema = yup.object().shape({
        username: yup.string()
        .min(6, 'Username must be 6 characters')
        .max(15, 'Username can not exceed 15 characters')
        .required('Required!'),
        email: yup.string()
        .email('Must be a valid email address')
        .required('Required!'),
        password: yup.string()
        .min(8, 'Password must be at least 8 characters.')
        .max(20, 'Password can not exceed 20 characters!')
        .required('Required!'),
    })

    const formik = useFormik({
        initialValues: {
            username: '',
            email: '',
            password: '',

        },
        validationSchema: signUpSchema,
        onSubmit: (values) => {
            console.log(values)
          fetch('/users', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(values)
          }).then((resp) => {
            if(resp.ok) {
                resp.json().then( (data) => console.log(data))
            } else {
                console.log('errors? handle them!')
            }
          })
        }
    })

    // console.log(formik.errors)


    return (

        <div>
            {/* {formik.errors} */}
            <form onSubmit={formik.handleSubmit}>
                <TextField 
                    id="username" 
                    label="Username" 
                    variant="outlined"
                    required
                    value={formik.values.username}
                    onChange={formik.handleChange}
                />
                
                <TextField 
                    id="email" 
                    label="Email"
                    variant="outlined"
                    required
                    value={formik.values.email}
                    onChange={formik.handleChange}
                />
            
                <TextField 
                    id="password" 
                    label="Password"
                    type='password'
                    variant="outlined"
                    required
                    value={formik.values.password}
                    onChange={formik.handleChange}
                />

                <Button 
                    variant="contained" type ="submit">Submit</Button>
            
            </form>

        </div>
    )
}

export default Signup;