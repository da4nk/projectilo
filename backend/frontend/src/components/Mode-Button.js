import React,{ useState } from "react";

const Mode = ()=>{
    const [darkMode, setDarkMode] = useState({text: 'DarkMode',enabeled: false});

    const toggle = ()=>
    {
        setDarkMode(prevstate =>(
        {
            ...prevstate,
            enabeled: !prevstate.enabeled
       }));
        document.documentElement.setAttribute('data-bs-theme', darkMode.enabeled ? 'light' : 'dark')

        if(darkMode.enabeled)
        {
            document.querySelector('.btn').innerHTML = 'DarkMode';

        }
        else if(!darkMode.enabeled)
        {
            document.querySelector('.btn').innerHTML = 'LightTheme';

        }
        

    };

    return (
        <button onClick = {toggle} className="btn btn-primary px-1 py-2">
            {darkMode.text}
        </button>
    )
}

export default Mode