FROM python:3.8

# Install FFmpeg and ffprobe
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Copy the bot folder
COPY bot /bot

# Set the working directory
WORKDIR /bot

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script
CMD ["python", "__main__.py"]
