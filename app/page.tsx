import AuthorPage from "./AuthorPage";
import Banner from "./Banner";
import SearchBox from "./SearchBox";
import DropResume from "./DropResume";

export default function HomePage() {
  return (
    <div>
      <Banner />
      <SearchBox />
      <AuthorPage />
      <DropResume message="Drop your resume here" />
    </div>
  );
}
