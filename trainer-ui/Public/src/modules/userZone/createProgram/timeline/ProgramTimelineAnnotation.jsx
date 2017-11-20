import React, { Component } from 'react';
import { DragSource, DropTarget } from 'react-dnd'
import DragHandleIcon from 'material-ui-icons/DragHandle';

import _ from 'underscore';

const cardSource = {
	beginDrag(props) {
		return {
			day:props.day
      // originalIndex:
		}
	},

	endDrag(props, monitor) {

		// const { id: droppedId, originalIndex } = monitor.getItem()
		// const didDrop = monitor.didDrop()
    //
		// if (!didDrop) {
		// 	props.moveCard(droppedId, originalIndex)
		// }
	}
};

const cardTarget = {
	canDrop() {
		return false
	},

	hover(props, monitor) {
		// const { id: draggedId } = monitor.getItem()
		// const { id: overId } = props
    //
		// if (draggedId !== overId) {
		// 	const { index: overIndex } = props.findCard(overId)
		// 	props.moveCard(draggedId, overIndex)
		// }
	}
};

@DropTarget("ANNOTATION",cardTarget, card, connect => {
	connectDropTarget: connect.dropTarget(),
})
@DragSource("ANNOTATION", cardSource, (connect, monitor) => {
	connectDragSource: connect.dragSource(),
	isDragging: monitor.isDragging(),
})
export default class ProgramTimelineAnnotation extends Component {

    static defaultProps = {
      //data
      day:null,

      //locality
      hasNext: true,
      isActive:false,
      isBeforeActive:false,

      //events
      onBubbleClick:null
    };

    getDay(){
        return this.props.day;
    }

    handleBubbleClick(e){
      if(_.isFunction(this.props.onBubbleClick)){
        this.props.onBubbleClick(this, e);
      }
    }

    getAnnotationClass(){
      let cardClass = "ProgramTimelineAnnotation ";

      if(this.props.isActive === true){
        cardClass += "active ";
      }

      if(this.props.isBeforeActive === true){
        cardClass += "beforeActive ";
      }

      return cardClass;
    }

    render() {


        return (
          <div className={this.getAnnotationClass()}>

            <div className="day-annotation">
              <div className="middle">
                  {this.props.dayAnnotation}
              </div>
            </div>

            <div className="card">
              <div className="top-tools">
                <DragHandleIcon className="dragHandle"></DragHandleIcon>
              </div>
              <ul className="sessions">

                {(function(sessions){
                  //rest day
                  if(!sessions || sessions.length === 0){
                      return (<li className="non-actionable">Rest</li>)
                  };

                  var listItems = sessions.map((e) => {
                    return (
                      <li className="actionable" key={e.id}>
                        {e.title}
                      </li>
                    );
                  });

                  return listItems;

                })(this.props.day.sessions)}

              </ul>
              <div className="bottom-tools">

              </div>
            </div>

            <div className="pre-path">

            </div>

            {(function(show){
              if(show){
                return (
                  <div className="post-path">

                  </div>
                );
              }
            })(this.props.hasNext)}

            <div className="path-dot" onClick={(e) => this.handleBubbleClick(e)}>

            </div>

          </div>
        );
    }
}
