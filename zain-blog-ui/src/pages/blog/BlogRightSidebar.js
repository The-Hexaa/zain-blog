import { Fragment, useState, useEffect } from "react"; 
import { useLocation } from "react-router-dom"; 
import SEO from "../../components/seo";
import LayoutOne from "../../layouts/LayoutOne";
import Breadcrumb from "../../wrappers/breadcrumb/Breadcrumb";
import BlogSidebar from "../../wrappers/blog/BlogSidebar";
import BlogPagination from "../../wrappers/blog/BlogPagination";
import BlogPosts from "../../wrappers/blog/BlogPosts";

const BlogRightSidebar = () => {
  const [totalPages, setTotalPages] = useState(0);
  const [posts, setPosts] = useState([]);
  const [selectedTags, setSelectedTags] = useState([]);
  const [selectedCategories, setSelectedCategories] = useState([]);
  const [search, setSearch] = useState(null);
  const { pathname } = useLocation();

  const fetchData = async (page = 1) => {
    console.log("fetching", page);
    try {
      let tags = selectedTags && selectedTags.length > 0 ? '&tags=[' + selectedTags+ ']': "";
      let categories = selectedCategories && selectedCategories.length > 0 ? '&category=[' + selectedCategories+ ']': "";
      console.log("search",search);

      const url = `http://127.0.0.1:8000/blog/posts/?p=${page}${search && search.length > 0 ? search : ''}${tags && tags.length > 0 ? tags : ''}${categories && categories.length > 0 ? categories : ''}`;
      console.log(url);
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error("Failed to fetch data");
      }
      const sData = await response.json();
      const data = sData.results;
      // for (const post of data){
      // }
      console.log("data result")
      console.log(data)
      setPosts(data);
      setTotalPages(sData.total_pages);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  useEffect(() => {
    fetchData();
  }, [selectedTags, selectedCategories, search]);

  const handlePageChange = (page) => {
    fetchData(page);
  };
  const handleFilterChange = (filterType, filterId) => {
    if (filterType === "tag") {
      setSelectedTags(filterId);
    }
    else if (filterType === "category") {
      setSelectedCategories(filterId);
    } else if (filterType === "search"){
      // console.log("search",filterId);
      setSearch(filterId);
    }
  };
  
  return (
    <Fragment>
      <SEO
        titleTemplate="Blog"
        description="Blog of flone react minimalist eCommerce template."
      />
      <LayoutOne headerTop="visible">
        {/* breadcrumb */}
        <Breadcrumb
          pages={[
            { label: "Home", path: process.env.PUBLIC_URL + "/" },
            { label: "Blog", path: process.env.PUBLIC_URL + pathname },
          ]}
        />
        <div className="blog-area pt-100 pb-100">
          <div className="container">
            <div className="row flex-row-reverse">
            <div className="col-lg-3">
                {/* blog sidebar */}
                <BlogSidebar onFilterChange={handleFilterChange} />
              </div>
              <div className="col-lg-9">
                <div className="ml-20">
                  <div className="row">
                    {/* blog posts */}
                    <BlogPosts posts={posts} />
                  </div>

                  {/* blog pagination */}
                  <BlogPagination
                    totalPages={totalPages}
                    onPageChange={handlePageChange}
                  />
                </div>
              </div>
              
            </div>
          </div>
        </div>
      </LayoutOne>
    </Fragment>
  );
};

export default BlogRightSidebar;