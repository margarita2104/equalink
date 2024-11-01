import { BrowserRouter, Route, Routes } from "react-router-dom";
import Header from "../components/Header/Header";
import Home from "./Home/Home";


const PageRoutes = () => {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        {/* <Route path="/chatbot" element={<Chatbot />} /> */}
      </Routes>
    </BrowserRouter>
  );
};

export default PageRoutes;