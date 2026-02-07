# Connection Information for Phase 3 Backend

## Frontend to Backend Connection

The frontend application has been configured to connect to the Phase 3 backend at:
`https://ayesha-aaqil-chatbot-phase3.hf.space`

## Configuration Changes Made

### 1. Environment Variables
- Updated `NEXT_PUBLIC_API_URL` in `.env.local` to point to the Phase 3 backend

### 2. Vercel Configuration
- Updated `vercel.json` to include environment variables for production deployment

### 3. API Service
- The frontend's API service (`src/services/api.ts`) now connects to the external backend
- All API calls (authentication, todo management, chat) are directed to the Phase 3 backend

## API Endpoints Used

The frontend connects to the following endpoints on the Phase 3 backend:

- Authentication:
  - `POST https://ayesha-aaqil-chatbot-phase3.hf.space/api/auth/signup`
  - `POST https://ayesha-aaqil-chatbot-phase3.hf.space/api/auth/signin`
  - `POST https://ayesha-aaqil-chatbot-phase3.hf.space/api/auth/signout`

- Todo Management:
  - `GET https://ayesha-aaqil-chatbot-phase3.hf.space/api/todos`
  - `POST https://ayesha-aaqil-chatbot-phase3.hf.space/api/todos`
  - `PUT https://ayesha-aaqil-chatbot-phase3.hf.space/api/todos/{id}`
  - `PATCH https://ayesha-aaqil-chatbot-phase3.hf.space/api/todos/{id}/complete`
  - `DELETE https://ayesha-aaqil-chatbot-phase3.hf.space/api/todos/{id}`

- Chat Interface:
  - `POST https://ayesha-aaqil-chatbot-phase3.hf.space/api/chat`

## Deployment

The frontend is deployed at:
`https://frontend-hsuq2kvkg-ayesha-aaqils-projects.vercel.app/`

## Build Status

The application builds successfully with the new backend configuration:
- All pages build correctly
- API connections are properly configured
- Environment variables are set for both development and production