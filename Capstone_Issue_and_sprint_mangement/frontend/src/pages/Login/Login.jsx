import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useForm } from "react-hook-form";
import { FiEye, FiEyeOff } from "react-icons/fi";

import AuthLayout from "../../components/common/AuthLayout";
import { useAuth } from "../../context/AuthContext";

import "./Login.css";

function Login() {
    const navigate = useNavigate();

    const { login } = useAuth();

    const [showPassword, setShowPassword] = useState(false);
    const [apiError, setApiError] = useState("");

    const {
        register,
        handleSubmit,
        formState: {
            errors,
            isSubmitting,
        },
    } = useForm();

    const onSubmit = async (data) => {
        try {
            setApiError("");

            await login(data);

            navigate("/dashboard");
        } catch (error) {
            setApiError(
                error.response?.data?.detail ||
                "Unable to login. Please try again."
            );
        }
    };

    return (
        <AuthLayout
            title="Welcome Back!"
            subtitle="Sign in to continue to your account."
        >
            <form
                className="login-form"
                onSubmit={handleSubmit(onSubmit)}
            >
                <div className="form-group">

                    <label htmlFor="email">
                        Email
                    </label>

                    <input
                        id="email"
                        type="email"
                        placeholder="Enter your email"
                        className={errors.email ? "input-error" : ""}
                        {...register("email", {
                            required: "Email is required",
                            pattern: {
                                value: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
                                message: "Please enter a valid email address",
                            },
                        })}
                    />

                    {errors.email && (
                        <p className="error-message">
                            {errors.email.message}
                        </p>
                    )}

                </div>

                <div className="form-group">

                    <label htmlFor="password">
                        Password
                    </label>

                    <div className="password-wrapper">

                        <input
                            id="password"
                            type={
                                showPassword
                                    ? "text"
                                    : "password"
                            }
                            placeholder="Enter your password"
                            className={errors.password ? "input-error" : ""}
                            {...register("password", {
                                required: "Password is required",
                                minLength: {
                                    value: 8,
                                    message:
                                        "Password must be at least 8 characters",
                                },
                            })}
                        />

                        <button
                            type="button"
                            className="toggle-password"
                            onClick={() =>
                                setShowPassword(!showPassword)
                            }
                        >
                            {showPassword ? (
                                <FiEyeOff />
                            ) : (
                                <FiEye />
                            )}
                        </button>

                    </div>

                    {errors.password && (
                        <p className="error-message">
                            {errors.password.message}
                        </p>
                    )}

                </div>

                <div className="login-options">

                    <label className="remember-me">

                        <input type="checkbox" />

                        Remember Me

                    </label>

                    <a href="#">
                        Forgot Password?
                    </a>

                </div>

                {apiError && (
                    <p className="error-message">
                        {apiError}
                    </p>
                )}

                <button
                    className="login-btn"
                    type="submit"
                    disabled={isSubmitting}
                >
                    {isSubmitting
                        ? "Signing In..."
                        : "Login"}
                </button>

                <div className="auth-footer">

                    <span>
                        New User?
                    </span>

                    <Link to="/register">
                        Register
                    </Link>

                </div>

            </form>
        </AuthLayout>
    );
}

export default Login;