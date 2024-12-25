import React from "react";



const Login = () => {
    return (
        <><form action="">
            <div className="form-group">
                <input autofocus className="form-control" type="text" name="username" placeholder="Username" />
            </div>
            <div class="form-group">
                <input className="form-control" type="password" name="password" placeholder="Password" />
            </div>
            <input className="btn btn-primary" type="submit" value="Login" />
        </form>
        dont have an account <a href="/register/">Register here.</a></>
    )

}

export default Login;