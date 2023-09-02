import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import styles from "./Header.module.scss";
import Button from "@mui/material/Button";
import { HEADER_TEXT as TEXT } from "../constants/text-constants";

const Header = () => {
  const { user } = useSelector((state) => state.auth);
  const dispatch = useDispatch();

  useEffect(() => {
    // On refresh page fetch user data if token exists
  }, []);

  return (
    <header>
      <div className={styles["header-status"]}>
        <span>{user && `${TEXT.USER_LOGGED_IN_TEXT} ${user.email}`}</span>
        <div className={styles["cta"]}>
          {user ? (
            <Button className="button">{TEXT.LOGOUT_BUTTON_TEXT}</Button>
          ) : (
            <>
              <NavLink to="/login" className={styles["nav-link"]}>
                {TEXT.LOGIN_BUTTON_TEXT}
              </NavLink>
              <NavLink to="/register" className={styles["nav-link"]}>
                {TEXT.SIGNUP_BUTTON_TEXT}
              </NavLink>
            </>
          )}
        </div>
      </div>
      <nav className={styles["navigation"]}>
        <NavLink to="/">{TEXT.HOME_NAV_TEXT}</NavLink>
        <NavLink to="/user-profile">{TEXT.PROFILE_NAV_TEXT}</NavLink>
      </nav>
    </header>
  );
};

export default Header;
