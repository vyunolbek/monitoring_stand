#!/bin/bash

# Переменные
WG_INTERFACE="wg0"
WG_CONFIG="/etc/wireguard/${WG_INTERFACE}.conf"
CLIENT_PRIVATE_KEY="cNHLr7QXoKSbp7FudFOWohQA1bEvloWdBBf6p3Iys2U="
CLIENT_ADDRESS="10.8.0.3/24"
CLIENT_DNS="1.1.1.1"
SERVER_PUBLIC_KEY="UlX6rlSPkDz5f2IJWTGZYb4L9RB7F8zrEGGoa73cZxg="
SERVER_ENDPOINT="195.122.253.120:51820"
ALLOWED_IPS="0.0.0.0/0"
PERSISTENT_KEEPALIVE=0

# Проверка на наличие sudo
if [[ "$EUID" -ne 0 ]]; then
  echo "Пожалуйста, запустите скрипт с правами суперпользователя."
  exit 1
fi

# Установка WireGuard, если он не установлен
if ! command -v wg &> /dev/null; then
  echo "WireGuard не установлен. Устанавливаем..."
  if [[ -f /etc/debian_version ]]; then
    apt update
    apt install -y wireguard
  elif [[ -f /etc/redhat-release ]]; then
    yum install -y epel-release
    yum install -y wireguard-tools
  else
    echo "Неизвестная операционная система. Пожалуйста, установите WireGuard вручную."
    exit 1
  fi
fi

# Создание конфигурационного файла
echo "Создание конфигурационного файла WireGuard..."
cat <<EOF > $WG_CONFIG
[Interface]
PrivateKey = $CLIENT_PRIVATE_KEY
Address = $CLIENT_ADDRESS
DNS = $CLIENT_DNS

[Peer]
PublicKey = $SERVER_PUBLIC_KEY
Endpoint = $SERVER_ENDPOINT
AllowedIPs = $ALLOWED_IPS
PersistentKeepalive = $PERSISTENT_KEEPALIVE
EOF

# Настройка прав на конфигурационный файл
chmod 600 $WG_CONFIG

# Запуск WireGuard
echo "Запуск WireGuard..."
wg-quick up $WG_INTERFACE

# Автоматический запуск при загрузке системы
echo "Добавление WireGuard в автозапуск..."
systemctl enable wg-quick@$WG_INTERFACE

echo "Настройка WireGuard клиента завершена. Конфигурация находится в $WG_CONFIG"
