
import React from 'react';
import hank from './images/hank.png';
import './Login.css';

export default function Login() {
    return (
      <div>
      log(n)
      </div>
    );
}
// //  Tutorial Link: https://blog.logrocket.com/user-authentication-firebase-react-apps/
//
// import React, { useEffect, useState } from "react";
// import { Link, useHistory } from "react-router-dom";
// import { auth, signInWithEmailAndPassword, signInWithGoogle } from "../firebase.js";
// // the tutorial says to use the below line instead
// // import { auth, signInWithEmailAndPassword, signInWithGoogle } from "./firebase";
// import { useAuthState } from "react-firebase-hooks/auth";
// import "./Login.css";
// function Login() {
//   const [email, setEmail] = useState("");
//   const [password, setPassword] = useState("");
//   const [user, loading, error] = useAuthState(auth);
//   const history = useHistory();
//   useEffect(() => {
//     if (loading) {
//       // maybe trigger a loading screen
//       return;
//     }
//     if (user) history.replace("/dashboard");
//   }, [user, loading]);
//   return (
//     <div className="login">
//       <div className="login__container">
//         <input
//           type="text"
//           className="login__textBox"
//           value={email}
//           onChange={(e) => setEmail(e.target.value)}
//           placeholder="E-mail Address"
//         />
//         <input
//           type="password"
//           className="login__textBox"
//           value={password}
//           onChange={(e) => setPassword(e.target.value)}
//           placeholder="Password"
//         />
//         <button
//           className="login__btn"
//           onClick={() => signInWithEmailAndPassword(email, password)}
//         >
//           Login
//         </button>
//         <button className="login__btn login__google" onClick={signInWithGoogle}>
//           Login with Google
//         </button>
//         <div>
//           <Link to="/reset">Forgot Password</Link>
//         </div>
//         <div>
//           Don't have an account? <Link to="/register">Register</Link> now.
//         </div>
//       </div>
//     </div>
//   );
// }
// export default Login;
