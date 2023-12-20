import { Card } from "@mui/material";
import { useOutletContext, useNavigate } from "react-router-dom";
import { Link,Button } from '@mui/material';

export function PropertiesCard(props) {
    const { id, address, total_apts, owner_name} = props.properties
    const navigate = useNavigate();


    const handleViewApartments = () => {
        
        navigate(`/properties/${id}/apartments`);
    };

    return (
        <Card key={id}>
            <div>
                <p>{owner_name}</p>
                <p>{address}</p>
                <p>{total_apts}</p>
                <Button onClick={handleViewApartments}>Apartments</Button>
                {/* <Button >Delete Property</Button> */}
            </div>

        </Card>
    )
}