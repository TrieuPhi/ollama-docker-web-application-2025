FROM ollama/ollama

# Copy the pull script
COPY ./pull-qwen.sh /pull-qwen.sh

# Make the script executable
RUN chmod +x /pull-qwen.sh

# The entrypoint is set in docker-compose.yml