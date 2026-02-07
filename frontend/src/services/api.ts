// frontend/src/services/api.ts

import { getAuthToken } from './auth';

// Check if we're in a Hugging Face Space environment
const isHuggingFaceSpace = process.env.NEXT_PUBLIC_API_URL?.includes('.hf.space') || false;

// For Hugging Face Spaces, we might need to use a different approach
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || '';

// Generic API request function
const apiRequest = async (endpoint: string, options: RequestInit = {}) => {
  // Ensure the endpoint starts with a slash
  const normalizedEndpoint = endpoint.startsWith('/') ? endpoint : `/${endpoint}`;
  
  // Construct the URL
  let url = `${API_BASE_URL}${normalizedEndpoint}`;

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
    // Log the URL and method being accessed for debugging
    console.log('Making API request to:', url);
    console.log('Method:', options.method || 'GET');
    console.log('Headers:', headers);

    // For Hugging Face Spaces, we might need to handle the request differently
    // Some Hugging Face Spaces might require specific headers or request formatting
    const fetchOptions = {
      ...options,
      headers,
      mode: 'cors', // Enable CORS
      credentials: 'omit', // Don't include cookies in cross-origin requests
      redirect: 'follow' // Follow redirects
    };

    // Make the request
    const response = await fetch(url, fetchOptions);

    // Log the response status for debugging
    console.log('API response status:', response.status);
    
    // Attempt to read response body for debugging (only if response has content)
    let responseBody;
    try {
      if (response.headers.get('content-type')?.includes('application/json')) {
        responseBody = await response.clone().json();
        console.log('API response body:', responseBody);
      } else {
        responseBody = await response.clone().text();
        console.log('API response body (text):', responseBody);
      }
    } catch (e) {
      console.log('Could not parse response body:', e);
    }

    // If we get a 401 or 403, clear auth and redirect to sign in
    if (response.status === 401 || response.status === 403) {
      const errorData = responseBody || await response.json().catch(() => ({}));
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
      // Check if it's a 405 error (Method Not Allowed)
      if (response.status === 405) {
        console.error(`Method not allowed for endpoint: ${url}`);
        console.error('Response body for 405 error:', responseBody);
        
        // Check if this is a critical endpoint that should exist in the full backend
        if (normalizedEndpoint.includes('/api/auth/') || normalizedEndpoint.includes('/api/todos')) {
          console.error(`Critical API endpoint not allowed: ${url}`);
          console.error('This suggests the backend is a simplified version without auth/todo endpoints.');
          
          throw new Error(`Method not allowed for endpoint: ${normalizedEndpoint}. The backend appears to be a simplified version that doesn't include authentication or todo management features. Ensure you're connecting to the full backend implementation with all required endpoints.`);
        }
        
        // For Hugging Face Spaces, this might indicate that the API endpoints are not properly exposed
        // The FastAPI endpoints might not be accessible if only the Gradio interface is exposed
        if (isHuggingFaceSpace) {
          throw new Error(`Method not allowed for endpoint: ${normalizedEndpoint}. This may indicate that the FastAPI endpoints are not properly exposed in the Hugging Face Space. The backend may only be serving the Gradio interface.`);
        } else {
          throw new Error(`Method not allowed for endpoint: ${normalizedEndpoint}. The backend may not support this operation.`);
        }
      }
      // Check if it's a 404 error for specific endpoints that should exist
      if (response.status === 404) {
        // Check if this is a critical endpoint that should exist in the full backend
        if (normalizedEndpoint.includes('/api/auth/') || normalizedEndpoint.includes('/api/todos')) {
          console.error(`Critical API endpoint not found: ${url}`);
          console.error('This suggests the backend might be a simplified version without auth/todo endpoints.');
          
          throw new Error(`API endpoint not found: ${normalizedEndpoint}. The backend may be a simplified version that doesn't include authentication or todo management features. Ensure you're connecting to the full backend implementation.`);
        }
      }
      // For other errors, try to get more details from the response
      let errorMessage = `API request failed: ${response.status} ${response.statusText}`;
      try {
        const errorDetail = responseBody;
        if (errorDetail?.detail) {
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