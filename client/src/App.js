import React from 'react';
import logo from './logo.svg';
import './App.css';

class App extends React.Component {
  componentDidMount() {
    const requestOptions = {
      method: "POST",
      headers: {
        "Content-type": "application/json"
      },
      body: JSON.stringify({
        "username": "admin",
        "email": "",
        "password": "password"
      })
    }
    const url = `/rest-auth/login/`;

    function handleResponse(response) {
      return response.json().then(data => {
        if (!response.ok) {
          return Promise.reject(data.message);
        }
        return data;
      });
    }

    fetch(url, requestOptions)
    .then(handleResponse)
    .then(function(data) {
      console.log(data);
    })
    .catch(error => console.error(error));
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    );
  }
}

export default App;
