proyectos = [
    {
        "indice": "01",
        "url": "https://rafasb.github.io/pihole_docker_compose/",
        "titulo": "PiHole en docker",
        "subtitulo": "Desplegar PiHole usando docker y docker-compose.",
        "explicacion": "Muy útil tanto para desplegar en casa como para realizar las primeras prácticas con docker y docker-compose.",
        "detalle": "Permite disponer de un sistema para bloquear publicidad en los dispositivos de casa y un servicio de DNS propio para incorporar tus dispositivos."
    },
    {
        "indice": "02",
        "url": "https://rafasb.github.io/wordpress-docker-full-stack/",
        "titulo": "Wordpress en docker con certificado Let's Encrypt",
        "subtitulo": "Útil para poner rápidamente en marcha un proyecto wordpress y poder mostrarlo públicamente con seguridad SSL.",
        "explicacion": "Hace uso de un proxy inverso para facilitar el acceso mediante cualquier nombre DNS y disponer del certificado gratuido y actualizado del servicio de Let's Encrypt.",
        "detalle": "Al emplear docker facilita el backup y el cambio de proyecto simplemente copiando y restaurando los directorios de datos."
    },
    {
        "indice": "03",
        "url": "https://github.com/rafasb/wordpress-traefik-docker/",
        "titulo": "Wordpress en docker con traefik y certificado Let's Encrypt",
        "subtitulo": "Útil para poner rápidamente en marcha un proyecto wordpress y poder mostrarlo públicamente con seguridad SSL.",
        "explicacion": "Hace uso de traefik que además de aportar un balanceado de carga y certificado SSL automatizado, nos muestra estadísticas de uso.",
        "detalle": "Es un excelente ejemplo para configurar traefik, ampliamente empleado con docker y kubernetes."
    },
    {
        "indice": "04",
        "url": "https://rafasb.github.io/gitlab_docker-compose/",
        "titulo": "Gitlab sobre docker-compose",
        "subtitulo": "Despliegue local de la potente aplicación GitLab sobre docker-compose.",
        "explicacion": "Servidor Git para control de versiones, servicio de CI/CD, registro de imágenes de contenedores.",
        "detalle": "También es interesante el script comentado gen-certs.sh para gestión de certificados."
    },
    {
        "indice": "05",
        "url": "https://rafasb.github.io/log-monitor/",
        "titulo": "Monitorización de logs",
        "subtitulo": "Despliegue local de Graylog, basándose en elasticsearch y fluentd para recopilar origenes de logs.",
        "explicacion": "Complentando la gran utilidad de Graylog para realizar análisis de logs, generar alertas y dashboards, disponemos de Fluentd para recopilar y realizar un primer tratamiento de los logs.",
        "detalle": "Es una solución muy potente y escalable donde combina diferentes aplicaciones vinculadas entre si."
    },
    {
        "indice": "06",
        "url": "https://rafasb.github.io/metrics-monitor/",
        "titulo": "Monitorización de métricas",
        "subtitulo": "Despliegue local de Grafana, basándose en Influxdb + Telegraf y Prometheus.",
        "explicacion": "Veremos dos aproximaciones diferentes para la monitorización de sistemas, una basada en Prometheus y otra basada en InfluxDB v2 y Telegraf.",
        "detalle": "Este es un ejemplo de un conjunto complejo de contenedores que realiza muy diferentes funciones para conseguir un resultado, disponer de paneles para monitorizar métricas de sistemas."
    },
    {
        "indice": "07",
        "url": "https://rafasb.github.io/ansible-docker-cli/",
        "titulo": "Contenedor para ejecutar Ansible",
        "subtitulo": "Ansible es una de las mejores soluciones para automatización. Este proyecto lo convierte en una aplicación portable",
        "explicacion": "El proyecto explora la posibilidad de crear nuestro propio contenedor, usando una imagen de Ubuntu e instalando aplicaciones de sistema, aplicaciones Python e incluso plugins y configuración de la aplicación.",
        "detalle": "El resultado es una imagen que podemos usar para ejecutar un contenedor como un comando CLI para realizar tareas automatizadas."
    },
    {
        "indice": "08",
        "url": "https://rafasb.github.io/jupyter-ansible/",
        "titulo": "Contenedor para ejecutar Jupiter",
        "subtitulo": "Combina la potencia de Ansible con la facilidad de uso y practicidad de Jupyter Notebook",
        "explicacion": "El proyecto crea un servidor de Jupyter Notebook (última versión Jupiter-Lab).",
        "detalle": "Permite emplear la potente herramienta de Ansible, con una colección de plugins orientada a la automatización de equipos de red y a través de la interfaz web de Jupyter"
    },
    {
        "indice": "09",
        "url": "https://rafasb.github.io/remote-wake-stop-servers/",
        "titulo": "Arrancar y detener equipos en remoto",
        "subtitulo": "En algunas situaciones puede resultar interesante poder encender o apagar un PC en remoto, tanto desde la propia LAN del equipo, como desde otra red e incluso desde Internet.",
        "explicacion": "El proyecto se basa en 3 contenedores, un para las funciones de Wake on LAN (WoL), otro para el apagado y el tercero basado en NPM para facilitar el acceso remoto seguro a los anteriores.",
        "detalle": "Es un ejemplo práctico e interesante para aprender a realizar un contenedor con APIs basadas en Python (FastAPI) y para asegurar el acceso a servicios que no implementan la seguridad de forma nativa."
    }
]