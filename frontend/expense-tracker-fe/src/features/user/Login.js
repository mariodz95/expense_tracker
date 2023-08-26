import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import Error from "../../components/Error";
import Spinner from "../../components/Spinner";
import { useLoginUserMutation } from "../../services/authApi";
import { setCredentials } from "./authSlice";
import styles from "./Login.module.scss";
import Button from "@mui/material/Button";

const Login = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { register, handleSubmit } = useForm();
  const { loading, user } = useSelector((state) => state.auth);
  const [login, { isLoading, error }] = useLoginUserMutation();

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
      console.log("Error", err);
    }
  };

  return (
    <div className={styles["form-container"]}>
      <form onSubmit={handleSubmit(submitForm)}>
        {error && <Error>{error}</Error>}
        <div className={styles["form-group"]}>
          <label htmlFor="email">Email</label>
          <input
            type="email"
            className={styles["form-input"]}
            {...register("email")}
            required
          />
        </div>
        <div className={styles["form-group"]}>
          <label htmlFor="password">Password</label>
          <input
            type="password"
            className={styles["form-input"]}
            {...register("password")}
            required
          />
        </div>
        <Button variant="contained" type="submit">Login</Button>;
      </form>
    </div>
  );
};

export default Login;
