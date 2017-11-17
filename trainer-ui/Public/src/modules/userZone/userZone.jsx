import React from 'react';
import { Route, Link } from 'react-router-dom'

import List, { ListItem, ListItemIcon, ListItemText } from 'material-ui/List';

import Collapse from 'material-ui/transitions/Collapse';
import DashboardIcon from 'material-ui-icons/Dashboard';
import PeopleIcon from 'material-ui-icons/People';
import FitnessCenterIcon from 'material-ui-icons/FitnessCenter';
import KitchenIcon from 'material-ui-icons/Kitchen';
import ExpandLess from 'material-ui-icons/ExpandLess';
import ExpandMore from 'material-ui-icons/ExpandMore';
import RadioButtonUncheckedIcon from 'material-ui-icons/RadioButtonUnchecked';

import Programs from './programs/Programs';
import CreateProgram from './createProgram/CreateProgram';

import './userZone.css';

class PersistentDrawer extends React.Component {

    state = {
        open: false
    };

    handleClick = () => {
        this.setState({ open: !this.state.open });
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



                        {/*<ListItem button component={Link} to='/uz/programs'>*/}
                            {/*<ListItemIcon>*/}
                                {/*<FitnessCenterIcon />*/}
                            {/*</ListItemIcon>*/}
                            {/*<ListItemText primary="Programs"/>*/}
                        {/*</ListItem>*/}

                        <ListItem button onClick={this.handleClick}>
                            <ListItemIcon>
                                <FitnessCenterIcon />
                            </ListItemIcon>
                            <ListItemText inset primary="Programs" />
                            {this.state.open ? <ExpandLess /> : <ExpandMore />}
                        </ListItem>
                        <Collapse component="li" in={this.state.open} transitionDuration="auto" unmountOnExit>
                            <List disablePadding>
                                <ListItem button className="nested" component={Link} to='/uz/programs'>
                                    <ListItemIcon>
                                        <RadioButtonUncheckedIcon />
                                    </ListItemIcon>
                                    <ListItemText inset primary="Saved" />
                                </ListItem>
                                <ListItem button className="nested" component={Link} to='/uz/createProgram'>
                                    <ListItemIcon>
                                        <RadioButtonUncheckedIcon />
                                    </ListItemIcon>
                                    <ListItemText inset primary="Create" />
                                </ListItem>
                                <ListItem button className="nested" component={Link} to='/uz/programs'>
                                    <ListItemIcon>
                                        <RadioButtonUncheckedIcon />
                                    </ListItemIcon>
                                    <ListItemText inset primary="Explorer" />
                                </ListItem>
                            </List>
                        </Collapse>


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
                    <Route path="/uz/programs" component={Programs}/>
                    <Route path="/uz/createProgram" component={CreateProgram}/>
                </div>
            </div>
        );
    }
}


export default PersistentDrawer;