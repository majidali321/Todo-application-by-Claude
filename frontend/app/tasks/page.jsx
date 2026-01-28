import React, { useState, useEffect } from 'react';
import { auth } from '../../lib/auth';
import { apiClient } from '../../utils/api';
import TaskList from '../../components/TaskList';
import TaskForm from '../../components/TaskForm';

export default function TasksPage() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [editingTask, setEditingTask] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [currentUser, setCurrentUser] = useState(null);

  useEffect(() => {
    const getUserAndTasks = async () => {
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

        // Fetch tasks for the user
        const userTasks = await apiClient.fetchTasks(session.user.id);
        setTasks(userTasks);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    getUserAndTasks();
  }, []);

  const handleCreateTask = async (taskData) => {
    try {
      const newTask = await apiClient.createTask(currentUser.id, taskData);
      setTasks([...tasks, newTask]);
      setShowForm(false);
    } catch (err) {
      setError(err.message);
    }
  };

  const handleUpdateTask = async (taskData) => {
    try {
      const updatedTask = await apiClient.updateTask(currentUser.id, editingTask.id, taskData);
      setTasks(tasks.map(t => t.id === editingTask.id ? updatedTask : t));
      setEditingTask(null);
      setShowForm(false);
    } catch (err) {
      setError(err.message);
    }
  };

  const handleDeleteTask = async (task) => {
    if (window.confirm('Are you sure you want to delete this task?')) {
      try {
        await apiClient.deleteTask(currentUser.id, task.id);
        setTasks(tasks.filter(t => t.id !== task.id));
      } catch (err) {
        setError(err.message);
      }
    }
  };

  const handleToggleComplete = async (task) => {
    try {
      const updatedTask = await apiClient.toggleTaskComplete(currentUser.id, task.id);
      setTasks(tasks.map(t => t.id === task.id ? updatedTask : t));
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

  return (
    <div className="container mx-auto p-4">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold">My Tasks</h1>
        <button
          onClick={() => {
            setEditingTask(null);
            setShowForm(true);
          }}
          className="px-4 py-2 bg-green-500 text-white rounded-md hover:bg-green-600"
        >
          Add New Task
        </button>
      </div>

      {showForm ? (
        <div className="mb-6">
          <TaskForm
            onSubmit={editingTask ? handleUpdateTask : handleCreateTask}
            initialData={editingTask}
            onCancel={() => {
              setShowForm(false);
              setEditingTask(null);
            }}
          />
        </div>
      ) : null}

      {tasks.length > 0 ? (
        <TaskList
          tasks={tasks}
          onEdit={(task) => {
            setEditingTask(task);
            setShowForm(true);
          }}
          onDelete={handleDeleteTask}
          onToggle={handleToggleComplete}
        />
      ) : (
        <div className="text-center py-8 text-gray-500">
          No tasks yet. Click "Add New Task" to get started!
        </div>
      )}
    </div>
  );
}