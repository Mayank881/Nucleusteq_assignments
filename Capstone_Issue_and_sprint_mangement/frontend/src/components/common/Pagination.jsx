import "./Pagination.css";
const Pagination = ({
    currentPage,
    totalPages,
    onPrevious,
    onNext,
}) => {
    if (totalPages <= 1) {
        return null;
    }

    return (
        <div className="pagination">
            <button
                onClick={onPrevious}
                disabled={currentPage === 1}
            >
                Previous
            </button>

            <span>
                Page {currentPage} of {totalPages}
            </span>

            <button
                onClick={onNext}
                disabled={currentPage === totalPages}
            >
                Next
            </button>
        </div>
    );
};

export default Pagination;