import flet as ft
import requests
from datetime import datetime

import time

#VARIABLES GENERALES QUE SE TOMARAN PARA LOS ELEMENTOS COMO BOTONES O CAMPOS DE ENTRADA
color="#404040"
color_hint="#C3C7CF"
color_primary="#000000"
color_secondary="#d6e7ff"
color_hovered="#234bb9"
border_input=10
desplegable_diagnostico="#E3F2FD"
color_check="#00e676"
color_error="#e57373"


#MÉTODO GENERAL DE LA APP
def main(page: ft.Page):
        
        #Configuraciones de la interfaz(VISTA)
        page.padding=0
        page.title = "Hortifrut APP"
        page.window.width = 360 
        page.window.height = 720
        page.bgcolor = "#dddddd"
        page.padding = 0
        page.spacing = 0
        page.adaptive = True
        page.theme_mode = ft.ThemeMode.DARK
        page.horizontal_alignment="center"
        page.vertical_alignment="center"

        #ESTA ES LA URL DE LA API A LA QUE LE HARÁ LA SOLICITUD
        API_URL = ""
        
        #----------------------------------------------------------------------------------------------------------------------------------------------
        
        #MÉTODO PARA HACER LA PREDICCIÓN
        def diagnosticar(e):

            # Recoger los valores de los campos del formulario

            datos = {
                'clonesize': ip_clonesize.value,
                'honeyBee': ip_honeyBee.value,
                'bumblesBee': ip_bumblesBee.value,
                'andrenaBee': ip_andrenaBee.value,
                'osmiaBee': ip_osmiaBee.value,
                'MaxTempBS': ip_MaxTempBS.value,
                'MinTempBS': ip_MinTempBS.value,
                'AverageTempBS': ip_AverageTempBS.value,
                'MaxTempBI': ip_MaxTempBI.value,
                'MinTempBI': ip_MinTempBI.value,
                'AverageTempBI': ip_AverageTempBI.value,
                'RainingDays': ip_RainingDays.value,
                'AverageRainingDays': ip_AverageRainingDays.value,
                'fruitset': ip_fruitset.value,
                'fruitmass': ip_fruitmass.value,
                'seeds': ip_seeds.value
            }

            #Llamada al método para validaciones
            for campo, valor in datos.items():
            # Verifica si el valor es None o una cadena vacía
                if valor is None or valor == '':
                    print(f"El campo '{campo}' está vacío.")
                    return False

            else: 
                
                #cabeceras para la solicitud
                headers = {
                        'Content-Type': 'application/json'}
                # Enviar una solicitud POST a la API
                try:
    
                    response = requests.post(API_URL, json=datos, headers=headers)
                    if response.status_code == 201:

                        response_json = response.json()
                        
                        prediction_value = response_json.get('prediccion', [0])
                        print(prediction_value)

                        prediccion_resultado.value = prediction_value


                    else:
                        # Imprimir mensaje de error detallado
                        print(f"Error: {response.status_code} - {response.text}")
                        prediccion_resultado.value = f"Error: {response.status_code}"

                except requests.exceptions.RequestException as e:
                    print(f"Ocurrió un error de red: {e}")
                    prediccion_resultado.value = f"Ocurrió un error de red: {e}"

                except ValueError as e:
                    print(f"Error al procesar la respuesta JSON: {e}")
                    prediccion_resultado.value = f"Error al procesar la respuesta JSON: {e}"

                except Exception as e:
                    print(f"Ocurrió un error inesperado: {e}")
                    prediccion_resultado.value = f"Ocurrió un error inesperado: {e}"

    

        #----------------------------------------------------------------------------------------------------------------------------------------------
        
        #A APARTIR DE AQUI ES PURO DISEÑO DE LA INTERFAZ PRIMERO CREANDO LOS TEXFIELD (campos de entrada) y otros


        border_radius=10

        #titulo del objetivo 1
        txt_objetivo = ft.Text("Predicción de \nRendimiento", style=ft.TextStyle(size=20, weight="bold", color=ft.colors.WHITE))
        
        #breve descripcion del tema
        txt_descripcion = ft.Text("Empresa HORTIFRUT", style=ft.TextStyle(size=14, color=ft.colors.WHITE))

        #titulo de formulario
        txt_formulario = ft.Text("Formulario para Predicción", style=ft.TextStyle(size=16, color=color))
       
        # Campo de entrada para 'clonesize'
        ip_clonesize = ft.TextField(
            label="Clonesize",
            keyboard_type="number",
            prefix_icon=ft.icons.STAR_OUTLINED,
            hint_text="0",
            content_padding=0,
            color=color,
            hint_style=ft.TextStyle(
                color=color_hint, 
                size=14, 
            ),
            label_style=ft.TextStyle(
                color=color, 
                size=14, 
            ),
            fill_color=ft.colors.WHITE,
            focused_border_color=color_primary,
            focused_border_width=1,
            border_color="#cccccc",
            border_radius=border_radius,
        )

        # Campo de entrada para 'honeyBee'
        ip_honeyBee = ft.TextField(
            label="Honey Bee",
            keyboard_type="number",
            prefix_icon=ft.icons.BUG_REPORT_OUTLINED,
            hint_text="0",
            content_padding=0,
            color=color,
            hint_style=ft.TextStyle(
                color=color_hint, 
                size=14, 
            ),
            label_style=ft.TextStyle(
                color=color, 
                size=14, 
            ),
            fill_color=ft.colors.WHITE,
            focused_border_color=color_primary,
            focused_border_width=1,
            border_color="#cccccc",
            border_radius=border_radius,
        )

        # Campo de entrada para 'bumblesBee'
        ip_bumblesBee = ft.TextField(
            label="Bumbles Bee",
            keyboard_type="number",
            prefix_icon=ft.icons.BUG_REPORT_OUTLINED,
            hint_text="0",
            content_padding=0,
            color=color,
            hint_style=ft.TextStyle(
                color=color_hint, 
                size=14, 
            ),
            label_style=ft.TextStyle(
                color=color, 
                size=14, 
            ),
            fill_color=ft.colors.WHITE,
            focused_border_color=color_primary,
            focused_border_width=1,
            border_color="#cccccc",
            border_radius=border_radius,
        )

        # Campo de entrada para 'andrenaBee'
        ip_andrenaBee = ft.TextField(
            label="Andrena Bee",
            keyboard_type="number",
            prefix_icon=ft.icons.BUG_REPORT_OUTLINED,
            hint_text="0",
            content_padding=0,
            color=color,
            hint_style=ft.TextStyle(
                color=color_hint, 
                size=14, 
            ),
            label_style=ft.TextStyle(
                color=color, 
                size=14, 
            ),
            fill_color=ft.colors.WHITE,
            focused_border_color=color_primary,
            focused_border_width=1,
            border_color="#cccccc",
            border_radius=border_radius,
        )

        # Campo de entrada para 'osmiaBee'
        ip_osmiaBee = ft.TextField(
            label="Osmia Bee",
            keyboard_type="number",
            prefix_icon=ft.icons.BUG_REPORT_OUTLINED,
            hint_text="0",
            content_padding=0,
            color=color,
            hint_style=ft.TextStyle(
                color=color_hint, 
                size=14, 
            ),
            label_style=ft.TextStyle(
                color=color, 
                size=14, 
            ),
            fill_color=ft.colors.WHITE,
            focused_border_color=color_primary,
            focused_border_width=1,
            border_color="#cccccc",
            border_radius=border_radius,
        )

        # Campo de entrada para 'MaxTempBS'
        ip_MaxTempBS = ft.TextField(
            label="Max Temp BS",
            keyboard_type="number",
            prefix_icon=ft.icons.THERMOSTAT_OUTLINED,
            hint_text="0",
            content_padding=0,
            color=color,
            hint_style=ft.TextStyle(
                color=color_hint, 
                size=14, 
            ),
            label_style=ft.TextStyle(
                color=color, 
                size=14, 
            ),
            fill_color=ft.colors.WHITE,
            focused_border_color=color_primary,
            focused_border_width=1,
            border_color="#cccccc",
            border_radius=border_radius,
        )

        # Campo de entrada para 'MinTempBS'
        ip_MinTempBS = ft.TextField(
            label="Min Temp BS",
            keyboard_type="number",
            prefix_icon=ft.icons.THERMOSTAT_OUTLINED,
            hint_text="0",
            content_padding=0,
            color=color,
            hint_style=ft.TextStyle(
                color=color_hint, 
                size=14, 
            ),
            label_style=ft.TextStyle(
                color=color, 
                size=14, 
            ),
            fill_color=ft.colors.WHITE,
            focused_border_color=color_primary,
            focused_border_width=1,
            border_color="#cccccc",
            border_radius=border_radius,
        )

        # Campo de entrada para 'AverageTempBS'
        ip_AverageTempBS = ft.TextField(
            label="Average Temp BS",
            keyboard_type="number",
            prefix_icon=ft.icons.THERMOSTAT_OUTLINED,
            hint_text="0",
            content_padding=0,
            color=color,
            hint_style=ft.TextStyle(
                color=color_hint, 
                size=14, 
            ),
            label_style=ft.TextStyle(
                color=color, 
                size=14, 
            ),
            fill_color=ft.colors.WHITE,
            focused_border_color=color_primary,
            focused_border_width=1,
            border_color="#cccccc",
            border_radius=border_radius,
        )

        # Campo de entrada para 'MaxTempBI'
        ip_MaxTempBI = ft.TextField(
            label="Max Temp BI",
            keyboard_type="number",
            prefix_icon=ft.icons.THERMOSTAT_OUTLINED,
            hint_text="0",
            content_padding=0,
            color=color,
            hint_style=ft.TextStyle(
                color=color_hint, 
                size=14, 
            ),
            label_style=ft.TextStyle(
                color=color, 
                size=14, 
            ),
            fill_color=ft.colors.WHITE,
            focused_border_color=color_primary,
            focused_border_width=1,
            border_color="#cccccc",
            border_radius=border_radius,
        )

        # Campo de entrada para 'MinTempBI'
        ip_MinTempBI = ft.TextField(
            label="Min Temp BI",
            keyboard_type="number",
            prefix_icon=ft.icons.THERMOSTAT_OUTLINED,
            hint_text="0",
            content_padding=0,
            color=color,
            hint_style=ft.TextStyle(
                color=color_hint, 
                size=14, 
            ),
            label_style=ft.TextStyle(
                color=color, 
                size=14, 
            ),
            fill_color=ft.colors.WHITE,
            focused_border_color=color_primary,
            focused_border_width=1,
            border_color="#cccccc",
            border_radius=border_radius,
        )

        # Campo de entrada para 'AverageTempBI'
        ip_AverageTempBI = ft.TextField(
            label="Average Temp BI",
            keyboard_type="number",
            prefix_icon=ft.icons.THERMOSTAT_OUTLINED,
            hint_text="0",
            content_padding=0,
            color=color,
            hint_style=ft.TextStyle(
                color=color_hint, 
                size=14, 
            ),
            label_style=ft.TextStyle(
                color=color, 
                size=14, 
            ),
            fill_color=ft.colors.WHITE,
            focused_border_color=color_primary,
            focused_border_width=1,
            border_color="#cccccc",
            border_radius=border_radius,
        )

        # Campo de entrada para 'RainingDays'
        ip_RainingDays = ft.TextField(
            label="Raining Days",
            keyboard_type="number",
            prefix_icon=ft.icons.WB_CLOUDY_OUTLINED,
            hint_text="0",
            content_padding=0,
            color=color,
            hint_style=ft.TextStyle(
                color=color_hint, 
                size=14, 
            ),
            label_style=ft.TextStyle(
                color=color, 
                size=14, 
            ),
            fill_color=ft.colors.WHITE,
            focused_border_color=color_primary,
            focused_border_width=1,
            border_color="#cccccc",
            border_radius=border_radius,
        )

        # Campo de entrada para 'AverageRainingDays'
        ip_AverageRainingDays = ft.TextField(
            label="Average Raining Days",
            keyboard_type="number",
            prefix_icon=ft.icons.WB_CLOUDY_OUTLINED,
            hint_text="0",
            content_padding=0,
            color=color,
            hint_style=ft.TextStyle(
                color=color_hint, 
                size=14, 
            ),
            label_style=ft.TextStyle(
                color=color, 
                size=14, 
            ),
            fill_color=ft.colors.WHITE,
            focused_border_color=color_primary,
            focused_border_width=1,
            border_color="#cccccc",
            border_radius=border_radius,
        )

        # Campo de entrada para 'fruitset'
        ip_fruitset = ft.TextField(
            label="Fruitset",
            keyboard_type="number",
            prefix_icon=ft.icons.LOCAL_FLORIST_OUTLINED,
            hint_text="0",
            content_padding=0,
            color=color,
            hint_style=ft.TextStyle(
                color=color_hint, 
                size=14, 
            ),
            label_style=ft.TextStyle(
                color=color, 
                size=14, 
            ),
            fill_color=ft.colors.WHITE,
            focused_border_color=color_primary,
            focused_border_width=1,
            border_color="#cccccc",
            border_radius=border_radius,
        )

        # Campo de entrada para 'fruitmass'
        ip_fruitmass = ft.TextField(
            label="Fruitmass",
            keyboard_type="number",
            prefix_icon=ft.icons.LOCAL_FLORIST_OUTLINED,
            hint_text="0",
            content_padding=0,
            color=color,
            hint_style=ft.TextStyle(
                color=color_hint, 
                size=14, 
            ),
            label_style=ft.TextStyle(
                color=color, 
                size=14, 
            ),
            fill_color=ft.colors.WHITE,
            focused_border_color=color_primary,
            focused_border_width=1,
            border_color="#cccccc",
            border_radius=border_radius,
        )

        # Campo de entrada para 'seeds'
        ip_seeds = ft.TextField(
            label="Seeds",
            keyboard_type="number",
            prefix_icon=ft.icons.GRAIN_OUTLINED,
            hint_text="0",
            content_padding=0,
            color=color,
            hint_style=ft.TextStyle(
                color=color_hint, 
                size=14, 
            ),
            label_style=ft.TextStyle(
                color=color, 
                size=14, 
            ),
            fill_color=ft.colors.WHITE,
            focused_border_color=color_primary,
            focused_border_width=1,
            border_color="#cccccc",
            border_radius=border_radius,
        )

        
    
        #botón -> Diagnosticar
        btn_diagnosticar= ft.FilledButton(
            text="Diagnosticar",
            width=300, 
            height=40,  
            on_click=lambda e: diagnosticar(e),
            style=ft.ButtonStyle(
                shape=ft.StadiumBorder(),
                color={
                    ft.ControlState.HOVERED: color_primary,
                    ft.ControlState.FOCUSED: ft.colors.WHITE,
                    ft.ControlState.DEFAULT: ft.colors.WHITE,
                },
                bgcolor={
                ft.ControlState.HOVERED: color_hint,
                ft.ControlState.DEFAULT: color_primary,
            },
            )
            )

        #etiqueta -> Obtener resultado
        txt_sub_resultado= ft.Text("Resultado:", style=ft.TextStyle(size=16, color="#333333"))

        #text, para mostrar el resultado de predicción
        prediccion_resultado=ft.Text(" ", style=ft.TextStyle(size=15, color=color_primary))

        #----------------------------------------------------------------------------------------------------------------------------------------------

        #CONTAINERS PARA SEPARAR COLUMNAS DE ELEMENTOS
     
        col_content_titulo=ft.Container(content=ft.Column([
                    txt_objetivo,
                    txt_descripcion

            ],horizontal_alignment = ft.CrossAxisAlignment.CENTER,), width=200)
        col_titulo_form=ft.Container(content=ft.Column([
                txt_formulario
            ]
            ), width=300, 
            margin=20,
            #border=ft.border.all()
            )
 
        # Contenedor para 'clonesize'
        col_clonesize = ft.Container(
            content=ft.Column([ip_clonesize]),
            width=300,
        )

        # Contenedor para 'honeyBee'
        col_honeyBee = ft.Container(
            content=ft.Column([ip_honeyBee]),
            width=300,
        )

        # Contenedor para 'bumblesBee'
        col_bumblesBee = ft.Container(
            content=ft.Column([ip_bumblesBee]),
            width=300,
        )

        # Contenedor para 'andrenaBee'
        col_andrenaBee = ft.Container(
            content=ft.Column([ip_andrenaBee]),
            width=300,
        )

        # Contenedor para 'osmiaBee'
        col_osmiaBee = ft.Container(
            content=ft.Column([ip_osmiaBee]),
            width=300,
        )

        # Contenedor para 'MaxTempBS'
        col_MaxTempBS = ft.Container(
            content=ft.Column([ip_MaxTempBS]),
            width=300,
        )

        # Contenedor para 'MinTempBS'
        col_MinTempBS = ft.Container(
            content=ft.Column([ip_MinTempBS]),
            width=300,
        )

        # Contenedor para 'AverageTempBS'
        col_AverageTempBS = ft.Container(
            content=ft.Column([ip_AverageTempBS]),
            width=300,
        )

        # Contenedor para 'MaxTempBI'
        col_MaxTempBI = ft.Container(
            content=ft.Column([ip_MaxTempBI]),
            width=300,
        )

        # Contenedor para 'MinTempBI'
        col_MinTempBI = ft.Container(
            content=ft.Column([ip_MinTempBI]),
            width=300,
        )

        # Contenedor para 'AverageTempBI'
        col_AverageTempBI = ft.Container(
            content=ft.Column([ip_AverageTempBI]),
            width=300,
        )

        # Contenedor para 'RainingDays'
        col_RainingDays = ft.Container(
            content=ft.Column([ip_RainingDays]),
            width=300,
        )

        # Contenedor para 'AverageRainingDays'
        col_AverageRainingDays = ft.Container(
            content=ft.Column([ip_AverageRainingDays]),
            width=300,
        )

        # Contenedor para 'fruitset'
        col_fruitset = ft.Container(
            content=ft.Column([ip_fruitset]),
            width=300,
        )

        # Contenedor para 'fruitmass'
        col_fruitmass = ft.Container(
            content=ft.Column([ip_fruitmass]),
            width=300,
        )

        # Contenedor para 'seeds'
        col_seeds = ft.Container(
            content=ft.Column([ip_seeds]),
            width=300,
        )

  
        col_boton=ft.Container(content=ft.Column([
                btn_diagnosticar
            ]
            ), width=300, 
            margin=10, 
            #border=ft.border.all()
            )

        col_t_resultado=ft.Container(content=ft.Column([
                txt_sub_resultado,
            ]
            ), width=300,
            height=40, 
            margin=ft.margin.only(left=10,top=10,right=10),
            )
        col_resultado=ft.Container(content=ft.ListView([
                prediccion_resultado
            ]
            ), width=300,
            height=300, 
            margin=ft.margin.only(left=10,bottom=10,right=10),
            padding=20, 
            border_radius=10,
            border=ft.border.all(
                color=color_primary,  # Color del borde
                width=1  # Ancho del borde)
                )
            )
        #----------------------------------------------------------------------------------------------------------------------------------------------  
        #CONTAINERS PARA SEPARAR FILAS DE ELEMENTOS
 
        row_titulo_container=ft.Container(content=ft.Row([
                col_content_titulo,
        ], spacing=0, alignment=ft.MainAxisAlignment.CENTER
        ), 
        border=None,
        )

        row_titulo_form=ft.Container(content=ft.Column([
                col_titulo_form
        ]
        ), 
        #width=360,
        alignment=ft.alignment.center,
        #border=ft.border.all()
        )

        # Para 'clonesize'
        row_clonesize = ft.Container(
            content=ft.Column([
                col_clonesize,
            ], spacing=0),
            padding=ft.padding.only(left=10, top=10, right=10),
            alignment=ft.alignment.center,
            #border=ft.border.all()
        )

        # Para 'honeyBee'
        row_honeyBee = ft.Container(
            content=ft.Column([
                col_honeyBee,
            ], spacing=0),
            padding=ft.padding.only(left=10, top=10, right=10),
            alignment=ft.alignment.center,
            #border=ft.border.all()
        )

        # Para 'bumblesBee'
        row_bumblesBee = ft.Container(
            content=ft.Column([
                col_bumblesBee,
            ], spacing=0),
            padding=ft.padding.only(left=10, top=10, right=10),
            alignment=ft.alignment.center,
            #border=ft.border.all()
        )

        # Para 'andrenaBee'
        row_andrenaBee = ft.Container(
            content=ft.Column([
                col_andrenaBee,
            ], spacing=0),
            padding=ft.padding.only(left=10, top=10, right=10),
            alignment=ft.alignment.center,
            #border=ft.border.all()
        )

        # Para 'osmiaBee'
        row_osmiaBee = ft.Container(
            content=ft.Column([
                col_osmiaBee,
            ], spacing=0),
            padding=ft.padding.only(left=10, top=10, right=10),
            alignment=ft.alignment.center,
            #border=ft.border.all()
        )

        # Para 'MaxTempBS'
        row_MaxTempBS = ft.Container(
            content=ft.Column([
                col_MaxTempBS,
            ], spacing=0),
            padding=ft.padding.only(left=10, top=10, right=10),
            alignment=ft.alignment.center,
            #border=ft.border.all()
        )

        # Para 'MinTempBS'
        row_MinTempBS = ft.Container(
            content=ft.Column([
                col_MinTempBS,
            ], spacing=0),
            padding=ft.padding.only(left=10, top=10, right=10),
            alignment=ft.alignment.center,
            #border=ft.border.all()
        )

        # Para 'AverageTempBS'
        row_AverageTempBS = ft.Container(
            content=ft.Column([
                col_AverageTempBS,
            ], spacing=0),
            padding=ft.padding.only(left=10, top=10, right=10),
            alignment=ft.alignment.center,
            #border=ft.border.all()
        )

        # Para 'MaxTempBI'
        row_MaxTempBI = ft.Container(
            content=ft.Column([
                col_MaxTempBI,
            ], spacing=0),
            padding=ft.padding.only(left=10, top=10, right=10),
            alignment=ft.alignment.center,
            #border=ft.border.all()
        )

        # Para 'MinTempBI'
        row_MinTempBI = ft.Container(
            content=ft.Column([
                col_MinTempBI,
            ], spacing=0),
            padding=ft.padding.only(left=10, top=10, right=10),
            alignment=ft.alignment.center,
            #border=ft.border.all()
        )

        # Para 'AverageTempBI'
        row_AverageTempBI = ft.Container(
            content=ft.Column([
                col_AverageTempBI,
            ], spacing=0),
            padding=ft.padding.only(left=10, top=10, right=10),
            alignment=ft.alignment.center,
            #border=ft.border.all()
        )

        # Para 'RainingDays'
        row_RainingDays = ft.Container(
            content=ft.Column([
                col_RainingDays,
            ], spacing=0),
            padding=ft.padding.only(left=10, top=10, right=10),
            alignment=ft.alignment.center,
            #border=ft.border.all()
        )

        # Para 'AverageRainingDays'
        row_AverageRainingDays = ft.Container(
            content=ft.Column([
                col_AverageRainingDays,
            ], spacing=0),
            padding=ft.padding.only(left=10, top=10, right=10),
            alignment=ft.alignment.center,
            #border=ft.border.all()
        )

        # Para 'fruitset'
        row_fruitset = ft.Container(
            content=ft.Column([
                col_fruitset,
            ], spacing=0),
            padding=ft.padding.only(left=10, top=10, right=10),
            alignment=ft.alignment.center,
            #border=ft.border.all()
        )

        # Para 'fruitmass'
        row_fruitmass = ft.Container(
            content=ft.Column([
                col_fruitmass,
            ], spacing=0),
            padding=ft.padding.only(left=10, top=10, right=10),
            alignment=ft.alignment.center,
            #border=ft.border.all()
        )

        # Para 'seeds'
        row_seeds = ft.Container(
            content=ft.Column([
                col_seeds,
            ], spacing=0),
            padding=ft.padding.only(left=10, top=10, right=10),
            alignment=ft.alignment.center,
            #border=ft.border.all()
        )


        row_boton=ft.Container(content=ft.Column([
                col_boton
        ]
        ),
        alignment=ft.alignment.center,
        #border=ft.border.all() 
        #width=360,
        )
        row_resultado=ft.Container(content=ft.Column([
                col_t_resultado,
                col_resultado,
        ]
        ),
        alignment=ft.alignment.center,
        #border=ft.border.all() ,
        width=300,
        )

        #----------------------------------------------------------------------------------------------------------------------------------------------       
        #CONTAINER PRINCIPAL - AQUI ES DONDE LE DIGO A LA APP QUE ME MUESTRE LOS ELEMENTOS QUE HE CREADO

        row_superior=ft.Container(content=ft.Column([
                row_titulo_container,              
        ],spacing=0, horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ), 
        bgcolor=color_primary,
        padding=ft.padding.only(left=20, top=10, bottom=20, right=20),
        )

        row_form=ft.Container(content=ft.Column([
                row_titulo_form,
                row_clonesize,
                row_honeyBee,
                row_bumblesBee,
                row_andrenaBee,
                row_osmiaBee,
                row_MaxTempBS,
                row_MinTempBS,
                row_AverageTempBS,
                row_MaxTempBI,
                row_MinTempBI,
                row_AverageTempBI,
                row_RainingDays,
                row_AverageRainingDays,
                row_fruitset,
                row_fruitmass,
                row_seeds,
                row_boton,
                row_resultado],
                spacing=0,
                alignment=ft.MainAxisAlignment.CENTER,  # Centrar verticalmente
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centrar horizontalmente
                ),
                bgcolor=ft.colors.WHITE,
                margin=10,
                padding=10,
                width=350,
                alignment=ft.alignment.center,
                border_radius=20
                )

        principal_container=ft.Container(content=ft.Column([
                row_superior,
                row_form
        ],
        spacing=0,
        alignment=ft.MainAxisAlignment.CENTER,  # Centrar verticalmente
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centrar horizontalmente
        ), 
        width=360,
        alignment=ft.alignment.center,
        #border=ft.border.all(),
        )


        objetive1_scrollable = ft.ListView(
        controls=[principal_container],
        expand=True,  # Permitir que el contenedor ocupe todo el espacio disponible
        )

        #page.controls.clear()
        page.controls.append(objetive1_scrollable)
        page.update()
ft.app(target=main, assets_dir="assets")


