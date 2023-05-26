import { useSelector } from 'react-redux'
import '../../styles/profile.css'

const Profile = () => {
  const { user } = useSelector((state) => state.auth)

  return (
    <div>
      {console.log("DADA user", user)}
      <figure>{user?.firstName}</figure>
      <span>
        Welcome <strong>{user?.firstName}!</strong> You can view this page
        because you're logged in
      </span>
    </div>
  )
}

export default Profile
