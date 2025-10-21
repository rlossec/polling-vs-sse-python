# Polling vs SSE Comparison

A demonstration project comparing **Polling** and **Server-Sent Events (SSE)** techniques for real-time user count tracking.

## 🎯 Project Overview

This project simulates a real-time user counter that updates every 2-3 seconds, comparing two different approaches to deliver this data to the frontend:

- **Polling**: Client makes periodic HTTP requests to fetch the latest count
- **SSE**: Server pushes updates to the client via a persistent connection

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager

### Installation & Run

```bash
# Install dependencies
uv sync

# Start the server
uv run app.py
```

The server will start on `http://localhost:8080`

## 📊 Features

### Backend (Flask)

- **Simulated user count**: Randomly fluctuates between 0-200 users
- **Two API endpoints**:
  - `GET /api/count` - Returns current count (for polling)
  - `GET /api/stream` - SSE stream for real-time updates
- **Automatic updates**: User count changes every 2-3 seconds

### Frontend (HTML/JS)

- **Interactive comparison**: Switch between polling and SSE modes
- **Real-time metrics**: Track HTTP requests, bandwidth usage, and timing
- **Visual feedback**: Live counter display with timestamps
- **Request logging**: Monitor all network activity

## 🔧 Technical Details

### Polling Implementation

- Client makes HTTP requests every 2 seconds
- Each request includes full HTTP headers (~600 bytes)
- Server responds with JSON containing count and timestamp

### SSE Implementation

- Single persistent connection established
- Server pushes updates only when count changes
- Minimal overhead after initial connection

### User Count Simulation

The `sim_user_count.py` module simulates realistic user behavior:

- 70% chance: Count changes by -3 to +5 users
- 30% chance: Count remains unchanged
- Bounded between 0 and 200 users

## 📈 Performance Comparison

The frontend tracks and displays:

- **Total HTTP requests**
- **Headers bandwidth usage**
- **Elapsed time**
- **Requests per second**

This allows you to observe the efficiency differences between the two approaches in real-time.

## 🛠️ Project Structure

```
backend/
├── app.py              # Flask server with polling and SSE endpoints
├── sim_user_count.py   # User count simulation logic
├── static/
│   └── index.html      # Frontend comparison interface
├── pyproject.toml      # Project dependencies
└── README.md           # This file
```

## 🎮 Usage

1. Start the server: `uv run app.py`
2. Open `http://localhost:8080` in your browser
3. Click "Start Polling" to test the polling approach
4. Click "Start SSE" to test the server-sent events approach
5. Observe the metrics to compare performance
6. Use "Stop" to halt the current mode

## 🔍 Key Differences

| Aspect              | Polling                       | SSE                          |
| ------------------- | ----------------------------- | ---------------------------- |
| **Connection**      | Multiple short-lived requests | Single persistent connection |
| **Bandwidth**       | Higher (repeated headers)     | Lower (headers sent once)    |
| **Server Load**     | Higher (more requests)        | Lower (fewer connections)    |
| **Real-time**       | Delayed by polling interval   | Near-instant updates         |
| **Browser Support** | Universal                     | Modern browsers only         |

## 📝 Dependencies

- `flask>=3.1.2` - Web framework
- `flask-cors>=6.0.1` - Cross-origin resource sharing
