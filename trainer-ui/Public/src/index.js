import React from 'react';
import thunkMiddleware from 'redux-thunk';
import ReactDOM from 'react-dom';
import { HashRouter, Route } from 'react-router-dom';
import { createStore, applyMiddleware } from 'redux';
import { Provider } from 'react-redux';

import registerServiceWorker from './registerServiceWorker';

//routes
import AuthBase from './modules/AuthBase.jsx';
import reducerIndex from './reducers/index.js';

// styles


//base store
let store = createStore(
	reducerIndex,
	applyMiddleware(
		thunkMiddleware
	)
);

//rendering
ReactDOM.render((
	<Provider >
	  <HashRouter>
	    <Route path="/" component={AuthBase} />
	  </HashRouter>
  	</Provider>

), document.getElementById('root'));

registerServiceWorker();