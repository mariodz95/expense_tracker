import { configureStore } from '@reduxjs/toolkit'
import authReducer from './features/user/authSlice'
import { authApi, signupApi } from './services/authApi'


export const store = configureStore({
  reducer: {
    auth: authReducer,
    [authApi.reducerPath]: authApi.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat([authApi.middleware]),
})
