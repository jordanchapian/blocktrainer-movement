import React, { Component } from 'react';
import {numToWords} from 'modules/utils/format';

class ProgramTimelineWeekIndicator extends Component {

  static defaultProps = {
    isBeforeActive:false
  };

  getIndicatorClass(){
    let cardClass = "ProgramTimelineWeekIndicator ";

    if(this.props.isBeforeActive === true){
      cardClass += "beforeActive ";
    }

    return cardClass;
  }

  render(){
    return (
      <div className={this.getIndicatorClass()}>
        <div className="text">
          Week {numToWords(this.props.weekNumber)}
        </div>
        <div className="path"></div>
      </div>
    );
  }
}


export default ProgramTimelineWeekIndicator;
