import React, { Component } from 'react';
import Paper from 'material-ui/Paper';
import Grid from 'material-ui/Grid';
import FitnessCenterIcon from 'material-ui-icons/FitnessCenter';

class Programs extends Component {

    render() {

        return (
            <div id="programLanding">
                <div className="pre-content-heading">

                    <div className="page-icon">
                        <FitnessCenterIcon />
                    </div>

                    <div className="breadcrumb">
                        <span>
                            Home / Programs
                        </span>
                    </div>

                </div>
                <div className="container tp rp lp">
                    <Grid container spacing={24}>
                        <Grid item xs={3}>
                            <Paper>
                                My Collection
                            </Paper>
                        </Grid>
                        <Grid item xs={3}>
                            <Paper>
                                Community Programs
                            </Paper>
                        </Grid>
                        <Grid item xs={3}>
                            <Paper>
                                Community Templates
                            </Paper>
                        </Grid>
                        <Grid item xs={3}>
                            <Paper>
                                Create New Program
                            </Paper>
                        </Grid>
                    </Grid>

                    <h2>
                        Recent Programs
                    </h2>

                    <h2>
                        Latest Community Programs
                    </h2>

                    <h2>
                        Latest Community Templates
                    </h2>



                </div>
            </div>
        );
    }
}

export default Programs;
