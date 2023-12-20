import { Card , Button} from "@mui/material";
import { useNavigate,useOutletContext } from "react-router-dom";



export function ApartmentsCard (props) {
    const {id, apt_name, tenant_name,lease_start, lease_end} = props.apartment
    const navigate = useNavigate();

    const handleViewTenantInfo = () => {
        navigate(`/apartments/${id}/tenant`);
    };

    const handleAddTenant =() => {
        props.setSelectedApartment(apt_name)
        navigate(`/apartments/${id}/addtenant`)

    }


    return (
        <Card key={id}>
            <div>
                <p>Tenant Name : {tenant_name}</p>
                <p>Apartment# : {apt_name}</p>
                <p>Lease Start : {lease_start}</p>
                <p>Lease End : {lease_end}</p>
                <Button onClick={handleAddTenant}>Add Tenant</Button>
                <Button onClick={handleViewTenantInfo}>Tenant Info</Button>
                <Button >Delete Apartment</Button>
            </div>

        </Card>
    )
}