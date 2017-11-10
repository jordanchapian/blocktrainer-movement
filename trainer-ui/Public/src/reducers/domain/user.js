import { combineReducers } from 'redux';

function activeUser(state = {
	
	isFetching: false,
    didInvalidate: false,
    data:undefined

}, action){

	switch(action.type){
		default:
			return state;
	}

}

const rootReducer = combineReducers({
	activeUser
});

export default rootReducer;