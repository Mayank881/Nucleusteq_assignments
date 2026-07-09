import api from "./api";

const projectService = {
  getAllProjects() {
    return api.get("/projects");
  },
};

export default projectService;