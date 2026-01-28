// Mock authentication client for the Todo App
// In a real implementation, you would use a proper auth library

class MockAuthClient {
  constructor(config) {
    this.baseURL = config.baseURL;
    this.secret = config.plugins?.[0]?.secret || "fallback-secret";
  }

  async signIn(provider, options) {
    // Mock sign in implementation
    return { user: { id: "mock-user-id", name: "Mock User" }, session: "mock-session-token" };
  }

  async signOut() {
    // Mock sign out implementation
    localStorage.removeItem('authToken');
    return { success: true };
  }

  async getSession() {
    // Get session from localStorage or return null
    const token = localStorage.getItem('authToken');
    if (token) {
      // Decode and return user info (simplified)
      return { user: { id: "mock-user-id" }, expiresAt: Date.now() + 3600000 }; // 1 hour from now
    }
    return null;
  }

  async getToken() {
    return localStorage.getItem('authToken');
  }
}

export const auth = new MockAuthClient({
  baseURL: process.env.NEXT_PUBLIC_BASE_URL || "http://localhost:3000",
});