import flet as ft
import speedtest
from time import sleep

def main(page: ft.Page):
    page.title = "Internet Speed Test"
    page.theme_mode = "dark"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.padding = 30
    page.bgcolor = "black"
    page.auto_scroll = True

    page.fonts = {
        "RoosterPersonalUse": "RoosterPersonalUse.ttf",
        "SourceCodePro-BlackItalic": "SourceCodePro-BlackItalic.ttf",
        "SourceCodePro-Bold": "SourceCodePro-Bold.ttf"
    }
    speed_test = speedtest.Speedtest()

    line_01 = ft.Text(value=">press to start...", font_family="SourceCodePro-BlackItalic", color="#ffffff")
    line_02 = ft.Text(value="", font_family="SourceCodePro-BlackItalic", color="#1aff1a")
    line_03 = ft.Text(value="", font_family="SourceCodePro-BlackItalic", color="#1aff1a")
    progress_bar1 = ft.ProgressBar(width=400, color="#0080ff", bgcolor="#eeeeee", opacity=0)
    progress_text1 = ft.Text("  ")
    progress_row1 = ft.Row([progress_text1, progress_bar1])
    line_04 = ft.Text(value="", font_family="SourceCodePro-Bold", color="#ffff00")
    line_05 = ft.Text(value="", font_family="SourceCodePro-BlackItalic", color="#1aff1a")
    line_06 = ft.Text(value="", font_family="SourceCodePro-BlackItalic", color="#1aff1a")
    progress_bar2 = ft.ProgressBar(width=400, color="#0080ff", bgcolor="#eeeeee", opacity=0)
    progress_text2 = ft.Text("  ")
    progress_row2 = ft.Row([progress_text2, progress_bar2])
    line_07 = ft.Text(value="", font_family="SourceCodePro-Bold", color="#ffff00")
    line_08 = ft.Text(value="", font_family="SourceCodePro-Bold", color="#ffffff")
    terminalText = ft.Column([line_01, line_02, line_03, progress_row1, line_04, line_05, line_06, progress_row2, line_07, line_08])

    appTitle = ft.Row(
        [
            ft.Text("Internet ", color="red", font_family="RoosterPersonalUse", style="displayLarge"),
            ft.Text("Speed", color="yellow", font_family="RoosterPersonalUse", style="displayLarge")
        ], alignment="center"
    )

    getSpeedContainer = ft.Container(
        content=terminalText,
        width=200,
        height=100,
        bgcolor="#4d4d4d",
        border_radius=30,
        padding=20,
        animate=ft.animation.Animation(1000, "bounceOut")
    )

    def animate_getSpeedContainer(e):
        progress_row1.opacity=0
        progress_bar1.opacity=0
        progress_bar1.value=None
        progress_row2.opacity=0
        progress_bar2.opacity=0
        progress_bar2.value=None
        line_01.value=""
        line_02.value=""
        line_03.value=""
        line_04.value=""
        line_05.value=""
        line_06.value=""
        line_07.value=""
        line_08.value=""
        
        
        getSpeedContainer.update()
        getSpeedContainer.width = 700
        getSpeedContainer.height = 400
        line_01.value = ">calculating download speed, please wait!"
        getSpeedContainer.update()
        sleep(1)

        ideal_server = speed_test.get_best_server()
        city = ideal_server["name"]
        country = ideal_server["country"]
        cc = ideal_server["cc"]
        line_02.value = f">finding the best possible server in {city}, {country}, {cc}"
        getSpeedContainer.update()
        sleep(1)

        line_03.value = ">connection established, status OK, fetching the download speed"
        progress_row1.opacity = 1
        progress_bar1.opacity = 1
        getSpeedContainer.update()
        
        download_speed = speed_test.download() / 1024 / 1024
        progress_bar1.value = 1
        getSpeedContainer.update()

        line_04.value = f">the download speed is {str(round(download_speed, 2))} Mbps"
        getSpeedContainer.update()
        sleep(2)

        line_05.value = ">calculating upload speed, please wait"
        getSpeedContainer.update()
        sleep(1)

        line_06.value = ">executing upload script, hold on"
        progress_row2.opacity = 1
        progress_bar2.opacity = 1
        getSpeedContainer.update()

        upload_speed = speed_test.upload() / 1024 / 1024
        progress_bar2.value = 1
        getSpeedContainer.update()
        
        line_07.value = f">the upload speed is {str(round(upload_speed, 2))} Mbps"
        getSpeedContainer.update()
        sleep(1)

        line_08.value = ">task completed successfully\n\n>>app developer: N. Sherone"
        getSpeedContainer.update()

    page.add(
        appTitle,
        getSpeedContainer,
        ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=animate_getSpeedContainer, icon_size=50)
    )

ft.app(target=main, assets_dir="assets")
