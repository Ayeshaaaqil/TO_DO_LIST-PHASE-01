// frontend/src/services/api.ts

import { getAuthToken } from './auth';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || '';

// Generic API request function
const apiRequest = async (endpoint: string, options: RequestInit = {}) => {
  // Ensure the endpoint starts with a slash
  const normalizedEndpoint = endpoint.startsWith('/') ? endpoint : `/${endpoint}`;
  
  // For Hugging Face Spaces, the API might need to be accessed differently
  // If the API_BASE_URL ends with .hf.space, we might need to handle it specially
  let url = `${API_BASE_URL}${normalizedEndpoint}`;
  
  // Check if we're calling the backend on Hugging Face Spaces
  if (API_BASE_URL.includes('.hf.space')) {
    // For Hugging Face Spaces, sometimes the API endpoints need to be accessed differently
    // The FastAPI endpoints might be available at a different path
    // Try to construct the URL appropriately
    url = `${API_BASE_URL}${normalizedEndpoint}`;
  }

  const headers = {
    'Content-Type': 'application/json',
    ...options.headers,
  };

  // Add auth token if available - get the latest token
  const token = getAuthToken();
  if (token) {
    (headers as any)['Authorization'] = `Bearer ${token}`;
  }

  try {
    // Log the URL being accessed for debugging
    console.log('Making API request to:', url);

    const response = await fetch(url, {
      ...options,
      headers,
      mode: 'cors', // Enable CORS
      credentials: 'omit', // Don't include cookies in cross-origin requests
      redirect: 'follow' // Follow redirects
    });

    // Log the response status for debugging
    console.log('API response status:', response.status);

    // If we get a 401 or 403, clear auth and redirect to sign in
    if (response.status === 401 || response.status === 403) {
      const errorData = await response.json().catch(() => ({}));
      console.error('Authentication error:', errorData);

      // Clear authentication state
      await import('./auth').then(auth => auth.clearAuth());

      // Redirect to sign in (in a browser environment)
      if (typeof window !== 'undefined') {
        window.location.href = '/signin';
      }

      throw new Error(`Authentication failed: ${response.status} ${response.statusText}`);
    }

    if (!response.ok) {
      // Check if it's a 404 error and provide more specific messaging
      if (response.status === 404) {
        console.error(`API endpoint not found: ${url}`);
        throw new Error(`API endpoint not found: ${normalizedEndpoint}. Please check if the backend service is running correctly.`);
      }
      // For other errors, try to get more details from the response
      let errorMessage = `API request failed: ${response.status} ${response.statusText}`;
      try {
        const errorDetail = await response.json();
        if (errorDetail.detail) {
          errorMessage += ` - Detail: ${errorDetail.detail}`;
        }
      } catch (e) {
        // If we can't parse the error response, use the generic message
      }
      throw new Error(errorMessage);
    }

    return response.json();
  } catch (error: any) {
    console.error('API request error:', error);
    if (error instanceof TypeError && error.message.includes('fetch')) {
      // This usually indicates a network error or CORS issue
      throw new Error('Failed to connect to server. This could be due to network issues or CORS policy. Please check if the backend service is running and accessible.');
    }
    throw error;
  }
};

// Authentication API functions
export const authAPI = {
  signup: async (email: string, password: string, name?: string) => {
    try {
      const response = await fetch(`${API_BASE_URL}/api/auth/signup`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password, name }),
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || `Signup failed: ${response.status} ${response.statusText}`);
      }

      return response.json();
    } catch (error: any) {
      if (error.name === 'TypeError' && error.message.includes('fetch')) {
        throw new Error('Failed to connect to server. Please check your connection and try again.');
      }
      throw error;
    }
  },

  signin: async (email: string, password: string) => {
    try {
      const response = await fetch(`${API_BASE_URL}/api/auth/signin`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || `Signin failed: ${response.status} ${response.statusText}`);
      }

      return response.json();
    } catch (error: any) {
      if (error.name === 'TypeError' && error.message.includes('fetch')) {
        throw new Error('Failed to connect to server. Please check your connection and try again.');
      }
      throw error;
    }
  },

  signout: async () => {
    const response = await fetch(`${API_BASE_URL}/api/auth/signout`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      throw new Error('Signout failed');
    }

    return response.json();
  },
};

// Todo API functions
export const todoAPI = {
  getTodos: async () => {
    return apiRequest('/api/todos');
  },

  createTodo: async (title: string, description?: string) => {
    return apiRequest('/api/todos', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        title: title,
        description: description || ""  // Ensure description is not undefined
      }),
    });
  },

  updateTodo: async (id: string, updates: { title?: string; description?: string }) => {
    return apiRequest(`/api/todos/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        title: updates.title,
        description: updates.description || ""
      }),
    });
  },

  toggleTodoComplete: async (id: string, isCompleted: boolean) => {
    return apiRequest(`/api/todos/${id}/complete`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ is_completed: isCompleted }),
    });
  },

  deleteTodo: async (id: string) => {
    return apiRequest(`/api/todos/${id}`, {
      method: 'DELETE',
    });
  },
};

// Chat API functions
export const chatAPI = {
  sendMessage: async (message: string, conversationId?: string) => {
    return apiRequest('/api/chat', {
      method: 'POST',
      body: JSON.stringify({
        message,
        conversation_id: conversationId || null
      }),
    });
  },
};