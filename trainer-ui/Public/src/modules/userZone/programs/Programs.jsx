import React, { Component } from 'react';
import { Route, Link } from 'react-router-dom'

// import Paper from 'material-ui/Paper';
// import Grid from 'material-ui/Grid';
import FitnessCenterIcon from 'material-ui-icons/FitnessCenter';

class Programs extends Component {

    render() {

        return (
            <div id="userZone">
                <div className="pre-content-heading">
                    <div className="page-icon">
                        <FitnessCenterIcon />
                    </div>
                    <div className="page-title">

                        <h1>
                            Programs
                        </h1>
                        <div className="nav-list">
                            <div>
                                <Link to="">Overview</Link>
                                <a>
                                    My Programs
                                </a>
                                <a>
                                    Community
                                </a>
                                <a>
                                    Create New Program
                                </a>
                            </div>
                        </div>
                    </div>

                </div>
                <div className="container tp rp lp">
                    {/*<Grid container spacing={24}>*/}
                        {/*<Grid item xs={12}>*/}

                            {/*<Paper>My Favorites</Paper>*/}
                        {/*</Grid>*/}
                        {/*<Grid item xs={6}>*/}
                            {/*<Paper>My Favorites</Paper>*/}
                        {/*</Grid>*/}
                        {/*<Grid item xs={3}>*/}
                            {/*<Paper>xs=3</Paper>*/}
                        {/*</Grid>*/}
                        {/*<Grid item xs={3}>*/}
                            {/*<Paper>xs=3</Paper>*/}
                        {/*</Grid>*/}
                        {/*<Grid item xs={3}>*/}
                            {/*<Paper>xs=3</Paper>*/}
                        {/*</Grid>*/}
                    {/*</Grid>*/}

                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                    <h1>Program View</h1>
                </div>
            </div>
        );
    }
}

export default Programs;
