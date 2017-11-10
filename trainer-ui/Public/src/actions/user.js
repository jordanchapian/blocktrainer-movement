import { restApi } from '../vendor/sovaSharedApi.js';

export const REQUEST_ACTIVE_USER = 'REQUEST_ACTIVE_USER';
export const RECEIVE_ACTIVE_USER = 'RECEIVE_ACTIVE_USER';

console.log(restApi);

//Note, this uses the (user) api (no ID needed)
export function requestActiveUser(){
	return {
		type: REQUEST_ACTIVE_USER
	}
}

export function receivedActiveUser(data){
	return {
		type: RECEIVE_ACTIVE_USER,
		data,
		receivedAt: Date.now()
	}
}

export function fetchActiveUser(){
	return function(dispatch){

		dispatch(requestActiveUser());

		return restApi.TenantService.v1.user.getActiveUser.execute()
			.then(response => response.json())
			.then(json => dispatch(receivedActiveUser(json)));
	};
}