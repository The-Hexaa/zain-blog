import { createSlice } from '@reduxjs/toolkit';


const initialState = {
    id: "",
    name: "",
    email: "",
    role: "",
}
const userInfoSlice = createSlice({
    name: "user_info",
    initialState,
    reducers: {
        setUserInfo(state, action) {
            state.id = action.payload.id;
            state.name = action.payload.name;
            state.email = action.payload.email;
            state.role = action.payload.role;

        },
        unsetUserInfo(state, action) {
            state.id = action.payload.id;
            state.name = action.payload.name;
            state.email = action.payload.email;
            state.role = action.payload.role;

        },
    },
});

export const { setUserInfo, unsetUserInfo } = userInfoSlice.actions;
export default userInfoSlice.reducer;
