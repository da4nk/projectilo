import React, { useEffect, useState } from "react";


import Cookies from 'js-cookie';

const Register = ()=>{

    // adds csrf token
    const [csrfToken, setCsrfToken] = useState('');
    useEffect(() => 
    {
        const token = Cookies.get('csrftoken');
        if (token) {
          setCsrfToken(token);
        }
    
    }, []);

    // this is the page 
    return(

    <><form action="/register/" method="post">
            
            <input type="hidden" name="csrfmiddlewaretoken" value={csrfToken} />

            <div className="form-group">
                <input className="form-control" autofocus type="text" name="username" placeholder="Username" />
            </div>
            <div className="form-group">
                <input className="form-control" type="email" name="email" placeholder="Email Address" />
            </div>
            <div className="form-group">
                <input className="form-control" type="password" name="password" placeholder="Password" />
            </div>
            <div className="form-group">
                <input className="form-control" type="password" name="confirmation" placeholder="Confirm Password" />
            </div>
            <input className="btn btn-primary" type="submit" value="Register" />
        </form><a href="">Log In here.</a></>
    )
}
export default Register;