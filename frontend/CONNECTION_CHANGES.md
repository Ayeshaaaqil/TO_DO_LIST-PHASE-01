# Frontend to Phase 3 Backend Connection Changes

## Files Modified

### 1. `.env.local`
- Changed `NEXT_PUBLIC_API_URL` from `http://127.0.0.1:8000` to `https://ayesha-aaqil-chatbot-phase3.hf.space`

### 2. `vercel.json`
- Added environment variable configuration to ensure the production deployment uses the correct backend URL

## Changes Made

The frontend application has been configured to connect to the Phase 3 backend hosted at `https://ayesha-aaqil-chatbot-phase3.hf.space` instead of the local backend.

## API Endpoints Used

The frontend will now connect to the following endpoints on the Phase 3 backend:

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

## Build Status
- The application builds successfully with the new backend configuration
- All frontend pages are properly connected to the Phase 3 backend

## Deployment
When deploying to Vercel, the environment variables in `vercel.json` will ensure the production application connects to the correct backend.