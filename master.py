import os
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)
from stable_diffusion import StableDiffusionModel


def generate_stable_diffusion_image(prompt, negative_prompt):
    """
    Generates an image using the Stable Diffusion model based on given prompts.

    Args:
        prompt (str): The main prompt describing the desired output.
        negative_prompt (str): The prompt describing undesired elements.

    Returns:
        str: The file path of the generated image.
    """
    model = StableDiffusionModel()
    generated_image = model.generate(prompt, negative_prompt)
    image_path = os.path.join('generated_images', 'generated_image.png')
    generated_image.save(image_path)
    return image_path


class StableDiffusionGUI(QWidget):
    def __init__(self):
        """
        Initializes the GUI application.
        """
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        Sets up the GUI layout, widgets and connections.
        """
        self.setWindowTitle('StableDiffusion Image Generator')
        layout = QVBoxLayout()

        self.prompt_input = QTextEdit()
        self.negative_prompt_input = QTextEdit()
        layout.addWidget(QLabel('Prompt:'))
        layout.addWidget(self.prompt_input)
        layout.addWidget(QLabel('Negative Prompt:'))
        layout.addWidget(self.negative_prompt_input)

        self.generate_button = QPushButton('Generate Image', self)
        self.generate_button.clicked.connect(self.generate_image)
        layout.addWidget(self.generate_button)

        self.result_label = QLabel(self)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def generate_image(self):
        """
        Captures input from text fields, generates an image, and displays it in the GUI.
        """
        prompt = self.prompt_input.toPlainText()
        negative_prompt = self.negative_prompt_input.toPlainText()
        result_image_path = generate_stable_diffusion_image(
            prompt, negative_prompt)
        self.result_label.setPixmap(QPixmap(result_image_path))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StableDiffusionGUI()
    ex.show()
    sys.exit(app.exec_())
