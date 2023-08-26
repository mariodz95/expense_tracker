import styles from "./Home.module.scss";
import { HOME_TEXT as TEXT } from "../../constants/text-constants"

const Home = () => {
  return (
    <div className={styles['home-container']}>
      <h1 className={styles.title}>{TEXT.TITLE_TEXT}</h1>
      <p>
        {TEXT.INFO_TEXT}
      </p>
    </div>
  );
};

export default Home;
