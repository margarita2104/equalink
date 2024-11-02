import { BrowserRouter, Route, Routes } from "react-router-dom";
import Header from "../components/Header/Header";
import Home from "./Home/Home";
import WritingAssistant from "./WritingAssistant/WritingAssistant";
import Education from "./Education/Education";
import Trends from "./Trends/Trends";


const PageRoutes = () => {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/writingassistant" element={<WritingAssistant />} />
        <Route path="/education" element={<Education />} />
        <Route path="/trends" element={<Trends />} />
      </Routes>
    </BrowserRouter>
  );
};

export default PageRoutes;