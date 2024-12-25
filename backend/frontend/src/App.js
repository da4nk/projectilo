import{
  BrowserRouter as Router, 
  Route, Routes 
  
} from "react-router-dom"

import React from 'react';
import './App.css';
import Login from "./pages/login";
import MainPage from "./pages/main";
import Register from "./pages/register";
function App() {
  

  



  return (
    
    <Router>
      <div className="App">
        <Routes>
          <Route path = "" element = {<MainPage />} />
          <Route path="/login/" element={<Login />} />
          <Route path = "/register" element = {<Register />} />

        </Routes>
      </div>
    </Router>
  );
}

export default App;
