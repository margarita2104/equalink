import { BrowserRouter, Route, Routes } from "react-router-dom";
import Header from "../components/Header/Header";
import Home from "./Home/Home";
import WritingAssistant from "./WritingAssistant/WritingAssistant";


const PageRoutes = () => {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/writingassistant" element={<WritingAssistant />} />
      </Routes>
    </BrowserRouter>
  );
};

export default PageRoutes;