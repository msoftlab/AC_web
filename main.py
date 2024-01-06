import flet as ft
import pandas as pd

###################################################
###############  Read Data
###################################################



sheet_id = '1z99dlbk4X6Azq1JUswy39yNt0jLyRVo136_FZtcrjXE'
sheet_name = 'AC'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'

df = pd.read_csv(url)



###################################################
###############  Style
###################################################


def btn_style_circle():
	c_style=ft.ButtonStyle(color={
		ft.MaterialState.HOVERED: ft.colors.RED,
	    ft.MaterialState.FOCUSED: ft.colors.RED,
	    ft.MaterialState.DEFAULT: ft.colors.GREY_500,
	    }, 

	    elevation={"pressed": 1, "": 0},
	    overlay_color=ft.colors.TRANSPARENT,
	    animation_duration=300,

	    side={
	    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE),
	    ft.MaterialState.FOCUSED: ft.BorderSide(2, ft.colors.RED),
	    ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.RED),
	    },

	    bgcolor = '#ffffff', 

	    shape=ft.CircleBorder())

	return c_style

style_btn_cir = btn_style_circle()

def btn_style(bg_color=ft.colors.GREEN_50):
	btn_style_normal = ft.ButtonStyle(color={
	    ft.MaterialState.HOVERED: ft.colors.BLACK,
	    ft.MaterialState.FOCUSED: ft.colors.BLACK,
	    ft.MaterialState.DEFAULT: ft.colors.GREY_500,
	    }, 

	    elevation={"pressed": 1, "": 0},
	    overlay_color=bg_color,
	    animation_duration=300,

	    side={
		    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.GREY_300),
		    ft.MaterialState.FOCUSED: ft.BorderSide(2, ft.colors.BLACK),
		    ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.BLACK),
		    },

	    bgcolor = '#ffffff', 

	    shape={
	    ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=15),
	    ft.MaterialState.FOCUSED: ft.RoundedRectangleBorder(radius=15),
	    ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=10),
	    })

	return btn_style_normal

green = btn_style()
pink = btn_style(ft.colors.PINK_50)
blue = btn_style(ft.colors.BLUE_50)

def create_text(txt):
	t = ft.Row(height = 50, 
        controls=[ft.Text(f"{txt}",
            size=15,
            color=ft.colors.BLACK,
            weight=ft.FontWeight.BOLD)],alignment=ft.MainAxisAlignment.CENTER)
	
	return t


######################################################
##################   Append Button list
######################################################

btn_mid = []

######################################################
##################   Interface 
######################################################


def main(page: ft.Page):

	page.title = 'ARCHICAD Learning Notebook_v2.2024'
	page.padding = 30
	page.bgcolor = '#ffffff'
	page.window_maximized = True	


	######################################################
	##################   Function --> Call Button
	######################################################

	def call_btn(e):
		btn_mid.clear()
		page.update()


	def call_btn_mid(name, w = 235, h = 55):
		a = df[df[name].notna()][name].to_list()

		btn_mid.clear()
		for i in a:
			if i.startswith('txt_'):
				t = i.split('_')[1].strip()
				txt = create_text(t)
				btn_mid.append(txt)

			else:
				btn = f'btn_{i}'
				btn = ft.ElevatedButton(f'{i}', width = w, height = h, style = blue)
				btn_mid.append(btn)

		page.update()


	def call_btn_AC(e):
		fun_call =  call_btn_mid('btn_AC')

	def call_btn_bim(e):
		fun_call =  call_btn_mid('btn_bim')

	def call_btn_info(e):
		fun_call =  call_btn_mid('btn_info')

	def call_btn_roadmap(e):
		fun_call =  call_btn_mid('btn_roadmap', w = 250, h= 150)
		
	def call_btn_misconceptions(e):
		fun_call =  call_btn_mid('btn_misconceptions', w = 250)

	def call_btn_basic(e):
		fun_call =  call_btn_mid('btn_basic')

	def call_btn_design(e):
		fun_call =  call_btn_mid('btn_design')

	def call_btn_workingDrawing(e):
		fun_call =  call_btn_mid('btn_workingDrawing')

	def call_btn_bimWorkflow(e):
		fun_call =  call_btn_mid('btn_bimWorkflow')

	def call_btn_websites(e):
		fun_call =  call_btn_mid('btn_websites')

	def call_btn_youtubeChannels(e):
		fun_call =  call_btn_mid('btn_youtubeChannels')

	def call_btn_facebook(e):
		fun_call =  call_btn_mid('btn_facebook')

	def call_btn_articles(e):
		fun_call =  call_btn_mid('btn_articles', h = 100)

	def call_btn_bimStandards(e):
		fun_call =  call_btn_mid('btn_bimStandards', h = 70)

	def call_btn_bimEsubmission(e):
		fun_call =  call_btn_mid('btn_bimEsubmission')

	def call_btn_world(e):
		fun_call =  call_btn_mid('btn_world')


	######################################################
	##################   Create Button _ LEFT
	######################################################


	btn_AC = ft.ElevatedButton('AC', style = style_btn_cir, on_click = call_btn_AC)
	btn_BIM = ft.ElevatedButton('BIM', style = style_btn_cir, on_click = call_btn_bim)
	btn_info = ft.ElevatedButton('Info', style = style_btn_cir, on_click = call_btn_info)

	btn_roadmap = ft.ElevatedButton('BIM ROADMAP', icon = ft.icons.ADD_ROAD_SHARP, width = 200, height = 50, style = pink, on_click = call_btn_roadmap)
	btn_misconceptions = ft.ElevatedButton('MISCONCEPTIONS',  icon = ft.icons.ERROR_OUTLINE, width = 200, height = 50, style = pink, on_click = call_btn_misconceptions)

	txt_1 = create_text('<< Setep by Step >>')

	btn_basic = ft.ElevatedButton('BASIC',  width = 200, height = 50, style = green, on_click = call_btn_basic)
	btn_design = ft.ElevatedButton('DESIGN',  width = 200, height = 50, style = green, on_click = call_btn_design)
	btn_wd = ft.ElevatedButton('WORKING DRAWING',  width = 200, height = 50,style = green, on_click = call_btn_workingDrawing)
	btn_BIM_workflow = ft.ElevatedButton('BIM WORKFLOW',  width = 200, height = 50,style = green, on_click = call_btn_bimWorkflow)
	btn_My_notebook = ft.ElevatedButton('MY NOTEBOOK',  width = 200, height = 50,style = green, on_click = call_btn)

	txt_2 = create_text('<< Resources >>')

	btn_website = ft.ElevatedButton('WEBSITES',  width = 200, height = 50, style = blue, on_click = call_btn_websites)
	btn_youtubeChannel = ft.ElevatedButton('YOUTUBE CHANNELS', width = 200, height = 50, style = blue, on_click = call_btn_youtubeChannels)
	btn_facebook = ft.ElevatedButton('FACEBOOK',  width = 200, height = 50, style = blue, on_click = call_btn_facebook)
	btn_read_article = ft.ElevatedButton('READ ARTICLES',  width = 200, height = 50, style = blue, on_click = call_btn_articles)
	btn_BIM_standard = ft.ElevatedButton('BIM STANDARDS',  width = 200, height = 50, style = blue, on_click = call_btn_bimStandards)
	btn_e_submission = ft.ElevatedButton('BIM e-SUBMISSION',  width = 200, height = 50, style = blue, on_click = call_btn_bimEsubmission)
	btn_world = ft.ElevatedButton('AROUND THE WORLD',  width = 200, height = 50, style = blue, on_click = call_btn_world)
	btn_collabotation = ft.ElevatedButton('BIM COLLABORATION',  width = 200, height = 50, style = blue, on_click = call_btn)

	widget_list_left_bottom = [btn_roadmap, btn_misconceptions, 
							txt_1, btn_basic, btn_design, btn_wd, btn_BIM_workflow, btn_My_notebook,
	  						txt_2, btn_website, btn_youtubeChannel, btn_facebook, btn_read_article, 
	  						btn_BIM_standard, btn_e_submission, btn_world, btn_collabotation]



	######## Create _ Container  #############
	
	container_left_top = ft.Container(width = 250, height = 50,
		alignment = ft.alignment.center,
		bgcolor = '#ffffff',
		content = ft.Row([btn_AC,btn_BIM, btn_info]))

	container_left_bottom = ft.Container(width = 250,
		expand = True,
		bgcolor = '#ffffff',
		border = ft.border.all(1,'#d3d3d3'), 
		padding = ft.padding.only(left=15, top = 15, bottom = 15, right = 10),
		border_radius = 20,
		content = ft.Column(widget_list_left_bottom, scroll=ft.ScrollMode.ALWAYS))

	container_left = ft.Container(  width = 250,
		alignment = ft.alignment.center,
		content = ft.Column([container_left_top, container_left_bottom] ))
		

	container_mid_a = ft.Container(width = 290,
		expand = True,
		bgcolor = '#ffffff',
		padding = ft.padding.only(left=15, top = 15, bottom = 15, right = 5),
		content = ft.Column(btn_mid, scroll=ft.ScrollMode.ALWAYS),
		)

	container_mid = ft.Container(width = 290,
		padding = ft.padding.all(5),
		border = ft.border.all(1,'#d3d3d3'), 
		border_radius = 20,
		alignment = ft.alignment.center,
		content = ft.Column([container_mid_a])
		)

	container_right = ft.Container(
		expand = True,  
		bgcolor = '#ffffff',
		border = ft.border.all(1,'#d3d3d3'), 
		border_radius = 20,
		padding = ft.padding.only(left=15, top = 15, bottom = 15, right = 10),
		content = ft.Column()
		)
	
	body = ft.Container(expand = True,
		content = ft.Row( 
		controls = [container_left,container_mid,container_right]
		))

	page.add(body)	

ft.app(target = main)# , view=ft.AppView.WEB_BROWSER)
