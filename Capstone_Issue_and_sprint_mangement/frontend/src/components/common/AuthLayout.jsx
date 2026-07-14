import "./AuthLayout.css";

function AuthLayout({
    title,
    subtitle,
    children,
}) {
    return (
        <div className="auth-layout">

            <div className="auth-branding">

                <div className="branding-content">

                    <div className="brand-logo">
                        IS
                    </div>

                    <h1>
                        Issue & Sprint
                        <br />
                        Management System
                    </h1>

                    <p>
                        Plan, Track and Deliver your projects
                        efficiently with a modern issue and
                        sprint management platform.
                    </p>

                </div>

            </div>

            <div className="auth-content">

                <div className="auth-card">

                    <h2>{title}</h2>

                    <p className="auth-subtitle">
                        {subtitle}
                    </p>

                    {children}

                </div>

            </div>

        </div>
    );
}

export default AuthLayout;