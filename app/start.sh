#!/bin/bash

uvicorn app.run:app --host 0.0.0.0 --port 8000 --reload