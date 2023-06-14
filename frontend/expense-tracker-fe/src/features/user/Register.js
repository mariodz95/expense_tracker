import { useEffect, useState } from 'react'
import { useForm } from 'react-hook-form'
import { useDispatch, useSelector } from 'react-redux'
import { useNavigate } from 'react-router-dom'
import Error from '../../components/Error'
import Spinner from '../../components/Spinner'
import { useSignupUserMutation } from '../../services/authApi'
import { setCredentials } from './authSlice'


const Register = () => {
  const [customError, setCustomError] = useState(null)

  const { loading, user, success } = useSelector(
    (state) => state.auth
  )
  const dispatch = useDispatch()
  const [signup, { isLoading, error }] = useSignupUserMutation();
  const { register, handleSubmit } = useForm()
  const navigate = useNavigate()

  useEffect(() => {
    if (user) navigate('/user-profile')
    if (success) navigate('/login')
  }, [navigate, user, success])

  const submitForm = async (data) => {
    data.email = data.email.toLowerCase()
    const user = await signup(data).unwrap();
    dispatch(setCredentials(user))
    navigate('/user-profile')
  }

  return (
    <form onSubmit={handleSubmit(submitForm)}>
      {error && <Error>{error}</Error>}
      {customError && <Error>{customError}</Error>}
      <div className='form-group'>
        <label htmlFor='username'>User Name</label>
        <input
          type='text'
          className='form-input'
          {...register('username')}
          required
        />
      </div>
      <div className='form-group'>
        <label htmlFor='first_name'>First Name</label>
        <input
          type='text'
          className='form-input'
          {...register('first_name')}
          required
        />
      </div>
      <div className='form-group'>
        <label htmlFor='last_name'>Last Name</label>
        <input
          type='text'
          className='form-input'
          {...register('last_name')}
          required
        />
      </div>
      <div className='form-group'>
        <label htmlFor='email'>Email</label>
        <input
          type='email'
          className='form-input'
          {...register('email')}
          required
        />
      </div>
      <div className='form-group'>
        <label htmlFor='password'>Password</label>
        <input
          type='password'
          className='form-input'
          {...register('password')}
          required
        />
      </div>
      <div className='form-group'>
        <label htmlFor='date_of_birth'>Date of birht</label>
        <input
          type='text'
          className='form-input'
          {...register('date_of_birth')}
          required
        />
      </div>
      <button type='submit' className='button' disabled={loading}>
        {loading ? <Spinner /> : 'Register'}
      </button>
    </form>
  )
}

export default Register
