import {
  MdDashboard,
  MdFolder,
  MdBugReport,
  MdViewKanban,
} from "react-icons/md";

import { NavLink } from "react-router-dom";

import "./Sidebar.css";

const Sidebar = () => {
  return (
    <aside className="sidebar">

      <div className="sidebar-logo">
        <h2>ISMS</h2>
        <span>Issue Tracker</span>
      </div>

      <nav className="sidebar-nav">

        <NavLink to="/dashboard">
          <MdDashboard />
          <span>Dashboard</span>
        </NavLink>

        <NavLink to="/projects">
          <MdFolder />
          <span>Projects</span>
        </NavLink>

        <NavLink to="/issues">
          <MdBugReport />
          <span>Issues</span>
        </NavLink>

        <NavLink to="/sprints">
          <MdViewKanban />
          <span>Sprints</span>
        </NavLink>

      </nav>

    </aside>
  );
};

export default Sidebar;