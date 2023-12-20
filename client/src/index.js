import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./index.css";
import './pages/Header.css'
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import { Owners } from "./pages/Owners";
import { Properties } from "./pages/Properties";
import { Tenants } from "./pages/Tenants";
import { Apartments } from "./pages/Apartments";
import { TenantForm } from "./pages/TenantForm";
import { UpdateTenantForm } from "./pages/UpdateTenantForm";
import { Signup } from "./pages/Signup";

const routes = [{
    path: '/',
    element: <App />,
    children: [
        {
            path: '/owners',
            element: <Owners />
        },
        {
            path: '/login',
            element: <Signup />
        },
        {
            path: "/owners/:ownerId/properties",
            element : <Properties />
        },
        {
            path: '/properties',
            element: <Properties />
        },
        {
            path: '/properties/<id>',
            element: <Properties />
        },
        {
            path: '/properties/:propertyId/apartments' ,
            element: <Apartments />
        },
        {
            path: '/apartments/:apartmentId/tenant',
            element: <Tenants />
        },
        {
            path: '/apartments/:apartmentId/addtenant',
            element: <TenantForm /> 
        },
        {
            path: `/tenants/:id/update`,
            element: <UpdateTenantForm />,
        },        
        {
            path: '/apartments',
            element: <Apartments />
        },
        {
            path: 'apartments/<id>',
            element: <Apartments />
        },
        {
            path: '/tenants',
            element: <Tenants />
        },
        {
            path: '/tenants/<id>',
            element: <Tenants />
        }
    ]
    },


]

const router = createBrowserRouter(routes)


const container = document.getElementById("root");
const root = createRoot(container);
root.render(<RouterProvider router = {router} />

    // <React.StrictMode>
    //     <BrowserRouter>
    //         <App />
    //     </BrowserRouter>
    // </React.StrictMode>

    );


