import "./App.css";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import HomePage from "./components/HomePage";
import Login from "./components/Login";
import Signup from "./components/Signup";

const router = createBrowserRouter([
  {
    path: "/", // Path of the route
    element: <HomePage />, // Component to render when the path is matched
  },
  {
    path: "/register", // Path of the route
    element: <Signup />, // Component to render when the path is matched
  },
  {
    path: "/login", // Path of the route
    element: <Login />, // Component to render when the path is matched
  },
]);

function App() {
  return (
    <div className="p-4 h-screen flex items-center justify-center">
      <RouterProvider router={router} />
    </div>
  );
}

export default App;
