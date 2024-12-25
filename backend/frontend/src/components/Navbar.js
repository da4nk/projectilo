import React from 'react'
import Mode from './Mode-Button'
const Navbar = () =>
{

    const info = document.querySelector('#user');
    const user = info.getAttribute("data-user");
    fetch(`api/users/{user}`)
    {
        
    }
    return (
        <><div>

        </div>
        
        <div id='sidebar' className='d-flex flex-column flex-shrink-0 p-3'>
            <div className='mb-4 '>
                <a id="item-link" href='/profile' className='d-flex align-items-center'>Profile</a>
            </div>


            <Mode />



            <div id="main-content" className='p-2 mt-5 pt-4'>
                <div className='mt-5 pt-4'>
                    <a id="item-link" href='/' className='d-flex align-items-center'>Home</a>

                </div>




            </div>
            <div id="bottom" className='mt-5 pt-4'>
                <div className='mb-5 pt-5'>
                    <a href='/login/' id='item-link' className='pt-5 mt-5  d-flex align-items-center'>Logout</a>
                </div>
            </div>
        </div></>
    )
}
export default Navbar