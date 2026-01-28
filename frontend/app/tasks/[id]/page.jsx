import React, { useState, useEffect } from 'react';
import { auth } from '../../../lib/auth';
import { apiClient } from '../../../utils/api';

export default function EditTaskPage({ params }) {
  const { id } = params;
  const [task, setTask] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [completed, setCompleted] = useState(false);
  const [currentUser, setCurrentUser] = useState(null);

  useEffect(() => {
    const getTaskAndUser = async () => {
      try {
        // Get current user session
        const session = await auth.getSession();
        if (!session) {
          window.location.href = '/signin';
          return;
        }

        setCurrentUser(session.user);

        // Set token for API requests
        const token = session.accessToken; // Assuming JWT token is available here
        apiClient.setToken(token);

        // Fetch the specific task
        const taskData = await apiClient.getTask(session.user.id, id);
        setTask(taskData);
        setTitle(taskData.title);
        setDescription(taskData.description || '');
        setCompleted(taskData.completed);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    if (id) {
      getTaskAndUser();
    }
  }, [id]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const updatedTask = await apiClient.updateTask(currentUser.id, parseInt(id), {
        title,
        description,
        completed
      });

      // Redirect back to tasks list
      window.location.href = '/tasks';
    } catch (err) {
      setError(err.message);
    }
  };

  if (loading) {
    return <div className="container mx-auto p-4">Loading...</div>;
  }

  if (error) {
    return (
      <div className="container mx-auto p-4">
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded">
          Error: {error}
        </div>
      </div>
    );
  }

  if (!task) {
    return (
      <div className="container mx-auto p-4">
        <div className="text-red-500">Task not found</div>
      </div>
    );
  }

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-6">Edit Task</h1>

      <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow-md max-w-2xl">
        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
            {error}
          </div>
        )}

        <div className="mb-4">
          <label htmlFor="title" className="block text-sm font-medium text-gray-700 mb-1">
            Title *
          </label>
          <input
            type="text"
            id="title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Enter task title"
          />
        </div>

        <div className="mb-4">
          <label htmlFor="description" className="block text-sm font-medium text-gray-700 mb-1">
            Description
          </label>
          <textarea
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            rows="3"
            placeholder="Enter task description (optional)"
          />
        </div>

        <div className="mb-4">
          <label className="inline-flex items-center">
            <input
              type="checkbox"
              checked={completed}
              onChange={(e) => setCompleted(e.target.checked)}
              className="rounded border-gray-300 text-blue-600 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50"
            />
            <span className="ml-2 text-sm text-gray-700">Completed</span>
          </label>
        </div>

        <div className="flex justify-end space-x-3">
          <a
            href="/tasks"
            className="px-4 py-2 border border-gray-300 rounded-md text-gray-700 hover:bg-gray-50"
          >
            Cancel
          </a>
          <button
            type="submit"
            className="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600"
          >
            Update Task
          </button>
        </div>
      </form>
    </div>
  );
}