import api from "./api";

const issueService = {
  getAllIssues() {
    return api.get("/issues");
  },
};

export default issueService;