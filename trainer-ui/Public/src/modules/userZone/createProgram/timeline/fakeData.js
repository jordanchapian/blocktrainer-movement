import _ from "underscore";

let sessionVariants = [

  [
    {
      title:"Back and Legs",
      type:"WEIGHT_TRAINING"
    },
    {
      title: "Cardio",
      type:"CARDIO"
    }
  ],

  [
    {
      title:"Back and Legs",
      type:"WEIGHT_TRAINING"
    }
  ],

  [
    {
      title: "Cardio",
      type:"CARDIO"
    }
  ]

];

function getSessionVariant(){
    var r = _.random(0,2);

    if(r === 0){

      return [
        {
          id:_.uniqueId(),
          title:"Back and Legs",
          type:"WEIGHT_TRAINING"
        },
        {
          id:_.uniqueId(),
          title: "Cardio",
          type:"CARDIO"
        }
      ];

    } else if(r === 1){

      return [
        {
          id:_.uniqueId(),
          title:"Back and Legs",
          type:"WEIGHT_TRAINING"
        }
      ];

    } else {

      return [
        {
          id:_.uniqueId(),
          title: "Cardio",
          type:"CARDIO"
        }
      ];

    }

}

var n_sessions = 23;
var sessions_left = 23;
var counter = 0;
var output = [];

for(let week = 0; week < Math.ceil(n_sessions / 7); week++){
  var restDaysInWeek;

  if(sessions_left >= 7){
      restDaysInWeek = 2;
  } else if(sessions_left >= 3){
      restDaysInWeek = 1;
  } else {
    restDaysInWeek = 0;
  }

  var nToAdd = Math.min(sessions_left, 7) - restDaysInWeek;
  for(let i = 0; i < nToAdd; i++){
      output.push({
        id:_.uniqueId(),
        sessions:getSessionVariant()
      });
      counter++;
  }

  for(let i = 0; i < restDaysInWeek; i++){
      output.push({
        id:_.uniqueId(),
        sessions:[]
      });
      counter++;
  }

  sessions_left  = sessions_left - nToAdd - restDaysInWeek;
}

export default output;
