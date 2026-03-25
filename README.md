# Pomodoro Timer

A desktop Pomodoro timer application built with PyQt6 that helps you stay focused with the Pomodoro Technique.

## Features:
- 25-minute work sessions
- 5-minute break sessions
- Automatic switching between work and break
- Session counter that persists across app restarts
- Start, pause, and reset controls
- Visual indicators for work/break mode
- Color-coded buttons (green=start, cyan=pause, red=reset)

## How to use:
1. Install PyQt6: `pip install PyQt6`
2. Run `python pomodoro-timer.py`
3. Click "Start" to begin a 25-minute work session
4. Timer automatically switches to a 5-minute break when work ends
5. After break, automatically starts a new work session and increments counter
6. Use "Pause" to stop temporarily, "Reset" to return to 25:00

## What is the Pomodoro Technique?
Work for 25 minutes, then take a 5-minute break. Repeat. This helps maintain focus and prevents burnout.

## How it works:
- Sessions counter saved to `pomodoro_sessions.txt`
- Automatically loads previous session count on startup
- QTimer ticks every second to update the display
- Auto-switches modes when timer reaches zero

## What I learned:
- Using QTimer for countdown functionality
- Time formatting (MM:SS display)
- State management (work vs break mode)
- Auto-switching between different timer modes
- Building a productivity tool
- Persistent session tracking

Created: March 2026
