import React, { Component } from 'react';
import _ from 'underscore';

import ProgramTimelineAnnotation from './ProgramTimelineAnnotation';
import ProgramTimelineWeekIndicator from './ProgramTimelineWeekIndicator';
import "./ProgramTimeline.css";
import fakeData from './fakeData';


function drawTimeline(data){

}

class ProgramTimeline extends Component {
    state = {
      days:fakeData,
      activeDay:fakeData[12]
    };

    handleDayChange(annotationClicked, e){
      this.setState({
         activeDay: annotationClicked.getDay()
      });
    }

    renderTimeline(){
      var r = [];

      var nWeeks = Math.ceil(this.state.days.length / 7);

      //get active day index
      var activeDayIndex = _.indexOf(this.state.days, this.state.activeDay);
      var activeWeekIndex = Math.floor(activeDayIndex / 7);

      //create the week indicators
      for(let i=0; i < nWeeks; i++){
          r.push([
            (<ProgramTimelineWeekIndicator weekNumber={i+1} isBeforeActive={activeWeekIndex >= i} key={"timeline-week-header-"+1} />)
          ]);
      }

      //create the annotations for each day
      for(let i=0; i< this.state.days.length; i++){
        let e = this.state.days[i];
        r[Math.floor(i / 7)].push((
          <ProgramTimelineAnnotation
              key={e.id}
              onBubbleClick={(annotation, e) => this.handleDayChange(annotation, e)}
              dayAnnotation={(i - (Math.floor(i / 7) * 7)) + 1}
              isBeforeActive={i < activeDayIndex}
              isActive={activeDayIndex === i}
              hasNext={i !== (this.state.days.length - 1)}
              day={e} />
        ));

      }


      return r.map(function(e, i){
        return (
          <div className="weekContainer" key={"timeline-week-"+i}>
            {e}
          </div>
        );
      });
    };

    render() {

        return (
            <div id="ProgramTimeline">
              <div className="ProgramTimeline-container">
                  {this.renderTimeline()}
              </div>
            </div>
        );
    }
}

export default ProgramTimeline;
