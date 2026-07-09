import { useNavigate } from "react-router-dom";

import { useAuth } from "../../context/AuthContext";

import "./Header.css";

function Header() {
    const navigate = useNavigate();

    const {
        user,
        logout,
    } = useAuth();

    const handleLogout = () => {
        logout();
        navigate("/login", {
            replace: true,
        });
    };

    return (
        <header className="header">

            <div>
                <h2>
                    Issue & Sprint Management System
                </h2>
            </div>

            <div className="header-user">

                <div className="user-avatar">
                    {user?.name
                        ? user.name.charAt(0).toUpperCase()
                        : "U"}
                </div>

                <div className="user-details">

                    <h4>
                        {user?.name || "User"}
                    </h4>

                    <small>
                        {user?.role || "Member"}
                    </small>

                </div>

                <button
                    className="logout-btn"
                    onClick={handleLogout}
                >
                    Logout
                </button>

            </div>

        </header>
    );
}

export default Header;