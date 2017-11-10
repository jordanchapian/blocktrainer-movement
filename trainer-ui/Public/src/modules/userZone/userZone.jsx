import React from 'react';
import { Route, Link } from 'react-router-dom'

import List, { ListItem, ListItemIcon, ListItemText } from 'material-ui/List';
import DashboardIcon from 'material-ui-icons/Dashboard';
import PeopleIcon from 'material-ui-icons/People';
import FitnessCenterIcon from 'material-ui-icons/FitnessCenter';
import KitchenIcon from 'material-ui-icons/Kitchen';

import Programs from './programs/Programs';


import './userZone.css';

class PersistentDrawer extends React.Component {
    state = {
        open: true,
    };

    handleDrawerOpen = () => {
        this.setState({ open: true });
    };

    handleDrawerClose = () => {
        this.setState({ open: false });
    };

    render() {
        const { classes, theme } = this.props;

        return (
            <div id="userZone">

                <div className="appBar">
                    <div className="brand">

                    </div>
                    <div className="toolbar">
                    </div>
                </div>

                <div className="nav">
                    <List>
                        <ListItem button component={Link} to='/uz/dashboard'>
                            <ListItemIcon>
                                <DashboardIcon />
                            </ListItemIcon>
                            <ListItemText primary="Dashboard"/>
                        </ListItem>
                        <ListItem button component={Link} to='/uz/programs'>
                            <ListItemIcon>
                                <FitnessCenterIcon />
                            </ListItemIcon>
                            <ListItemText primary="Programs"/>
                        </ListItem>
                        <ListItem button component={Link} to='/uz/diets'>
                            <ListItemIcon>
                                <KitchenIcon />
                            </ListItemIcon>
                            <ListItemText primary="Diets"/>
                        </ListItem>
                        <ListItem button component={Link} to='/uz/clients'>
                            <ListItemIcon>
                                <PeopleIcon />
                            </ListItemIcon>
                            <ListItemText primary="Clients"/>
                        </ListItem>
                    </List>
                </div>
                <div className="content">
                    <Route  path="/uz/programs" component={Programs}/>
                </div>
            </div>
        );
    }
}


export default PersistentDrawer;