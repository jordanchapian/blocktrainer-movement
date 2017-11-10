import React, { Component } from 'react';
import { Route } from 'react-router-dom'

import Login from './login/Login.jsx';
import UserZone from './userZone/userZone.jsx';

import { MuiThemeProvider, createMuiTheme } from 'material-ui/styles';

import './AuthBase.css'

const theme = createMuiTheme();

class AuthBase extends Component {

  render() {
    return (

          <MuiThemeProvider theme={theme}>
              <div>
                  <Route path="/login" component={Login}/>
                  <Route path="/uz" component={UserZone}/>
              </div>
          </MuiThemeProvider>
    );
  }
}

export default AuthBase;
