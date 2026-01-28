import React from 'react';
import './globals.css';

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-gray-100">
        <nav className="bg-white shadow">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between h-16">
              <div className="flex items-center">
                <h1 className="text-xl font-bold text-gray-900">Todo App</h1>
              </div>
              <div className="flex items-center space-x-4">
                <a href="/" className="text-gray-700 hover:text-blue-600">Home</a>
                <a href="/tasks" className="text-gray-700 hover:text-blue-600">Tasks</a>
                <a href="/signin" className="text-gray-700 hover:text-blue-600">Sign In</a>
                <a href="/signup" className="text-gray-700 hover:text-blue-600">Sign Up</a>
              </div>
            </div>
          </div>
        </nav>

        <main className="container mx-auto py-6">
          {children}
        </main>
      </body>
    </html>
  );
}