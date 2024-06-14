import { Mail, Home, Circle,FileText } from "react-feather";
import pages from './pages'

export default [
  {
    id: "home",
    title: "Home",
    icon: <Home size={20} />,
    navLink: "/home",
  }, ...pages
];
