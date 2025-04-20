# Simple IP Service

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)


### Description

Service provides several endpoints for retrieving the client's IP address in various formats:
- **`/ip`**: Returns the IP address as plain text.
- **`/json`**: Returns the IP address in JSON format.


### Configure settings:

Configure by edit `config.py` or set enviroment variable:
  - BASE_URL: default value "https://your-domain.com"
  - HOST: default value "0.0.0.0"
  - PORT: default value 8000
  - WORKERS: default value 1


### Run the application:

  ```bash
  BASE_URL=https://my-site.com
  PORT=8000
  WORKERS=1
  uv run src/main.py
  ```


## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
