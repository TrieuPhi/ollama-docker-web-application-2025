Từ log tôi thấy model đang được pull, nhưng chưa hoàn thành. Bạn có thể kiểm tra trạng thái của model bằng cách:

1. Kiểm tra model đã pull chưa:
```bash
docker exec ollama-server ollama list
```

2. Nếu muốn xem log chi tiết của quá trình pull:
```bash
docker-compose logs -f ollama-server
```

Tôi sẽ tổng hợp lại tất cả các lệnh Docker cần thiết cho dự án này:

### 1. Các lệnh cơ bản để chạy ứng dụng:
```bash
# Dừng và xóa container cũ
docker-compose down

# Build lại image (khi có thay đổi code)
docker-compose build --no-cache

# Chạy container
docker-compose up -d

# Xem log
docker-compose logs -f ollama-server
```

### 2. Các lệnh kiểm tra và quản lý:
```bash
# Kiểm tra danh sách model đã pull
docker exec ollama-server ollama list

# Kiểm tra trạng thái container
docker ps

# Kiểm tra logs của container
docker logs ollama-server

# Vào trong container (nếu cần debug)
docker exec -it ollama-server /bin/bash
```

### 3. Các lệnh dọn dẹp (khi cần):
```bash
# Dừng và xóa container
docker-compose down

# Xóa tất cả image không sử dụng
docker system prune -a

# Xóa volume không sử dụng
docker volume prune
```

### 4. Các lệnh hữu ích khác:
```bash
# Kiểm tra sử dụng tài nguyên
docker stats

# Kiểm tra thông tin network
docker network ls
docker network inspect ollama-docker-web-application-2025_my-net
```

Lưu ý:
- Khi pull model lần đầu sẽ mất một chút thời gian vì model khá lớn
- Nếu gặp lỗi, bạn có thể xem log để debug
- Nếu muốn pull model khác, bạn có thể sửa tên model trong file `pull-qwen.sh` và build lại

Bạn có cần tôi giải thích thêm về bất kỳ lệnh nào không?
