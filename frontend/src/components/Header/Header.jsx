import { Link } from "react-router-dom";

const Header = () => {
  return (
    <header className="py-5 px-10 border-b-2 border-b-alto">
      <nav className="font-bold flex items-center justify-between">
        <Link to="/">
          <h1 className="text-3xl">EqualInk</h1>
        </Link>
        <div className="flex items-center gap-14">
          <Link
            className="text-xl border-2 border-transparent hover:border-b-black"
            to="/writingassistant"
          >
            Writing assistant
          </Link>
          <Link
            className="text-xl border-2 border-transparent hover:border-b-black"
            to="/"
          >
            Education
          </Link>
          <Link
            className="text-xl border-2 border-transparent hover:border-b-black"
            to="/"
          >
            Trends
          </Link>
        </div>
      </nav>
    </header>
  );
};

export default Header;
