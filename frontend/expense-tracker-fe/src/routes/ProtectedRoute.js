import { useSelector } from 'react-redux'
import { NavLink, Outlet } from 'react-router-dom'

const ProtectedRoute = () => {
  const { user } = useSelector((state) => state.auth)

  if (!user) {
    return (
      <div className='unauthorized'>
        <h1>Unauthorized.</h1>
        <span>
          <NavLink to='/login'>Login</NavLink>
        </span>
      </div>
    )
  }

  return <Outlet />
}

export default ProtectedRoute
