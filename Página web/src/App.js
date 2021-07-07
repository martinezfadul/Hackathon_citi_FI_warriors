import Product from "./components/Product"
import './App.css';
import Navbar from "./components/Navbar";
import Products from "./components/Products";
import CheckoutCard from "./components/CheckoutCard";
import CheckoutPage from "./components/CheckoutPage";
import { Switch, BrowserRouter as Router, Route } from "react-router-dom";
import SignIn from "./components/Signin";
import SignUp from "./components/Signup";
import { useEffect } from "react";
import { auth } from "./firebase";
import { actionTypes } from "./reducer";
import {useStateValue} from "./StateProvider"
import Carousel from "./components/Carousel"
import Home from "./components/ubicacion";

const ColoredLine = ({ color }) => (
  <hr
    style={{
      color: color,
      backgroundColor: color,
      height: 5,
    }}
  />
);


function App() {
  const [{user}, dispatch] = useStateValue();
  useEffect(()=>{
    auth.onAuthStateChanged((authUser)=>{
      console.log(authUser);
      if (authUser){
        dispatch({
          type: actionTypes.SET_USER,
          user: authUser,
        })
      }
    })
  },[])

  return (
    <Router>
    <div className="App">
        <Navbar/>
        
           <Switch>
                  
                <Route path="/signup">
                    <SignUp/>
                  </Route>
                  
                  <Route path="/signin">
                    <SignIn/>
                  </Route>
                  
                  <Route path="/checkout-page">
                    <CheckoutPage/>
                  </Route>
                  
                  <Route path="/">
                     <Carousel/>
                     
                    <div className="texto">
                      <h1>Para ti</h1>
                      <ColoredLine color="red" />
                    </div>

                    <Products/>
                  </Route>
           </Switch>

        
      </div>
    </Router>
  );
}

export default App;
