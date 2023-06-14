import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'

const API_URL = "http://localhost:7000/";


export const authApi = createApi({
  reducerPath: 'authApi',
  baseQuery: fetchBaseQuery({ 
    baseUrl: API_URL,
    prepareHeaders: (headers, { getState }) => {
      headers.set('Content-Type', 'application/json')
      headers.set('Accept', 'application/json')
      return headers
  }
  }),
  endpoints: (build) => ({
    loginUser: build.mutation({
      query: (body) => ({
        url: 'auth/login',
        method: 'POST',
        body,
      }),
    }),
    signupUser: build.mutation({
      query: (body) => ({
        url: 'auth/signup',
        method: 'POST',
        body,
      }),
    }),
  }),
});

export const { useLoginUserMutation, useSignupUserMutation } = authApi;
