import cv2

class videoBase:
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.video = cv2.VideoCapture(path)
        self.selected_frame = None
        self.outline_color = (0, 0, 255)  # Red color for object outline

    def print_basic_info(self):
        print(f"Video Name: {self.name}")
        print(f"Video Path: {self.path}")
        print(f"Number of Frames: {int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))}")
        print(f"Frame Width: {int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))}")
        print(f"Frame Height: {int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))}")

    def play(self):
        while True:
            ret, frame = self.video.read()
            if not ret:
                break
            cv2.imshow(self.name, frame)
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break
        self.video.release()
        cv2.destroyAllWindows()

    def object_selection(self):
        cv2.namedWindow(self.name)
        cv2.setMouseCallback(self.name, self.mouse_callback)
        self.play()

    def mouse_callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.selected_frame = self.video.get(cv2.CAP_PROP_POS_FRAMES)
            print(f"Object selected at frame {int(self.selected_frame)}")
            cv2.destroyAllWindows()

    def play_with_outline(self):
        self.video.set(cv2.CAP_PROP_POS_FRAMES, self.selected_frame)
        frame_width = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (frame_width, frame_height))

        while True:
            ret, frame = self.video.read()
            if not ret:
                break
            if self.selected_frame is not None:
                # Implement object outlining logic here
                # For demonstration, let's draw a red rectangle around the object
                cv2.rectangle(frame, (50, 50), (150, 150), self.outline_color, 2)
            cv2.imshow(self.name, frame)
            out.write(frame)
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break

        self.video.release()
        out.release()
        cv2.destroyAllWindows()

    def take_snapshot(self, frame_number, filename):
        self.video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ret, frame = self.video.read()
        if ret:
            # Implement object outlining logic here
            # For demonstration, let's draw a red rectangle around the object
            cv2.rectangle(frame, (50, 50), (150, 150), self.outline_color, 2)
            cv2.imwrite(filename, frame)
            print(f"Snapshot saved as {filename}")
        else:
            print("Failed to capture a snapshot.")

    def save_video(self, output_filename):
        # Saving the video with the object outlined
        self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Reset to the beginning of the video
        frame_width = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out = cv2.VideoWriter(output_filename, cv2.VideoWriter_fourcc(*'XVID'), 30, (frame_width, frame_height))

        while True:
            ret, frame = self.video.read()
            if not ret:
                break
            if self.selected_frame is not None:
                # Implement object outlining logic here
                # For demonstration, let's draw a red rectangle around the object
                cv2.rectangle(frame, (50, 50), (150, 150), self.outline_color, 2)
            out.write(frame)

        self.video.release()
        out.release()
        print(f"Video with object outline saved as {output_filename}")


if __name__ == "__main__":
    video = videoBase("sample_video", "sample_video.mp4")
    video.print_basic_info()
    video.object_selection()
    video.play_with_outline()
    video.save_video("output_video.avi")
    video.take_snapshot(100, "snapshot_frame100.png")