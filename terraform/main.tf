terraform {
  required_providers {
    yandex = {
      source  = "yandex-cloud/yandex"
      version = "0.69.0"
    }
  }
}

provider "yandex" {
  token     = "AQAAAABb-hjxAATuwcMzvQmN_0X9s5W6L8DvdIY"
  cloud_id  = "b1gkblmp64p8rquuo7hu"
  folder_id = "b1gcoodl8urbs3gqlr2u"
  zone      = "ru-central1-c"
}

resource "yandex_compute_image" "vm-1" {
  source_image = "fd8t3qtmqkqb3vsfjs11"
  name         = "ubuntu_img"
}
