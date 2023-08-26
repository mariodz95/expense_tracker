import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { useEffect, useState } from "react";
import { useLoginUserMutation } from "../../services/authApi";
import { setCredentials } from "./authSlice";
import { LOGIN_TEXT as TEXT } from "../../constants/text-constants";
import styles from "./Login.module.scss";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Box from "@mui/material/Box";

const Login = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { register, handleSubmit } = useForm();
  const { user } = useSelector((state) => state.auth);
  const [login] = useLoginUserMutation();
  const [errorMessage, setErrorMessage] = useState()

  useEffect(() => {
    if (user) {
      navigate("/user-profile");
    }
  }, [navigate, user]);

  const submitForm = async (data) => {
    try {
      const user = await login(data).unwrap();
      dispatch(setCredentials(user));
      navigate("/user-profile");
    } catch (err) {
      setErrorMessage(err.data.detail)
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
          <span className={styles['error-message']}>{errorMessage}</span>
        </div>
        <div className={styles["row"]}>
          <Button
            variant="contained"
            className={styles["login-button"]}
            type="submit"
            color="secondary"
          >
            {TEXT.LOGIN_BUTTON_TEXT}
          </Button>
        </div>
      </Box>
    </div>
  );
};

export default Login;
