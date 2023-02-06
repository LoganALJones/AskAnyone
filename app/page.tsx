
import AuthorPage from "./AuthorPage";
import Banner from "./Banner";
import SearchBox from "./SearchBox";

export default function HomePage() {
    return (
        // fetch the chat bot data (profile picture) 
        <div>
        <Banner />
        <SearchBox />
        <AuthorPage/>
        </div>
    );
} 