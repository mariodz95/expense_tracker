import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  token: null,
  user: null,
  isAuthenticated: false,
  error: null,
};

export const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    setCredentials: (state, action) => {
      const { payload } = action;
      return {
        ...state,
        token: payload.token,
        user: payload.user,
        isAuthenticated: true,
      };
    },
    logout: (state) => {
      return initialState;
    },
  },
});

export const { setCredentials, logout } = authSlice.actions;

export default authSlice.reducer;

export const selectCurrentUser = (state) => state.auth.user;
export const selectIsAuthenticated = (state) => state.auth.isAuthenticated;
