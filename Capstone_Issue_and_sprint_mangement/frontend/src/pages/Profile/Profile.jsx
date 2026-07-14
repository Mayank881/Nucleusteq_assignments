import { useEffect, useState } from "react";
import api from "../../services/api";

import "./Profile.css";

const Profile = () => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetchProfile();
    }, []);

    const fetchProfile = async () => {
        try {
            const response = await api.get("/users/me");
            setUser(response.data);
        } catch (error) {
            console.error("Failed to load profile", error);
        } finally {
            setLoading(false);
        }
    };

    if (loading) {
        return (
            <div className="profile-page">
                <p>Loading...</p>
            </div>
        );
    }
    return (
    <div className="profile-page">

        <h1 className="profile-title">
            My Profile
        </h1>

        <p className="profile-subtitle">
            View your account details.
        </p>

        <div className="profile-card-wrapper">

            <div className="profile-card">

                <div className="profile-avatar">
                    {user?.name?.charAt(0).toUpperCase()}
                </div>

                <div className="profile-row">
                    <span className="label">Name</span>
                    <span className="value">{user?.name}</span>
                </div>

                <div className="profile-row">
                    <span className="label">Email</span>
                    <span className="value">{user?.email}</span>
                </div>

                <div className="profile-row">
                    <span className="label">Role</span>
                    <span className="role">{user?.role}</span>
                </div>

            </div>

        </div>

    </div>
  );
};

export default Profile;