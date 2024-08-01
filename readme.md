# Human:
# Requires for python

- numpy
- pygame
- sounddevice

# Sounddevice requires:

- sudo apt-get install libportaudio2


# ChatGPT:
Sure, here is an updated and detailed README that includes the additional details for the scripts you have provided.

---

# Artistic Audio Visualizer

This project contains a series of Python scripts (`sound.py` to `sound9.py`) for creating an artistic audio visualizer using Pygame, Numpy, and Sounddevice libraries. Each script provides a unique implementation or improvement over the previous version, allowing you to visualize audio input in real-time with different features.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Scripts Overview](#scripts-overview)
- [Contributing](#contributing)
- [License](#license)

## Requirements

- Python 3.x
- Pygame
- Numpy
- Sounddevice

## Installation

1. Clone the repository or download the scripts.
2. Install the required libraries using pip:
    ```bash
    pip install pygame numpy sounddevice
    ```

## Usage

Each script (`sound.py` to `sound9.py`) can be executed independently. To run a script, use the following command:

```bash
python sound.py
```

Replace `sound.py` with `sound2.py`, `sound3.py`, etc., to run the other versions.

## Features

### Common Features
- Real-time audio visualization
- Configurable parameters for audio processing and visualization
- Frequency to note mapping
- Note color coding
- Dynamic circle size based on audio magnitude
- Note letters displayed in the middle of the circles

### Unique Features per Script
Each script has incremental improvements and unique features. Refer to the [Scripts Overview](#scripts-overview) section for detailed information on each script's features.

## Scripts Overview

### `sound.py`
- Basic real-time audio visualization.
- Displays circles representing frequencies.
- Maps frequencies to musical notes.

### `sound2.py`
- Added smoothing to frequency magnitudes.
- Improved visual representation with configurable smoothing factor.

### `sound3.py`
- Introduced configurable frequency range.
- Enhanced user interaction for adjusting parameters.

### `sound4.py`
- Implemented thresholding for circle display.
- Configurable threshold parameter to filter low magnitudes.

### `sound5.py`
- Added note colors for visual differentiation.
- Each note is displayed with a unique color.

### `sound6.py`
- Included quarter-step notes for more accurate frequency representation.
- Added colors for quarter-step notes.

### `sound7.py`
- Incorporated loudness into the display by adjusting circle sizes based on magnitude.
- Enhanced visual feedback with dynamic circle sizes.

### `sound8.py`
- Displayed note letters in the middle of the circles.
- Improved user interface with text rendering.

### `sound9.py`
- Utilized Short-Time Fourier Transform (STFT) for more accurate frequency detection.
- Implemented a Hanning window for better time-frequency resolution.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to create a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

By following this README, you should be able to run and explore each version of the audio visualizer scripts, understanding their unique features and improvements. Enjoy visualizing your audio input in real-time!