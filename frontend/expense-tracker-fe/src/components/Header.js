import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { NavLink } from 'react-router-dom'
import '../styles/header.css'

const Header = () => {
  const { user } = useSelector((state) => state.auth)
  const dispatch = useDispatch()

  // // automatically authenticate user if token is found
  // const { data, isFetching } = useGetDetailsQuery('userDetails', {
  //   pollingInterval: 900000, // 15mins
  // })


  return (
    <header>
      <div className='header-status'>
        <span>
          {/* {isFetching
            ? `Fetching your profile...`
            : user !== null
            ? `Logged in as ${user.email}`
            : "You're not logged in"} */}
          {user && `Logged in as ${user.email}`}
          {user === null && "You're not logged in"}
        </span>
        <div className='cta'>
          {user ? (
            <button className='button'>
              Logout
            </button>
          ) : (
            <NavLink className='button' to='/login'>
              Login
            </NavLink>
          )}
        </div>
      </div>
      <nav className='container navigation'>
        <NavLink to='/'>Home</NavLink>
        <NavLink to='/login'>Login</NavLink>
        <NavLink to='/register'>Register</NavLink>
        <NavLink to='/user-profile'>Profile</NavLink>
      </nav>
    </header>
  )
}

export default Header
