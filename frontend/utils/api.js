const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";

class ApiClient {
  constructor() {
    this.token = null;
  }

  setToken(token) {
    this.token = token;
  }

  async request(endpoint, options = {}) {
    const headers = {
      "Content-Type": "application/json",
      ...options.headers,
    };

    if (this.token) {
      headers.Authorization = `Bearer ${this.token}`;
    }

    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      ...options,
      headers,
    });

    if (!response.ok) {
      throw new Error(`API request failed: ${response.status} ${response.statusText}`);
    }

    return response.json();
  }

  // Task API methods
  async fetchTasks(userId) {
    return this.request(`/api/${userId}/tasks`);
  }

  async createTask(userId, taskData) {
    return this.request(`/api/${userId}/tasks`, {
      method: "POST",
      body: JSON.stringify(taskData),
    });
  }

  async getTask(userId, taskId) {
    return this.request(`/api/${userId}/tasks/${taskId}`);
  }

  async updateTask(userId, taskId, taskData) {
    return this.request(`/api/${userId}/tasks/${taskId}`, {
      method: "PUT",
      body: JSON.stringify(taskData),
    });
  }

  async deleteTask(userId, taskId) {
    return this.request(`/api/${userId}/tasks/${taskId}`, {
      method: "DELETE",
    });
  }

  async toggleTaskComplete(userId, taskId) {
    return this.request(`/api/${userId}/tasks/${taskId}/complete`, {
      method: "PATCH",
    });
  }
}

export const apiClient = new ApiClient();