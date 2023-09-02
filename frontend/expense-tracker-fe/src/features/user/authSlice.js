import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  token: null,
  user: null,
  isAuthenticated: false,
  refreshToken: null,
};

export const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    setCredentials: (state, action) => {
      const { payload } = action;
      return {
        ...state,
        token: payload.refreshToken,
        user: payload.user,
        isAuthenticated: true,
      };
    },
  },
});

export const { setCredentials } = authSlice.actions;

export default authSlice.reducer;
