class Mobile:
    def __init__(self,processor,camera):
        self.processor=processor
        self.camera=camera
    def getProcessorName(self):
        return self.processor
    def getCameraName(self):
        return self.camera
Redmi=Mobile("Snapdragorn",13)
print("The processor of Redmi is:",Redmi.processor)
print("The camera of Redmi is:",Redmi.camera)

Samsung=Mobile("Quad core",35)
print("The processor of Samsung is:",Samsung.processor)
print("The camera of Samsung is:",Samsung.camera)
