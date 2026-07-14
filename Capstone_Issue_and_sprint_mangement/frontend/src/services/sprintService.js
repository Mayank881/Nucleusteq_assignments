import api from "./api";

const sprintService = {
  getAllSprints() {
    return api.get("/sprints");
  },
};

export default sprintService;