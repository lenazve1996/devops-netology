resource "yandex_compute_instance" "node01" {
  name                      = "node01"
  zone                      = "ru-central1-a"
  hostname                  = "node01.netology.cloud"
  allow_stopping_for_update = true

  resources {
    cores  = 8
    memory = 8
  }

  boot_disk {
    initialize_params {
      image_id    = "${var.centos-7-base}"
      name        = "root-node01"
      type        = "network-nvme"
      size        = "50"
    }
  }

  network_interface {
    subnet_id = "${yandex_vpc_subnet.default.id}"
    nat       = true
  }

  metadata = {
    ssh-keys = "-----BEGIN PUBLIC KEY-----\nAAAAB3NzaC1yc2EAAAADAQABAAABgQCpNsfhK66EKb4f6dd9sSTz7NnEhvVheNj4Nxi9LzgFkXAtYWf8eSo35MJMEx/4EbLbQ2JDkVJ71Tjg3qsQa0CGoG3ybJRttYO3w+V4488ehNFd2B0BAoekUzCapA+Pdd4z7fZtXNFAvdlZLM4n2sdt2Gr4JRD0K0p//m038/p/JdvNrLDVE0C8qLAMVfF7gyqxuX+lizwlMXgvK7jTrhi57QUK0BhL7NUt6kqSbpcRte9TUO1vit4igB+UdDw8AP89YwMYDC59oh2LkmdebhNvc+vSgx/YzzbL1zsEsErX7rcjOKLlv92wlEf2iIzgZFBSjrZM5/lWM5mBYo+6ujCafHjXHvswq4aBmrcIp/yQENpyfrWSuWyLjAqGtcD0fm0V8NFhF9xKd5KA0x8Df4N0NTo4DVDmDMTGPX8Z+JP6RJbRY5fq2IuyQTBkCufrbiSPqFV2SIE0+Y6l/DG4x+6/Q/kxRPLkz1haL+WtClHKOtwWa7B5wQjnvkxW6fQvcOc\n-----END PUBLIC KEY-----\n"
  }
}
