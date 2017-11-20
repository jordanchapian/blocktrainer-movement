import React, { Component } from 'react';
import ProgramTimeline from './timeline/ProgramTimeline';


import './CreateProgram.css';

class CreateProgram extends Component {

    render() {

        return (
            <div id="createProgram" >
                <div className='timelineContainer'>
                  <ProgramTimeline>
                  </ProgramTimeline>
                </div>
            </div>
        );
    }
}

export default CreateProgram;
