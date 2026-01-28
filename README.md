# TodoApp - Full-Stack Application

A modern full-stack todo application built with Next.js, FastAPI, SQLModel, Better Auth, and Neon Postgres.

## Features

- ✅ Multi-user support with secure authentication
- ✅ JWT-based authentication with Better Auth
- ✅ Complete CRUD operations for todos
- ✅ User data isolation and privacy
- ✅ Responsive frontend with Next.js
- ✅ RESTful API with FastAPI
- ✅ SQLModel for database modeling
- ✅ Neon Postgres for cloud database
- ✅ Monorepo structure with workspaces

## Tech Stack

- **Frontend**: Next.js 14+ with App Router
- **Backend**: FastAPI with Python 3.9+
- **Database**: Neon Postgres (SQLModel/SQLAlchemy)
- **Authentication**: Better Auth with JWT
- **Monorepo**: npm workspaces
- **Deployment**: Vercel (frontend), Railway/Hatchbox (backend)

## Prerequisites

- [Node.js](https://nodejs.org/) (v18+)
- [npm](https://www.npmjs.com/) (v8+)
- [UV](https://github.com/astral-sh/uv) (Python package manager)
- [Python](https://www.python.org/) (v3.9+)

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/todoapp.git
   cd todoapp
   ```

2. **Install dependencies:**
   ```bash
   # Install root dependencies and workspace dependencies
   npm run setup
   ```

3. **Set up environment variables:**
   ```bash
   # Copy the example .env file and update values
   cp .env.example .env
   ```

   Update the `.env` file with your actual database URL and auth secret:
   - `DATABASE_URL`: Your Neon Postgres connection string
   - `BETTER_AUTH_SECRET`: A secure random secret for JWT signing

4. **Run the development servers:**
   ```bash
   # Start both frontend and backend in development mode
   npm run dev
   ```

   The applications will start on:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000

## Development Scripts

- `npm run setup` - Install all dependencies for root, frontend, and backend
- `npm run dev` - Start both frontend and backend development servers
- `npm run dev:frontend` - Start only the frontend development server
- `npm run dev:backend` - Start only the backend development server
- `npm run build` - Build the frontend application
- `npm run start` - Start both applications in production mode

## Project Structure

```
todoapp/
├── .env                    # Environment variables
├── package.json           # Root package with workspaces
├── README.md              # This file
├── frontend/              # Next.js frontend application
└── backend/               # FastAPI backend application
```

## Database Setup

1. Sign up for a [Neon account](https://neon.tech/)
2. Create a new project
3. Copy the connection string and add it to your `.env` file as `DATABASE_URL`

## Authentication

The application uses Better Auth for authentication:
- Users can register and login securely
- JWT tokens are used for session management
- Protected routes ensure user data isolation

## Deployment

### Frontend (Next.js) - Vercel
1. Connect your repository to [Vercel](https://vercel.com/)
2. Set the Root Directory to `frontend` in Vercel project settings
3. Set environment variables in Vercel dashboard:
   - `NEXT_PUBLIC_API_BASE_URL`: Your backend API URL (e.g., https://your-backend.onrender.com)
4. Deploy automatically on push to main branch

### Backend (FastAPI) - Railway/Render
1. Connect your repository to [Railway](https://railway.app/) or [Render](https://render.com/)
2. Set the Root Directory to `backend` in the platform settings
3. Set environment variables:
   - `DATABASE_URL`: Your Neon Postgres connection string
   - `BETTER_AUTH_SECRET`: Your JWT secret
4. Configure the deployment to run `uvicorn src.main:app --host 0.0.0.0 --port $PORT`

### Alternative Deployment Approach
If you want to deploy the frontend to Vercel while keeping the backend separate:

1. Create a new branch specifically for frontend deployment:
   ```bash
   git checkout -b frontend-deploy
   # Move frontend contents to root (optional)
   ```

2. Or configure Vercel to use the `frontend` directory as the root for building.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues, please open an issue in the GitHub repository or contact the maintainers.