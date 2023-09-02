import React, { useEffect, useState } from "react";
import { useForm } from "react-hook-form";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import { useSignupUserMutation } from "../../services/authApi";
import { setCredentials } from "./authSlice";
import styles from "./Login.module.scss";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Box from "@mui/material/Box";
import { SIGNUP_TEXT as TEXT } from "../../constants/text-constants";
import { DatePicker } from "@mui/x-date-pickers/DatePicker";
import { DemoContainer } from "@mui/x-date-pickers/internals/demo";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";
import { format } from "date-fns";

const Register = () => {
  const { user, success } = useSelector((state) => state.auth);
  const dispatch = useDispatch();
  const [signup] = useSignupUserMutation();
  const { register, handleSubmit } = useForm();
  const navigate = useNavigate();
  const [errorMessage, setErrorMessage] = useState();
  const [dateOfBirthValue, setDateOfBirthValue] = useState();

  useEffect(() => {
    if (user) navigate("/user-profile");
    if (success) navigate("/login");
  }, [navigate, user, success]);

  const submitForm = async (data) => {
    try {
      data.email = data.email.toLowerCase();
      data.date_of_birth = format(dateOfBirthValue, "yyyy-MM-dd hh:mm:ss");
      const user = await signup(data).unwrap();
      dispatch(setCredentials(user));
      navigate("/user-profile");
    } catch (err) {
      setErrorMessage(err.data.detail);
    }
  };

  return (
    <div className={styles["form-container"]}>
      <Box
        component="form"
        onSubmit={handleSubmit(submitForm)}
        sx={{
          "& .MuiTextField-root": { m: 1, width: "25ch" },
        }}
      >
        <div className={styles["row"]}>
          <TextField
            required
            id="outlined-required"
            label={TEXT.EMAIL_LABEL_TEXT}
            InputLabelProps={{
              shrink: true,
            }}
            color="secondary"
            type="email"
            {...register("email")}
          />
        </div>
        <div className={styles["row"]}>
          <TextField
            required
            id="outlined-required"
            label={TEXT.PASSWORD_LABEL_TEXT}
            InputLabelProps={{
              shrink: true,
            }}
            color="secondary"
            type="password"
            {...register("password")}
          />
        </div>
        <div className={styles["row"]}>
          <TextField
            required
            id="outlined-required"
            label={TEXT.USERNAME_LABEL_TEXT}
            InputLabelProps={{
              shrink: true,
            }}
            color="secondary"
            type="text"
            {...register("username")}
          />
        </div>
        <div className={styles["row"]}>
          <TextField
            required
            id="outlined-required"
            label={TEXT.FIRSTNAME_LABEL_TEXT}
            InputLabelProps={{
              shrink: true,
            }}
            color="secondary"
            type="text"
            {...register("first_name")}
          />
        </div>
        <div className={styles["row"]}>
          <TextField
            required
            id="outlined-required"
            label={TEXT.LASTNAME_LABEL_TEXT}
            InputLabelProps={{
              shrink: true,
            }}
            color="secondary"
            type="text"
            {...register("last_name")}
          />
        </div>
        <div className={styles["row"]}>
          <LocalizationProvider dateAdapter={AdapterDayjs}>
            <DemoContainer components={["DatePicker"]}>
              <DatePicker
                label={TEXT.DATE_OF_BIRTH_LABEL}
                onChange={(e) => {
                  setDateOfBirthValue(e.$d);
                }}
                slotProps={{
                  textField: {
                    required: true,
                  },
                }}
              />
            </DemoContainer>
          </LocalizationProvider>{" "}
        </div>
        <div className={styles["row"]}>
          <span className={styles["error-message"]}>{errorMessage}</span>
        </div>
        <div className={styles["row"]}>
          <Button
            variant="contained"
            className={styles["form-button"]}
            type="submit"
            color="secondary"
          >
            {TEXT.SIGNUP_BUTTON_TEXT}
          </Button>
        </div>
      </Box>
    </div>
  );
};

export default Register;
