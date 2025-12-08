variable "aws_region" {
    type = string
    default ="us-east-1"
}

variable "app_name"{
    type = string
    default = "gist-api"
}

variable "container_port"{
    type = number
    default = 8000
}

variable "cpu"{
    type = number
    default = 256
}

variable "memory"{
    type = number
    default = 512
}

