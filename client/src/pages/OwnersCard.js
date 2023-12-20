// import { Card, Button } from "@mui/material";
// import { useOutletContext } from "react-router-dom";

// export function OwnersCard(props) {
//     const {Owners} = useOutletContext()
//     const {id, name, contact_info} = props.owners

//     return (
        
//         <Card key={id}>
//             <div>
//                 <p>Owner Name : {name}</p>
//                 <p>Owner Contact Info : {contact_info}</p>
//                 <Button href="#text-buttons" >Properties</Button>
//                 <Button href="#text-buttons">Delete Owner</Button>
//             </div>
//         </Card>
//     )
// }
// OwnersCard.js

import React from "react";
import { Card, Button } from "@mui/material";
import { useHistory } from "react-router-dom";
import { useNavigate } from "react-router-dom";

export function OwnersCard(props) {
    const { id, name, contact_info } = props.owners;
    const navigate = useNavigate();

    const handleViewProperties = () => {
        navigate(`/owners/${id}/properties`);
    };

    return (
        <Card key={id}>
            <div>
                <p>Owner Name: {name}</p>
                <p>Owner Contact Info: {contact_info}</p>
                <Button onClick={handleViewProperties}>Properties</Button>
                {/* <Button >Delete Owner</Button> */}
            </div>
        </Card>
    );
}
