import { useState, useEffect } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  const authenticate = async () => {
    const auth = await fetch("/authenticate/", {
      credentials: 'include', // Include cookies in the request
    })
    const data = await auth.json()
    console.log(data)
  }

  useEffect(() => {
    authenticate()
  }, []);

  const test = async () => {
    try {
      const test1 = await fetch("http://127.0.0.1:8000/api/rest");
      if (test1.ok) {
        console.log(
          'Test route is "OK", now converting serialized data to json format'
        );
        const data = await test1.json();

        console.log("test1 response: ", data);
        /** data:
         * ['/api/test1/', '/api/test2/', '/api/test3/', '/api/test4/', '/api/test5/']
         */
        return data;
      }
    } catch (e) {
      console.log("Error", e);
    }
  };

  const [userData, setUserData] = useState(null);

  const fetchUserData = async () => {
    try {
      const response = await fetch('http://localhost:8000/get_user_data/', {
        credentials: 'include', // Include cookies in the request
      });
      if (response.ok) {
        const data = await response.json();
        setUserData(data);
      } else {
        console.error('Failed to fetch user data');
      }
    } catch (error) {
      console.error('Error fetching user data:', error);
    }
  };

  useEffect(() => {
    fetchUserData();
  }, []);



  return (
    <>
      <div>
        <button onClick={test}>TEST ROUTE: CLICK & CHECK CONSOLE</button>
        <button onClick={() => (window.location.href = 'http://localhost:8000/steam_login/')}>Login with Steam</button>
        <button onClick={() => (window.location.href = 'http://localhost:8000/logout/')}>Logout</button>
        <button onClick={() => (window.location.href = 'http://localhost:8000/generate_response/')}>Get User Data</button>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
      {userData && (
        <div>
          <h2>User Data</h2>
            <p>Username: {(userData as { username: string }).username}</p>
            <p>Email: {(userData as { email: string }).email}</p>
          <p>Steam ID: {(userData as { steam_id: string }).steam_id}</p>
        </div>
      )}
    </>
  );
};

export default App;
