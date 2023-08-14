from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


class cal(App):
    def build(self):
      self.icon="calculator.png"
      self.operators=["+","-","*","/"]
      self.last_was_operator=None
      self.last_was_button=None
      self.zero= ("0")
      main_layout=BoxLayout(orientation="vertical")
      self.solution=TextInput(background_color='black',foreground_color='white',halign="right",font_size=50,readonly=True)
      main_layout.add_widget(self.solution)
      button=[
         ["7","8","9","/"],
         ["4","5","6","+"],
         ["1","2","3","-"],
         [".","0","c","*"],

         ]
      for row in button:
            h_layout=BoxLayout()
            for label in row:
               button1= Button(text=label,font_size=30,background_color="gray",pos_hint={"center_x":0.5,"center_y":0.5})
               button1.bind(on_press=self.on_button_press)
               h_layout.add_widget(button1)
            main_layout.add_widget(h_layout)
      eqaial_button= Button(text="=",font_size=30,background_color="gray",pos_hint={"center_x":0.5,"center_y":0.5})
      eqaial_button.bind(on_press=self.on_solution)
      main_layout.add_widget(eqaial_button)
      return main_layout
    def on_button_press(self,instance):
      current = self.solution.text
      button_text = instance.text
      if button_text =='c':
          self.solution.text=""
      else:
          if current and  (self.last_was_operator and button_text in self.operators):
              return
          elif current and (self.last_was_operator and button_text in self.zero):
              return  
          elif current=="" and button_text in self.operators:
              return
          elif current=="" and button_text in self.zero:
              return
          else:
              new_text= current + button_text
              self.solution.text = new_text
      self.last_button =button_text
      self.last_was_operator = self.last_button in self.operators
    def on_solution(self,instance):
      text = self.solution.text
      if text:
          solution=str(eval(self.solution.text))
          self.solution.text = solution

      
if __name__=="__main__":
    cal().run()