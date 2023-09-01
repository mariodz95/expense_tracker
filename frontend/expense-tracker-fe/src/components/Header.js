import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { NavLink } from 'react-router-dom'
import styles from "./Header.module.scss";
import Button from "@mui/material/Button";

const Header = () => {
  const { user } = useSelector((state) => state.auth)
  const dispatch = useDispatch()

  // // automatically authenticate user if token is found
  // const { data, isFetching } = useGetDetailsQuery('userDetails', {
  //   pollingInterval: 900000, // 15mins
  // })


  return (
    <header>
      <div className={styles['header-status']}>
        <span>
          {user && `Logged in as ${user.email}`}
          {user === null && "You're not logged in"}
        </span>
        <div className={styles['cta']}>
          {user ? (
            <Button className='button'>
              Logout
            </Button>
          ) : (
            <NavLink className='button' to='/login'>
              Login
            </NavLink>
          )}
        </div>
      </div>
      <nav className={styles['navigation']}>
        <NavLink to='/'>Home</NavLink>
        <NavLink to='/login'>Login</NavLink>
        <NavLink to='/register'>Register</NavLink>
        <NavLink to='/user-profile'>Profile</NavLink>
      </nav>
    </header>
  )
}

export default Header
