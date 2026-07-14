import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useForm } from "react-hook-form";
import { FiEye, FiEyeOff } from "react-icons/fi";

import AuthLayout from "../../components/common/AuthLayout";
import authService from "../../services/authService";

import "./Register.css";

function Register() {
    const navigate = useNavigate();

    const [showPassword, setShowPassword] = useState(false);
    const [showConfirmPassword, setShowConfirmPassword] = useState(false);
    const [apiError, setApiError] = useState("");

    const {
        register,
        handleSubmit,
        watch,
        reset,
        formState: {
            errors,
            isSubmitting,
        },
    } = useForm({
        defaultValues: {
            role: "member",
        },
    });

    const password = watch("password");

    const onSubmit = async (data) => {
        try {
            setApiError("");

            const payload = {
                name: data.name,
                email: data.email,
                password: data.password,
                role: data.role,
            };

            await authService.register(payload);

            alert("Registration Successful");

            reset();

            navigate("/login");
        } catch (error) {
            setApiError(
                error.response?.data?.detail ||
                "Registration failed."
            );
        }
    };

    return (
        <AuthLayout
            title="Create Account"
            subtitle="Create your account to start managing projects."
        >
            <form
                className="register-form"
                onSubmit={handleSubmit(onSubmit)}
            >
                <div className="form-group">
                    <label htmlFor="name">
                        Full Name
                    </label>

                    <input
                        id="name"
                        type="text"
                        placeholder="Enter your full name"
                        className={errors.name ? "input-error" : ""}
                        {...register("name", {
                            required: "Name is required",
                            minLength: {
                                value: 2,
                                message: "Minimum 2 characters required",
                            },
                        })}
                    />

                    {errors.name && (
                        <p className="error-message">
                            {errors.name.message}
                        </p>
                    )}
                </div>

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
                                message:
                                    "Please enter a valid email address",
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
                            placeholder="Enter password"
                            className={
                                errors.password
                                    ? "input-error"
                                    : ""
                            }
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

                <div className="form-group">
                    <label htmlFor="confirmPassword">
                        Confirm Password
                    </label>

                    <div className="password-wrapper">
                        <input
                            id="confirmPassword"
                            type={
                                showConfirmPassword
                                    ? "text"
                                    : "password"
                            }
                            placeholder="Confirm Password"
                            className={
                                errors.confirmPassword
                                    ? "input-error"
                                    : ""
                            }
                            {...register("confirmPassword", {
                                required:
                                    "Confirm Password is required",
                                validate: (value) =>
                                    value === password ||
                                    "Passwords do not match",
                            })}
                        />

                        <button
                            type="button"
                            className="toggle-password"
                            onClick={() =>
                                setShowConfirmPassword(
                                    !showConfirmPassword
                                )
                            }
                        >
                            {showConfirmPassword ? (
                                <FiEyeOff />
                            ) : (
                                <FiEye />
                            )}
                        </button>
                    </div>

                    {errors.confirmPassword && (
                        <p className="error-message">
                            {errors.confirmPassword.message}
                        </p>
                    )}
                </div>

                <div className="form-group">
                    <label htmlFor="role">
                        Role
                    </label>

                    <select
                        id="role"
                        className={errors.role ? "input-error" : ""}
                        {...register("role", {
                            required: "Please select a role",
                        })}
                    >
                        <option value="member">
                            Member
                        </option>

                        <option value="viewer">
                            Viewer
                        </option>
                    </select>

                    {errors.role && (
                        <p className="error-message">
                            {errors.role.message}
                        </p>
                    )}
                </div>

                {apiError && (
                    <p className="error-message">
                        {apiError}
                    </p>
                )}

                <button
                    type="submit"
                    className="register-btn"
                    disabled={isSubmitting}
                >
                    {isSubmitting
                        ? "Creating..."
                        : "Create Account"}
                </button>

                <div className="auth-footer">
                    <span>
                        Already have an account?
                    </span>

                    <Link to="/login">
                        Login
                    </Link>
                </div>
            </form>
        </AuthLayout>
    );
}

export default Register;