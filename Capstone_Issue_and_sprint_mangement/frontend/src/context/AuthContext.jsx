import { createContext, useContext, useEffect, useState } from "react";

import authService from "../services/authService";

const AuthContext = createContext();

export function AuthProvider({ children }) {
    const [user, setUser] = useState(null);
    const [token, setToken] = useState(
        localStorage.getItem("token")
    );
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const initializeAuth = async () => {
            if (!token) {
                setLoading(false);
                return;
            }

            try {
                const currentUser =
                    await authService.getCurrentUser();

                setUser(currentUser);
            } catch (error) {
                console.error(error);

                localStorage.removeItem("token");
                localStorage.removeItem("user");

                setToken(null);
                setUser(null);
            } finally {
                setLoading(false);
            }
        };

        initializeAuth();
    }, [token]);

    const login = async (loginData) => {
        const response =
            await authService.login(loginData);

        localStorage.setItem(
            "token",
            response.access_token
        );

        setToken(response.access_token);

        const currentUser =
            await authService.getCurrentUser();

        localStorage.setItem(
            "user",
            JSON.stringify(currentUser)
        );

        setUser(currentUser);
    };

    const logout = () => {
        localStorage.removeItem("token");
        localStorage.removeItem("user");

        setToken(null);
        setUser(null);
    };

    const value = {
        user,
        token,
        loading,
        login,
        logout,
        isAuthenticated: !!token,
    };

    return (
        <AuthContext.Provider value={value}>
            {children}
        </AuthContext.Provider>
    );
}


export function useAuth() {
    return useContext(AuthContext);
}

export default AuthProvider;