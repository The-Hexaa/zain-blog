import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'


// Define a service using a base URL and expected endpoints
export const userAuthApi = createApi({
  reducerPath: 'userAuthApi',
  baseQuery: fetchBaseQuery({ baseUrl: `${process.env.REACT_APP_API_URL}/account/` }),
  endpoints: (builder) => ({
    registerUser: builder.mutation({
        query:(user)=>{
            return{
                url:'register/',
                method: 'POST',
                body: user,
                headers: {
                    'Content-Type': 'application/json',
                    'ngrok-skip-browser-warning':"1233",
                },
            }
        }
    }),
    verifyUser: builder.mutation({
        query:(token)=>{
            return{
                url:'verify-email/',
                method: 'GET',
                headers: {
                    'Authorization': `bearer ${token}`,
                    'ngrok-skip-browser-warning':"1233",
                },
            }
        }
    }),
    loginUser: builder.mutation({
      query:(user)=>{
          return{
              url:'login/',
              method: 'POST',
              body: user,
              headers: {
                  'Content-Type': 'application/json',
                  'ngrok-skip-browser-warning':"1233",
              },
          }
      }
    }),
    getLoggedUser: builder.mutation({
        query:(access_token)=>{
            return{
                url:'profile/',
                method: 'GET',
                headers: {
                    'authorization': `Bearer ${access_token}`,
                    'ngrok-skip-browser-warning':"1233",
                },
            }
        }
      }),
      changePassword: builder.mutation({
        query:({userdata, access_token})=>{
            console.log('q userdata',userdata)
            console.log('q access_token',access_token)
            return{
                url:'changepassword/',
                method: 'POST',
                body: userdata,
                headers: {
                    'authorization': `Bearer ${access_token}`,
                    'ngrok-skip-browser-warning':"1233",
                },
            }
        }
      }),
      verifyOtp: builder.mutation({
        query:({data, user_id})=>{
            console.log("otp", data)
            return{
                url:`otp/${user_id}/verify_otp/`,
                method: 'PATCH',
                body: data,
                headers: {
                    'ngrok-skip-browser-warning':"1233",
                },
            }
        }
    }),
    sendOtp: builder.mutation({
        query:(user_id)=>{
            return{
                url:`otp/${user_id}/regenerate_otp/`,
                method: 'PATCH',
                headers: {
                    'ngrok-skip-browser-warning':"1233",
                },
            }
        }
    }),
}),
})

// Export hooks for usage in functional components, which are
// auto-generated based on the defined endpoints
export const { useRegisterUserMutation, useLoginUserMutation, useGetLoggedUserMutation, useChangePasswordMutation, useVerifyUserMutation, useSendOtpMutation, useVerifyOtpMutation } = userAuthApi;