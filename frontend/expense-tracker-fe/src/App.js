import './App.css';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'
import Header from './components/Header'
import Login from "./features/user/Login"
import Register from './features/user/Register'
import Profile from './features/user/Profile'
import Home from './features/home/Home'
import ProtectedRoute from './routes/ProtectedRoute'
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  return (
    <Router>
      <Header />
      <div className="App">
      <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/login' element={<Login />} />
          <Route path='/register' element={<Register />} />
          <Route element={<ProtectedRoute />}>
            <Route path='/user-profile' element={<Profile />} />
          </Route>
          <Route path='*' element={<Navigate to='/' replace />} />
        </Routes>

      </div>
    </Router>
  );
}

export default App;
