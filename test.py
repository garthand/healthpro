from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivy.uix.boxlayout import BoxLayout
import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.uix.image import Image


class MyContentAliment(BoxLayout):
    monto_alimento = 0

    def apply_currency_format(self):
        # if len <= 3
        if len(self.ids.monto_aliment_viaje.text) <= 3 and self.ids.monto_aliment_viaje.text.isnumeric():
            self.ids.monto_aliment_viaje.text = "$" + self.ids.monto_aliment_viaje.text + '.00'
        # n,nnn
        elif len(self.ids.monto_aliment_viaje.text) == 4 and self.ids.monto_aliment_viaje.text.isnumeric():
            self.ids.monto_aliment_viaje.text = "$" + self.ids.monto_aliment_viaje.text[0] + "," + \
                                            self.ids.monto_aliment_viaje.text[1:] + '.00'
        # nn,nnn
        elif len(self.ids.monto_aliment_viaje.text) == 5 and self.ids.monto_aliment_viaje.text.isnumeric():
            self.ids.monto_aliment_viaje.text = "$" + self.ids.monto_aliment_viaje.text[:2] + "," + \
                                            self.ids.monto_aliment_viaje.text[2:] + '.00'

    def limit_currency(self):
        if len(self.ids.monto_aliment_viaje.text) > 5 and self.ids.monto_aliment_viaje.text.startswith('$') == False:
            self.ids.monto_aliment_viaje.text = self.ids.monto_aliment_viaje.text[:-1]

    def sumar_gasto(self):
        if self.ids.monto_aliment_viaje.text == "":
            pass
        elif self.ids.monto_aliment_viaje.text.startswith('$'):
            pass
        else:
            travel_manager = MDApp.get_running_app().root.get_screen('travelManager')
            monto_total = float(travel_manager.ids.suma_solic_viaje.text[2:])
            monto_total += float(self.ids.monto_aliment_viaje.text)
            travel_manager.ids.suma_solic_viaje.text = "$ " + str(monto_total)
            self.apply_currency_format()

    # USE THIS METHOD TO UPDATE THE VALUE OF ALIMENTOS (donut)
    def update_requested_value(self):
        MyContentAliment.monto_alimento = 0
        if len(self.ids.monto_aliment_viaje.text) > 0:
            MyContentAliment.monto_alimento = self.ids.monto_aliment_viaje.text
        else:
            MyContentAliment.monto_alimento = 0  
        TravelManagerWindow.update_donut_graph(MyContentAliment.monto_alimento)

class MyContentCasetas(BoxLayout):
    monto_casetas = 0
    def apply_currency_format(self):
        # if len <= 3
        if len(self.ids.monto_casetas_viaje.text) <= 3 and self.ids.monto_casetas_viaje.text.isnumeric():
            self.ids.monto_casetas_viaje.text = "$" + self.ids.monto_casetas_viaje.text + '.00'
        # n,nnn
        elif len(self.ids.monto_casetas_viaje.text) == 4 and self.ids.monto_casetas_viaje.text.isnumeric():
            self.ids.monto_casetas_viaje.text = "$" + self.ids.monto_casetas_viaje.text[0] + "," + \
                                            self.ids.monto_casetas_viaje.text[1:] + '.00'
        # nn,nnn
        elif len(self.ids.monto_casetas_viaje.text) == 5 and self.ids.monto_casetas_viaje.text.isnumeric():
            self.ids.monto_casetas_viaje.text = "$" + self.ids.monto_casetas_viaje.text[:2] + "," + \
                                            self.ids.monto_casetas_viaje.text[2:] + '.00'

    def limit_currency(self):
        if len(self.ids.monto_casetas_viaje.text) > 5 and self.ids.monto_casetas_viaje.text.startswith('$') == False:
            self.ids.monto_casetas_viaje.text = self.ids.monto_casetas_viaje.text[:-1]

    def sumar_gasto(self):
        if self.ids.monto_casetas_viaje.text == "":
            pass
        elif self.ids.monto_casetas_viaje.text.startswith('$'):
            pass
        else:
            travel_manager = MDApp.get_running_app().root.get_screen('travelManager')
            monto_total = float(travel_manager.ids.suma_solic_viaje.text[2:])
            monto_total += float(self.ids.monto_casetas_viaje.text)
            travel_manager.ids.suma_solic_viaje.text = "$ " + str(monto_total)
            self.apply_currency_format()

    # USE THIS METHOD TO UPDATE THE VALUE OF CASETAS (donut)
    def update_requested_value(self):
        MyContentCasetas.monto_casetas = 0
        if len(self.ids.monto_casetas_viaje.text) > 0:
            MyContentCasetas.monto_casetas = self.ids.monto_casetas_viaje.text
        else:
            MyContentCasetas.monto_casetas = 0
        TravelManagerWindow.update_donut_graph(MyContentCasetas.monto_casetas)


class MyContentGasolina(BoxLayout):
    monto_gasolina = 0

    def apply_currency_format(self):
        # if len <= 3
        if len(self.ids.monto_gas_viaje.text) <= 3 and self.ids.monto_gas_viaje.text.isnumeric():
            self.ids.monto_gas_viaje.text = "$" + self.ids.monto_gas_viaje.text + '.00'
        # n,nnn
        elif len(self.ids.monto_gas_viaje.text) == 4 and self.ids.monto_gas_viaje.text.isnumeric():
            self.ids.monto_gas_viaje.text = "$" + self.ids.monto_gas_viaje.text[0] + "," + \
                                        self.ids.monto_gas_viaje.text[1:] + '.00'
        # nn,nnn
        elif len(self.ids.monto_gas_viaje.text) == 5 and self.ids.monto_gas_viaje.text.isnumeric():
            self.ids.monto_gas_viaje.text = "$" + self.ids.monto_gas_viaje.text[:2] + "," + \
                                        self.ids.monto_gas_viaje.text[2:] + '.00'

    def limit_currency(self):
        if len(self.ids.monto_gas_viaje.text) > 5 and self.ids.monto_gas_viaje.text.startswith('$') == False:
            self.ids.monto_gas_viaje.text = self.ids.monto_gas_viaje.text[:-1]

    def sumar_gasto(self):
        if self.ids.monto_gas_viaje.text == "":
            pass
        elif self.ids.monto_gas_viaje.text.startswith('$'):
            pass
        else:
            travel_manager = MDApp.get_running_app().root.get_screen('travelManager')
            monto_total = float(travel_manager.ids.suma_solic_viaje.text[2:])
            monto_total += float(self.ids.monto_gas_viaje.text)
            travel_manager.ids.suma_solic_viaje.text = "$ " + str(monto_total)
            self.apply_currency_format()

    # USE THIS METHOD TO UPDATE THE VALUE OF GASOLINA (donut)
    def update_requested_value(self):
        MyContentGasolina.monto_gasolina = 0
        if len(self.ids.monto_gas_viaje.text) > 0:
            MyContentGasolina.monto_gasolina = self.ids.monto_gas_viaje.text
        else:
            MyContentGasolina.monto_gasolina = 0             
        TravelManagerWindow.update_donut_graph \
            (MyContentGasolina.monto_gasolina)

class LoginWindow(Screen):
    pass


class TravelManagerWindow(Screen):
    panel_container = ObjectProperty(None)
    expense_graph = ObjectProperty(None)

    # EXPANSION PANEL PARA SOLICITAR GV
    def set_expansion_panel(self):
        self.ids.panel_container.clear_widgets()
        # FOOD PANEL
        self.ids.panel_container.add_widget(MDExpansionPanel(icon="food", content=MyContentAliment(),
                                                         panel_cls=MDExpansionPanelOneLine(text="Alimentacion")))
        # CASETAS PANEL
        self.ids.panel_container.add_widget(MDExpansionPanel(icon="food", content=MyContentCasetas(),
                                                         panel_cls=MDExpansionPanelOneLine(text="Casetas")))
        # GAS PANEL
        self.ids.panel_container.add_widget(MDExpansionPanel(icon="food", content=MyContentGasolina(),
                                                         panel_cls=MDExpansionPanelOneLine(text="Gasolina")))
    def update_donut_graph(self):
        plt.clf()  # clear the plot
        travel_manager = MDApp.get_running_app().root.get_screen('travelManager')
        travel_manager.ids.expense_graph.clear_widgets()
        # create data
        names = 'Alimentación', 'Casetas', 'Gasolina',
        data_values = [MyContentAliment.monto_alimento, MyContentCasetas.monto_casetas,
                 MyContentGasolina.monto_gasolina]

        # Create a white circle for the center of the plot
        my_circle = plt.Circle((0, 0), 0.65, color='white')
        # Create graph, add and place percentage labels
        # Add spaces to separate elements from the donut
        explode = (0.05, 0.05, 0.05)
        plt.pie(data_values, autopct="%.1f%%", startangle=0, pctdistance=0.80, labeldistance=1.2, explode=explode)

        p = plt.gcf()
        p.gca().add_artist(my_circle)
        # Create and place legend of the graph
        plt.legend(labels=names, loc="center", fontsize='xx-small')
        # Add graph to Kivy App
        # plt.show()
        # THE DESIRED RESULT IS TO ADD THE GRAPH TO THE APP WITH THE LINE OF CODE BELOW, INSTEAD OF THE plt.show() line
        travel_manager.ids.expense_graph.add_widget(FigureCanvasKivyAgg(figure=plt.gcf()))


# WINDOW MANAGER ################################
class WindowManager(ScreenManager):
    pass


class ReprodExample3(MDApp):
    travel_manager_window = TravelManagerWindow()

    def build(self):
        self.theme_cls.primary_palette = "Teal"
        return WindowManager()


if __name__ == "__main__":
    ReprodExample3().run()
