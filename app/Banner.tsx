import SearchBox from "./SearchBox";

function Banner() {
  return (
    <div className="flex flex-col lg:space-x-5 lg:ml-20 justify-between items-center font-bold px-10 py-5 mb-3">
      <h1 className="text-6xl">Search Books</h1>
      <h2 className = "mt-5 md:mt-0"> Leverage AI to get information that is more relevant to your questions.
</h2>
    </div>
  );
}

export default Banner;